# author Laura Diosan
# created on ${10-11-2024-10-45}

# Problema 1
# Sa se precizeze care dintre urmatorii algoritmi determina prima cifra (cea mai din stanga) a unui numar care nu se repeta printre cifrele sale. 
# Raspuns corect: v1 si v2 (dar v1 foloseste dictioanre, v2 liste - in pseudocod putem diferentia intre dictionare si liste !?!)

def first_non_repeating_digit(n): 
    digit_count = {} 
    for digit in str(n): 
        digit_count[digit] = digit_count.get(digit, 0) + 1 
    for digit in str(n): 
        if digit_count[digit] == 1: 
            return int(digit) 
    return None

def test_first_non_repeating_digit(): 
    assert first_non_repeating_digit(112234455) == 3 
    assert first_non_repeating_digit(1023456789) == 1 
    assert first_non_repeating_digit(1122334455) == None 
    assert first_non_repeating_digit(111222333444555) == None 
    assert first_non_repeating_digit(12120) == 0 
    print("All tests pass")

test_first_non_repeating_digit()

def first_non_repeating_digit_v2(n):
    digit_count = [0] * 10
    for digit in str(n):
        digit_count[int(digit)] += 1
    for digit in str(n):
        if digit_count[int(digit)] == 1: 
            return int(digit)
    return None


def test_first_non_repeating_digit_v2(): 
    assert first_non_repeating_digit_v2(112234455) == 3 
    assert first_non_repeating_digit_v2(1023456789) == 1 
    assert first_non_repeating_digit_v2(1122334455) == None 
    assert first_non_repeating_digit_v2(111222333444555) == None 
    assert first_non_repeating_digit_v2(12120) == 0 
    print("All tests v2 pass")

test_first_non_repeating_digit_v2()

def first_non_repeating_digit_v3(n):
    digit_count = [0] * 10
    for digit in str(n):
        digit_count[int(digit)] += 1
    for digit in range(0,10):
        if digit_count[digit] == 1: 
            return int(digit)
    return None


def test_first_non_repeating_digit_v3(): 
    assert first_non_repeating_digit_v3(112234455) == 3 
    assert not first_non_repeating_digit_v3(1023456789) == 1 
    assert first_non_repeating_digit_v3(1122334455) == None 
    assert first_non_repeating_digit_v3(111222333444555) == None 
    assert first_non_repeating_digit_v3(12120) == 0 
    print("All tests v3 pass")

test_first_non_repeating_digit_v3()


def first_non_repeating_digit_v4(n):
    digit_count = [1] * 10
    for digit in str(n):
        digit_count[int(digit)] += 1
    for digit in str(n):
        if digit_count[int(digit)] == 1: 
            return int(digit)
    return None


def test_first_non_repeating_digit_v4(): 
    assert not first_non_repeating_digit_v4(112234455) == 3 
    assert not first_non_repeating_digit_v4(1023456789) == 1 
    assert first_non_repeating_digit_v4(1122334455) == None 
    assert first_non_repeating_digit_v4(111222333444555) == None 
    assert not first_non_repeating_digit_v4(12120) == 0 
    print("All tests v4 pass")

test_first_non_repeating_digit_v4()


# Problema 2
# Care dintre urmatorii algoritmi verifica daca un numar este puteere a lui 2.
# toate cele 4 versiuni

def is_power_of_two(n): 
    return n > 0 and (n & (n - 1)) == 0

def test_is_power_of_two(): 
    assert is_power_of_two(1) 
    assert is_power_of_two(2) 
    assert is_power_of_two(4) 
    assert is_power_of_two(8) 
    assert not is_power_of_two(3) 
    assert not is_power_of_two(5) 
    assert not is_power_of_two(6) 
    assert not is_power_of_two(7) 
    print("All tests power of two pass")

test_is_power_of_two()

import math 
def is_power_of_two_v2(n): 
    if n <= 0: 
        return False 
    return math.log2(n).is_integer()

def test_is_power_of_two_v2(): 
    assert is_power_of_two_v2(1) 
    assert is_power_of_two_v2(2) 
    assert is_power_of_two_v2(4) 
    assert is_power_of_two_v2(8) 
    assert not is_power_of_two_v2(3) 
    assert not is_power_of_two_v2(5) 
    assert not is_power_of_two_v2(6) 
    assert not is_power_of_two_v2(7) 
    print("All tests power of two v2 pass")

test_is_power_of_two_v2()

def is_power_of_two_v3(n): 
    if n <= 0: 
        return False 
    while n % 2 == 0: 
        n /= 2 
    return n == 1

def test_is_power_of_two_v3(): 
    assert is_power_of_two_v3(1) 
    assert is_power_of_two_v3(2) 
    assert is_power_of_two_v3(4) 
    assert is_power_of_two_v3(8) 
    assert not is_power_of_two_v3(3) 
    assert not is_power_of_two_v3(5) 
    assert not is_power_of_two_v3(6) 
    assert not is_power_of_two_v3(7) 
    print("All tests power of two v3 pass")

test_is_power_of_two_v3()

def is_power_of_two_v4(n): 
    if n <= 0: 
        return False 
    if n == 1: 
        return True 
    if n % 2 != 0: 
        return False 
    return is_power_of_two(n // 2)

def test_is_power_of_two_v4(): 
    assert is_power_of_two_v4(1) 
    assert is_power_of_two_v4(2) 
    assert is_power_of_two_v4(4) 
    assert is_power_of_two_v4(8) 
    assert not is_power_of_two_v4(3) 
    assert not is_power_of_two_v4(5) 
    assert not is_power_of_two_v4(6) 
    assert not is_power_of_two_v4(7) 
    print("All tests power of two v4 pass")

test_is_power_of_two_v4()

# Problema 3
#  Precizati ce efect are aplicarea urmatorului algoritm asupra unei matrici patratice mat:
# a) algoritmul returneaza transpusa matricii mat
# b) algoritmul roteste matricea mat cu 90 de grade in sensul acelor de ceasornic
# c) algoritmul roteste matricea mat cu 180 de grade in sensul acelor de ceasornic
# d) algoritmul ordoneaza pe linii elementele matricii mat

# raspuns corect: a

def process_matrix(mat): 
    m, n = len(mat), len(mat[0]) 
    new_mat = [[0] * m for _ in range(n)] 
    for i in range(m): 
        for j in range(n): 
            new_mat[j][i] = mat[i][j] 
    return new_mat

def process_matrix_in_place(mat): 
    m, n = len(mat), len(mat[0]) 
    for i in range(m): 
        for j in range(i + 1, n): 
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j] 
    return mat

def test_process_matrix(): 
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
    assert process_matrix(mat) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 
    assert process_matrix_in_place(mat) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]] 

    mat = [[1, 2], [4, 5]] 
    assert process_matrix(mat) == [[1, 4], [2, 5]] 
    assert process_matrix_in_place(mat) == [[1, 4], [2, 5]] 

    mat = [[1]] 
    assert process_matrix(mat) == [[1]] 
    assert process_matrix_in_place(mat) == [[1]] 

    print("All tests matrix pass")

test_process_matrix()
