"""attention_utils.py
Reusable utilities for presenting attention mechanisms in lecture notebooks.
"""
from typing import Optional, Tuple, List
import math
import numpy as np
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt

# -----------------------------
# Tokenization & Embeddings
# -----------------------------

def simple_tokenize(text: str) -> List[str]:
    """Very simple whitespace/punctuation tokenizer (for didactic demos).
    """
    return [t for t in text.replace(',', ' ').replace('.', ' ').split() if t]

class TinyEmbed:
    """Random embeddings for demo purposes (no training).
    Missing tokens map to zeros.
    """
    def __init__(self, vocab: List[str], d: int = 16, device: Optional[torch.device] = None):
        self.d = d
        self.device = device or torch.device('cpu')
        self.table = {w: torch.randn(d, device=self.device) for w in vocab}
    def __call__(self, tokens: List[str]) -> torch.Tensor:
        return torch.stack([self.table.get(t, torch.zeros(self.d, device=self.device)) for t in tokens])

# -----------------------------
# Unified Attention Core
# -----------------------------

def scaled_dot_product_attention(
    queries: torch.Tensor,   # [B, q, d]
    keys: torch.Tensor,      # [B, n, d]
    values: torch.Tensor,    # [B, n, d]
    mask: Optional[torch.Tensor] = None,  # broadcastable to [B, q, n]; True=keep
    scale: Optional[float] = None,
) -> Tuple[torch.Tensor, torch.Tensor]:
    """Compute scaled dot-product attention.
    Returns:
        context: [B, q, d]
        weights: [B, q, n] (row-wise softmax)
    """
    B, q, d = queries.shape
    scale = (d ** 0.5) if scale is None else scale
    scores = torch.einsum('bqd,bnd->bqn', queries, keys) / scale
    if mask is not None:
        mask = mask.to(dtype=torch.bool)
        # Use the minimum representable value of dtype to avoid NaNs in softmax
        scores = scores.masked_fill(~mask, torch.finfo(scores.dtype).min)
    weights = torch.softmax(scores, dim=-1)
    context = torch.einsum('bqn,bnd->bqd', weights, values)
    return context, weights

# Wrappers for clarity

def soft_attention_unified(queries: torch.Tensor, keys: torch.Tensor, values: torch.Tensor, mask: Optional[torch.Tensor] = None):
    return scaled_dot_product_attention(queries, keys, values, mask)


def self_attention_unified(x: torch.Tensor, mask: Optional[torch.Tensor] = None):
    return scaled_dot_product_attention(x, x, x, mask)


def cross_attention_unified(queries: torch.Tensor, encoder_keys: torch.Tensor, encoder_values: torch.Tensor, mask: Optional[torch.Tensor] = None):
    return scaled_dot_product_attention(queries, encoder_keys, encoder_values, mask)

# -----------------------------
# Masks
# -----------------------------

def causal_mask(n: int, device: Optional[torch.device] = None) -> torch.Tensor:
    device = device or torch.device('cpu')
    return torch.ones(n, n, dtype=torch.bool, device=device).tril().unsqueeze(0)  # [1, n, n]


def local_mask(q: int, n: int, w: int, device: Optional[torch.device] = None) -> torch.Tensor:
    device = device or torch.device('cpu')
    M = torch.zeros(q, n, dtype=torch.bool, device=device)
    for i in range(q):
        left = max(0, i - w)
        right = min(n, i + w + 1)
        M[i, left:right] = True
    return M.unsqueeze(0)  # [1, q, n]

# Sparse mask zoo (for long sequences)

def sliding_window_mask(n: int, w: int, device: Optional[torch.device] = None) -> torch.Tensor:
    device = device or torch.device('cpu')
    M = torch.zeros(n, n, dtype=torch.bool, device=device)
    for i in range(n):
        M[i, max(0, i - w): min(n, i + w + 1)] = True
    return M.unsqueeze(0)


def longformer_mask(n: int, w: int, global_idx: Optional[List[int]] = None, device: Optional[torch.device] = None) -> torch.Tensor:
    M = sliding_window_mask(n, w, device=device)[0]
    if global_idx:
        M[global_idx, :] = True
        M[:, global_idx] = True
    return M.unsqueeze(0)


def block_sparse_mask(n: int, block_size: int = 4, band: int = 1, device: Optional[torch.device] = None) -> torch.Tensor:
    device = device or torch.device('cpu')
    nb = (n + block_size - 1) // block_size
    M = torch.zeros(n, n, dtype=torch.bool, device=device)
    for b in range(nb):
        for u in range(max(0, b - band), min(nb, b + band + 1)):
            br = slice(b * block_size, min(n, (b + 1) * block_size))
            ur = slice(u * block_size, min(n, (u + 1) * block_size))
            M[br, ur] = True
    return M.unsqueeze(0)


def dilated_mask(n: int, w: int, dilation: int = 2, device: Optional[torch.device] = None) -> torch.Tensor:
    device = device or torch.device('cpu')
    M = torch.zeros(n, n, dtype=torch.bool, device=device)
    for i in range(n):
        for k in range(-w, w + 1):
            j = i + k * dilation
            if 0 <= j < n:
                M[i, j] = True
    return M.unsqueeze(0)


def strided_mask(n: int, stride: int = 4, include_self: bool = True, device: Optional[torch.device] = None) -> torch.Tensor:
    device = device or torch.device('cpu')
    M = torch.zeros(n, n, dtype=torch.bool, device=device)
    for i in range(n):
        M[i, i % stride::stride] = True
        if include_self:
            M[i, i] = True
    return M.unsqueeze(0)


