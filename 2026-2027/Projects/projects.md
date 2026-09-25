
# Teme de proiect MIRPR 2026-2027


<!-- Onco - lung, breast -->
<!-- cardiologie - 6 oct -->
<!-- Voice -->
<!-- Stoma
Cristiana - Nagarro
Farmacie
Marsh -->

## Project 1

<details>
    <summary> Identificarea cancerului de plaman  (owner: dl. dr. Andrei Roman) 
    <img src="project-images\lungCancer.jpeg" width="100">
    </summary>

### Identificarea cancerului de plaman

#### Scop
Dezvoltarea unui sistem inteligent care să ajute medicii în diagnosticarea timpurie a cancerului de plămân.

#### Ideea de baza
Deși cancerul pulmonar este recunoscut ca fiind cel mai mortal tip de cancer, un prognostic bun și un tratament eficient depind de detectarea timpurie a acestuia. Povara medicilor poate fi redusa cu ajutorul tehnicilor de AI care sunt esențiale în automatizarea diagnosticului și clasificării bolilor. De aceea, se dorește dezvoltarea unui sistem inteligent care să ajute medicii în diagnosticarea timpurie a cancerului de plămân. 

Se va urmari dezvoltarea unor modele inteligente capabine sa analizeze scanarile CT/PET si sa prezica diferiti biomarkeri tumorali folosind doar:
- 3D Segmented CT scans (maybe PET)
- Biopsy confirmed IHC markers (maybe genomic too)
- Age
- Gender
Scopul este construirea unei "biopsii virtuale" care să sprijine radiologii în timpul diagnosticului. 

Problema poate fi abordata ca o problema de clasificare multi-label. 