def bigbird_mask(n: int, w: int = 2, r: int = 3, global_idx: Optional[List[int]] = None, device: Optional[torch.device] = None) -> torch.Tensor:
    device = device or torch.device('cpu')
    M = sliding_window_mask(n, w, device=device)[0]
    rng = np.random.default_rng(0)
    for i in range(n):
        choices = rng.choice(n, size=min(r, n), replace=False)
        M[i, choices] = True
    if global_idx:
        M[global_idx, :] = True
        M[:, global_idx] = True
    return M.unsqueeze(0)

# -----------------------------
# Diagnostics & Visualization
# -----------------------------

def mask_density(M: torch.Tensor) -> Tuple[float, int, int]:
    m = M.bool()
    q, n = m.shape[-2], m.shape[-1]
    nz = int(m.sum().item())
    return nz / (q * n), nz, q * n

class AttentionVisualizer:
    def __init__(self, tokens_x: List[str], tokens_y: Optional[List[str]] = None):
        self.tokens_x = tokens_x
        self.tokens_y = tokens_x if tokens_y is None else tokens_y

    def show_bars(self, weights_1d, title="Attention weights", color="#2D6A4F"):
        fig, ax = plt.subplots(1, 1)
        ax.bar(range(len(self.tokens_x)), weights_1d, color=color)
        ax.set_xticks(range(len(self.tokens_x)))
        ax.set_xticklabels(self.tokens_x, rotation=45, ha='right')
        ax.set_title(title); ax.set_ylabel("weight")
        plt.tight_layout(); plt.show()

    def show_matrix(self, W_2d, title="Attention (q × n)", cmap="Greens"):
        fig, ax = plt.subplots(1, 1)
        im = ax.imshow(W_2d, cmap=cmap)
        ax.set_xticks(range(len(self.tokens_y)))
        ax.set_xticklabels(self.tokens_y, rotation=45, ha='right')
        ax.set_yticks(range(len(self.tokens_x)))
        ax.set_yticklabels(self.tokens_x)
        ax.set_title(title)
        fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        plt.tight_layout(); plt.show()

# -----------------------------
# Multi-head demo (didactic)
# -----------------------------

def multihead_self_attention_demo(X: torch.Tensor, heads: int = 4):
    B, n, d = X.shape
    per_head = max(1, d // heads)
    Ws = []
    for _ in range(heads):
        proj = torch.randn(per_head, d, device=X.device) / (d ** 0.5)
        Xh = X @ proj.T  # [B, n, per_head]
        _, Wh = self_attention_unified(Xh)   # [B, n, n]
        Ws.append(Wh)
    W_stack = torch.stack(Ws, dim=0)  # [h, B, n, n]
    W_mean = W_stack.mean(dim=0)      # [B, n, n]
    return Ws, W_mean

# -----------------------------
# One-call demo runner (optional)
# -----------------------------

def run_demo(text: str, mode: str = "self", mask: Optional[torch.Tensor] = None, query_token: str = "<query>"):
    tokens = simple_tokenize(text)
    emb = TinyEmbed(sorted(set(tokens + [query_token])), d=16)
    X = emb(tokens).unsqueeze(0)  # [1, n, d]
    viz = AttentionVisualizer(tokens)
    if mode == "soft":
        q = emb([query_token]).unsqueeze(0)  # [1, 1, d]
        ctx, W = scaled_dot_product_attention(q, X, X, mask=mask)
        viz.show_bars(W[0,0].detach().cpu().numpy(), "Soft attention")
    elif mode == "cross":
        q = emb([tokens[0]]).unsqueeze(0)    # pretend a target query
        ctx, W = scaled_dot_product_attention(q, X, X, mask=mask)
        viz = AttentionVisualizer([tokens[0]], tokens)
        viz.show_matrix(W[0].detach().cpu().numpy(), "Cross attention", cmap="Blues")
    else:  # self
        ctx, W = self_attention_unified(X, mask=mask)
        viz.show_matrix(W[0].detach().cpu().numpy(), "Self attention", cmap="Greens")
    return ctx, W, tokens

# -----------------------------
# Hard attention variants
# -----------------------------

def greedy_hard_attention(queries: torch.Tensor, keys: torch.Tensor, values: torch.Tensor):
    scores = torch.einsum('bqd,bnd->bqn', queries, keys)
    idx = scores.argmax(dim=-1)  # [B, q]
    B, q, n = scores.shape
    one_hot = torch.zeros(B, q, n, device=queries.device)
    for b in range(B):
        for i in range(q):
            one_hot[b, i, idx[b, i]] = 1.0
    context = torch.einsum('bqn,bnd->bqd', one_hot, values)
    return context, one_hot


def gumbel_softmax_attention(queries: torch.Tensor, keys: torch.Tensor, values: torch.Tensor, tau: float = 0.7, hard: bool = True):
    scores = torch.einsum('bqd,bnd->bqn', queries, keys)
    U = torch.rand_like(scores)
    g = -torch.log(-torch.log(U + 1e-9) + 1e-9)
    logits = (scores + g) / max(tau, 1e-6)
    weights = torch.softmax(logits, dim=-1)
    if hard:
        idx = weights.argmax(dim=-1, keepdim=True)
        one_hot = torch.zeros_like(weights).scatter_(-1, idx, 1.0)
        weights = (one_hot - weights).detach() + weights
    context = torch.einsum('bqn,bnd->bqd', weights, values)
    return context, weights