#### Data
- Chest CT-scane images [link](https://www.kaggle.com/datasets/mohamedhanyyy/chest-ctscan-images/data)
- Lung Image Database Consortium image collection (LIDC-IDRI) [link](https://www.cancerimagingarchive.net/collection/lidc-idri/)

#### Bibliografie
- Shao J, Ma J, Zhang S, Li J, Dai H, Liang S, Yu Y, Li W, Wang C. Radiogenomic System for Non-Invasive Identification of Multiple Actionable Mutations and PD-L1 Expression in Non-Small Cell Lung Cancer Based on CT Images. Cancers. 2022; 14(19):4823 [link](https://doi.org/10.3390/cancers14194823)
- Owens CA, Peterson CB, Tang C, Koay EJ, Yu W, et al. (2018) Lung tumor segmentation methods: Impact on the uncertainty of radiomics features for non-small cell lung cancer. PLOS ONE 13(10): e0205003 [link](https://doi.org/10.1371/journal.pone.0205003)
- Majumder S, Katz S, Kontos D, Roshkovan L. State of the art: radiomics and radiomics-related artificial intelligence on the road to clinical translation. BJR Open. 2023 Dec 12;6(1):tzad004. doi: 10.1093/bjro/tzad004. PMID: 38352179; PMCID: PMC10860524.
- Liu, J. A., Yang, I. Y., & Tsai, E. B. (2022). Artificial intelligence (AI) for lung nodules, from the AJR special series on AI applications. American Journal of Roentgenology, 219(5), 703-712. [link](https://ajronline.org/doi/10.2214/AJR.22.27487) 
- Gu, Y., Chi, J., Liu, J., Yang, L., Zhang, B., Yu, D., ... & Lu, X. (2021). A survey of computer-aided diagnosis of lung nodules from CT scans using deep learning. Computers in biology and medicine, 137, 104806. [link](https://www.sciencedirect.com/science/article/pii/S0010482521006004?casa_token=qhi8cSHcd5UAAAAA:iUwm4l441GNq0Ph2QQ8gW5tConmiyHUtm6ynRLEi1b7Io2HdL6qI0hSggNQPfHWn16XeO4FDNQ#sec4)
- Javed, R., Abbas, T., Khan, A. H., Daud, A., Bukhari, A., & Alharbey, R. (2024). Deep learning for lungs cancer detection: a review. Artificial Intelligence Review, 57(8), 197. [link](https://link.springer.com/article/10.1007/s10462-024-10807-1)
- Shatnawi, M. Q., Abuein, Q., & Al-Quraan, R. (2025). Deep learning-based approach to diagnose lung cancer using CT-scan images. Intelligence-Based Medicine, 11, 100188. [link](https://www.sciencedirect.com/science/article/pii/S2666521224000553#bib41)
- Hiraman, A., Viriri, S., & Gwetu, M. (2024). Lung tumor segmentation: a review of the state of the art. Frontiers in Computer Science, 6, 1423693. [link](https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2024.1423693/full)
- Jayaram, J., Haw, S. C., Palanichamy, N., Anaam, E., & Kumar, S. (2025). A Systematic Review on Effectiveness and Contributions of Machine Learning and Deep Learning Methods in Lung Cancer Diagnosis and Classifications. International Journal of Computing, 17(1), 1-12. [link](https://iiict.uob.edu.bh/IJCDS/papers/1571032811.pdf)

</details>

## Project 2
<details>
    <summary> Identificarea cancerului de san  (owner: dl. dr. Andrei Roman) 
        <img src="project-images\breastCancer.jpeg" width="100">
    </summary>

### Identificarea cancerului de san

#### Scop
Dezvoltarea unui sistem inteligent care să ajute medicii în diagnosticarea timpurie a cancerului de san.

#### Ideea de baza
Detectarea cancerului de sân în mamografii este o problemă critică în imagistica medicală și diagnostic. Interpretarea mamografiilor este provocatoare din cauza variațiilor în densitatea țesuturilor, a structurilor suprapuse și a diferențelor subtile dintre tumorile benigne și maligne. 
Această problemă trebuie rezolvată folosind un algoritm inteligent, deoarece examinarea manuală tradițională de către radiologi este consumatoare de timp și predispusă la erori umane. 

Plecand de la seturile de date cu mamografii, se vor folosii modele de AI bazate pe arhitecturi de tip Transformer/GNN pentru a identifica tumori maligne si benigne in imagini. Modelele folosite pot fi pre-antrenate pe alte seturi de date si fine-tunate pe setul de date cu mamografii.

#### Data
- MIAS [link](http://peipa.essex.ac.uk/info/mias.html)
- DDSM [link](http://www.eng.usf.edu/cvprg/Mammography/Database.html) or [link](https://www.cancerimagingarchive.net/collection/cbis-ddsm/)
- INbreast  [link](https://www.kaggle.com/datasets/tommyngx/inbreast2012)
- DBT - [link](https://www.cancerimagingarchive.net/collection/breast-cancer-screening-dbt/)

#### Bibliografie
- Graph CNNs 
    - PyG [link](https://github.com/pyg-team/pytorch_geometric) 
    - Graph Learning resources [link](https://snap.stanford.edu/graphlearning-workshop/)
    - GNNs for breast cancer - Chowa, S. S., Azam, S., Montaha, S., Payel, I. J., Bhuiyan, M. R. I., Hasan, M. Z., & Jonkman, M. (2023). Graph neural network-based breast cancer diagnosis using ultrasound images with optimized graph construction integrating the medically significant features. Journal of Cancer Research and Clinical Oncology, 149(20), 18039-18064. [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC10725367/)
    - GNNs for breast cancer -  Agyekum, E. A., Kong, W., Ren, Y. Z., Issaka, E., Baffoe, J., Xian, W., ... & Shen, X. (2025). A comparative analysis of three graph neural network models for predicting axillary lymph node metastasis in early-stage breast cancer. Scientific Reports, 15(1), 13918. [link](https://www.nature.com/articles/s41598-025-97257-z)
- Transformers
    - Vit - Dosovitskiy, A. (2020). An image is worth 16x16 words: Transformers for image recognition at scale. arXiv preprint arXiv:2010.11929.
        [link](https://arxiv.org/pdf/2010.11929)
        - Code [link](https://github.com/google-research/vision_transformer) or HuggingFace models [link](https://huggingface.co/docs/transformers/en/model_doc/vit)
    - CrossViT - Chen, C. F. R., Fan, Q., & Panda, R. (2021). Crossvit: Cross-attention multi-scale vision transformer for image classification. In Proceedings of the IEEE/CVF international conference on computer vision (pp. 357-366). [link](https://openaccess.thecvf.com/content/ICCV2021/papers/Chen_CrossViT_Cross-Attention_Multi-Scale_Vision_Transformer_for_Image_Classification_ICCV_2021_paper.pdf)
        - Code [link](https://github.com/IBM/CrossViT)
    - DeiT - Touvron, H., Cord, M., Douze, M., Massa, F., Sablayrolles, A., & Jégou, H. (2020). Training data-efficient image transformers & distillation through attention. arXiv 2020. arXiv preprint arXiv:2012.12877, 2(3). \href{https://arxiv.org/abs/2012.12877v2}{link}
        - Code [link](https://github.com/facebookresearch/deit/tree/2aefd8fc8634d099c1495ce9dba2b6c6a921d611)
    - MammoViT - Al Mansour, A. G., Alshomrani, F., Alfahaid, A., & Almutairi, A. T. (2025). MammoViT: A Custom Vision Transformer Architecture for Accurate BIRADS Classification in Mammogram Analysis. Diagnostics, 15(3), 285 [link](https://www.mdpi.com/2075-4418/15/3/285)
    - Gutierrez-Cardenas, J. (2024). Breast Cancer Classification Through Transfer Learning with Vision Transformer, PCA, and Machine Learning Models. International Journal of Advanced Computer Science & Applications, 15(4). [link](https://www.proquest.com/docview/3060148581?fromopenview=true&pq-origsite=gscholar&sourcetype=Scholarly%20Journals)
</details>




## Project 3
<details>
    <summary> Automatizarea intocmirii fisei pacientului  (owner: dna. dr. Alina Baciu) 
    <img src="project-images\voice.avif" width="150">
    </summary>

### Automatizarea intocmirii fisei pacientului

#### Scop
Dezvoltarea unui sistem inteligent care să ajute medicii pentru a completa in mod automat fisa pacientului.

#### Ideea de baza
Munca medicilor este plina de provocari. Mai ales cand trebuie sa faca multe task-uri, uneori simultan, precum realizarea si citirea unei ecografii si inregistrarea observatiilor facute. De aceea este nevoie de un sistem inteligent care sa transforme informatia audio inregistrata de catre un medic in format text si sa completeze in mod automat rubricile dedicate din fisa pacientului.
Se va pleca de la inregistrari audio precum [aceasta](projects/voice2text/test1.ogg), se vor converti in format text si se va compelta automat partea evidentiata cu galben din fisa pacientului, precum [aceasta](projects/voice2text/patient1.odt) (informatiile respective se vor salva intr-un tabel/jason si apoi se vor exporta intr-un document word)

#### Data
- inregistrari audio [link](projects/voice2text/test1.ogg) [link](projects/voice2text/test2.ogg) [link](projects/voice2text/test3.ogg)
- fisa pacientului [link](projects/voice2text/patient1.odt)
 
#### Bibliografie
- [Whisper](https://openai.com/index/whisper/)
- [DeepSpeech](https://github.com/mozilla/DeepSpeech)
- [RobinASR](https://github.com/racai-ai/RobinASR) - for romanian
- [speech2text](https://huggingface.co/docs/transformers/model_doc/speech_to_text)
- [wav2vec](https://ai.meta.com/research/impact/wav2vec/)
- [wav2vec2](https://huggingface.co/docs/transformers/model_doc/wav2vec2)
- [romanian wav2vec2](https://huggingface.co/gigant/romanian-wav2vec2)
- [wavLM](https://huggingface.co/docs/transformers/model_doc/wavlm)

</details>


## Project 4
<details>
    <summary>  De la interfața cutanată la simulator digital cardiac: optimizarea asistată de inteligență artificială a senzorilor ECG purtabili imprimați 3D (Owner: dl. dr. Dan Blendea, prof. dr. Zoltan Balint) <img  style="vertical-align:middle" src="project-images\smartWatch.png" alt="networks" width="100"/> </summary>

### De la interfața cutanată la simulatorul digital cardiac: optimizarea asistată de inteligență artificială a senzorilor ECG purtabili imprimați 3D (From Skin Interface to Cardiac Digital Twin: AI-Guided Optimization of 3D-Printed Wearable ECG Sensors)

#### Scop
Dezvoltarea și optimizarea unor senzori ECG purtabili imprimați 3D, utilizând metode de inteligență artificială pentru a îmbunătăți calitatea semnalului, confortul utilizatorului și robustețea măsurătorilor. Obiectivul final este integrarea senzorilor într-un flux care permite construirea unui simulator digital cardiac personalizat.

#### Ideea de baza
Senzorii ECG purtabili sunt influențați de numeroși factori: geometria electrodului, materialul utilizat, poziționarea pe corp, mișcarea utilizatorului și caracteristicile individuale ale pielii. Proiectul urmărește utilizarea tehnicilor AI pentru: predicția calității semnalului ECG; optimizarea parametrilor de fabricație și utilizare; detectarea și eliminarea artefactelor; estimarea parametrilor fiziologici relevanți; furnizarea datelor necesare unui geamăn digital cardiac. Se vor compara mai multe metode.
 
#### Data
- [link](https://bmcresnotes.biomedcentral.com/articles/10.1186/s13104-022-06146-5
https://www.researchgate.net/publication/378021834_Analysis_of_Fitness_Based_on_Smart_Watch_Data)
- [link](https://ceur-ws.org/Vol-3514/paper73.pdf)
- PhysioNet ECG Databases (MIT-BIH, PTB-XL etc.)
- date ECG provenite din dispozitive wearable comerciale;
- date sintetice generate cu simulatoare ECG;

#### Bibliografie
- Mogra, A., Pandey, P. K., & Panwar, R. S. (2024, December). Artificial Intelligence Enabled Sleep Health Dashboards: Power BI Integration for Data-Driven Lifestyle Modifications. In 2024 Eighth International Conference on Parallel, Distributed and Grid Computing (PDGC) (pp. 535-539). IEEE [link](https://ieeexplore.ieee.org/abstract/document/10984363)
- Reddy, N. C. N., Ramesh, A., Rajasekaran, R., & Masih, J. (2020, May). Ritchie’s Smart Watch Data Analytics and Visualization. In International Conference on Image Processing and Capsule Networks (pp. 776-784). Cham: Springer International Publishing.[link](https://d1wqtxts1xzle7.cloudfront.net/96645011/978-3-030-51859-2_70-libre.pdf?1672579590=&response-content-disposition=inline%3B+filename%3DRitchie_s_Smart_Watch_Data_Analytics_and.pdf&Expires=1759213247&Signature=QSkC1ZZ1hezkhPx2bnqrWfikyhAPRw8R83lYHOrsKW2GA4nfVd~kOZ-RvFPbNCPPnK9x6b66MnJYvnR1VElnEt~Nn8dsjHjiR4WpKMJ8KhfpSqKeoPoEmTSPtTo57lcLSAyLr7XL0tbdk5YpxUrrK6GcHpG7YTfUrOu9Xh2lxi~-V1DOXFkhtHqw9wtWGoniLusVXsLuGaGdQibTMUCEUmV5Cw-fISVvv170AiNH-Lb5z4yZqaunHabVBOBWQ~dhzedn~7G7PPQEdWcIBSXf~uxQDpCfXlzRQ1F-Xh2dBDZFyOru9AxMKgElC6a6f5jMIn6YLQwPTpZBiSgW~YZYEQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)
- Bhavsar, K., Singhal, S., Chandel, V., Samal, A., Khandelwal, S., Ahmed, N., & Ghose, A. (2021, March). Digital biomarkers: Using smartwatch data for clinically relevant outcomes. In 2021 IEEE International Conference on Pervasive Computing and Communications Workshops and other Affiliated Events (PerCom Workshops) (pp. 630-635). IEEE. [link](https://ieeexplore.ieee.org/abstract/document/9431000)
- Del-Valle-Soto, C., Briseño, R. A., Valdivia, L. J., & Nolazco-Flores, J. A. (2024). Unveiling wearables: exploring the global landscape of biometric applications and vital signs and behavioral impact. BioData Mining, 17(1), 15. [link](https://link.springer.com/content/pdf/10.1186/s13040-024-00368-y.pdf)

</details>


## Project 5
<details>
    <summary>  Simulator digital al valvei mitrale asistat de inteligență artificială pentru simularea intervențiilor virtuale în regurgitarea mitrală funcțională  (Owner: dl. dr. Dan Blendea, prof. dr. Zoltan Balint) <img  style="vertical-align:middle" src="project-images\AI-Mitral-Valve-Digital-Twin.png" alt="networks" width="100"/> </summary>

### Simulator digital al valvei mitrale asistat de inteligență artificială pentru simularea intervențiilor virtuale în regurgitarea mitrală funcțională (AI-Enabled Electromechanical Mitral-Valve Digital Twin for Virtual Intervention Simulation in Functional Mitral Regurgitation)

#### Scop
Dezvoltarea unui simulator digital al valvei mitrale care combină modele anatomice, biomecanice și electrofiziologice pentru simularea și evaluarea virtuală a intervențiilor asociate regurgitării mitrale funcționale.

#### Ideea de baza
Regurgitarea mitrală funcțională este o afecțiune complexă în care modificările ventriculului stâng afectează funcționarea valvei mitrale. Un simulator digital poate fi utilizat pentru: simularea evoluției bolii; evaluarea diferitelor strategii terapeutice; analiza impactului modificărilor anatomice; predicția rezultatelor post-intervenție.

Componenta AI poate fi utilizată pentru: segmentarea imaginilor ecografice sau RMN; estimarea parametrilor biomecanici; reducerea costului computațional al simulărilor; predicția succesului intervențiilor; explicarea factorilor care influențează prognosticul.
 
#### Data
- [CAMUS](https://www.creatis.insa-lyon.fr/Challenge/camus/)
- [ACDC](https://www.creatis.insa-lyon.fr/Challenge/acdc/databases.html)
- [STACOM](https://www.cardiacatlas.org/)
- [SimTK](https://simtk.org/projects/cardiacatlas)
- [OpenCMISS](https://www.opencmiss.org/)

#### Bibliografie
- Messika-Zeitoun, D., Mousavi, J., Pourmoazen, M., Cotte, F., Dreyfus, J., Nejjari, M., ... & Mesana, T. (2024). Computational simulation model of transcatheter edge-to-edge mitral valve repair: a proof-of-concept study. European Heart Journal-Cardiovascular Imaging, 25(10), 1415-1422. [link](https://pubmed.ncbi.nlm.nih.gov/38801398/)
- Thangtodoaraj, P. M., Benson, S. H., Oikonomou, E. K., Asselbergs, F. W., & Khera, R. (2024). Cardiovascular care with digital twin technology in the era of generative artificial intelligence. European Heart Journal, 45(45), 4808-4821. [link](https://academic.oup.com/eurheartj/article/45/45/4808/7775549)
- Corona, S., Godefroy, T., Tastet, O., Corbin, D., Modine, T., von Bardeleben, S., ... & Ben Ali, W. (2025). Towards standardizing mitral transcatheter edge-to-edge repair with deep-learning algorithm: a comprehensive multi-model strategy. Frontiers in Network Physiology, 5, 1701758.[link](https://www.frontiersin.org/journals/network-physiology/articles/10.3389/fnetp.2025.1701758/full)
- Messika-Zeitoun, D., Mousavi, J., Pourmoazen, M., Cotte, F., Dreyfus, J., Nejjari, M., ... & Mesana, T. (2024). Computational simulation model of transcatheter edge-to-edge mitral valve repair: a proof-of-concept study. European Heart Journal-Cardiovascular Imaging, 25(10), 1415-1422. [link](https://pubmed.ncbi.nlm.nih.gov/38801398/)
- Simonian, N., Vakamudi, S., Pirwitz, M., & Sacks, M. (2025). 72261| Development of a Mitral Valve Digital Twin for Transcatheter Edge-to-Edge Repair. Structural Heart, 9. [link](https://www.structuralheartjournal.org/article/S2474-8706%2825%2900152-6/fulltext)

</details>



## Project 6
<details>
    <summary>  ??? <img  style="vertical-align:middle" src="project-images\?.png" alt="networks" width="100"/> </summary>

### Title

#### Scop
...

#### Ideea de baza
...

#### Data
...

#### Bibliografie
...


</details>



