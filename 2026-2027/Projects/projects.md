
# Teme de proiect MIRPR 2026-2027

## Proiect 1

<details>
    <summary> Mai multe perspective, un singur diagnostic: AI pentru detectarea precoce a cancerului pulmonar  (owner: dl. dr. Andrei Roman) 
    <img src="project-images\lungCancer.jpeg" width="100">
    </summary>

### Identificarea cancerului de plaman

#### Scop
Dezvoltarea unui sistem inteligent care să ajute medicii în diagnosticarea timpurie a cancerului de plămân.

#### Ideea de baza
Deși cancerul pulmonar este recunoscut ca fiind cel mai mortal tip de cancer, un prognostic bun și un tratament eficient depind de detectarea timpurie a acestuia. Povara medicilor poate fi redusa cu ajutorul tehnicilor de AI care sunt esențiale în automatizarea diagnosticului și clasificării bolilor. De aceea, se dorește dezvoltarea unui sistem inteligent care să ajute medicii în diagnosticarea timpurie a cancerului de plămân. 

Se va urmari dezvoltarea unor modele inteligente capabile sa analizeze scanarile CT/PET si sa prezica diferiti biomarkeri tumorali folosind doar:
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

## Proiect 2
<details>
    <summary> AI pentru sănătatea femeilor: Identificarea cancerului de san  (owner: dl. dr. Andrei Roman) 
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




## Proiect 3
<details>
    <summary> Vocea care scrie: Automatizarea intocmirii fisei pacientului  (owner: dna. dr. Alina Baciu) 
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


## Proiect 4
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
- Manninger, M., Lercher, I., Hermans, A. N., Isaksen, J. L., Prassl, A. J., Zirlik, A., ... & Linz, D. (2025). Machine-learning guided differentiation between photoplethysmography waveforms of supraventricular and ventricular origin. Computer Methods and Programs in Biomedicine, 267, 108798. [link](https://pubmed.ncbi.nlm.nih.gov/40294456/)
</details>


## Proiect 5
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
- Manninger, M., Lercher, I., Hermans, A. N., Isaksen, J. L., Prassl, A. J., Zirlik, A., ... & Linz, D. (2025). Machine-learning guided differentiation between photoplethysmography waveforms of supraventricular and ventricular origin. Computer Methods and Programs in Biomedicine, 267, 108798. [link](https://pubmed.ncbi.nlm.nih.gov/40294456/)
</details>



## Proiect 6
<details>
    <summary>  AI pentru zâmbete: Identificarea tumorilor osoase maxofaciale (Owner: dna. dr. Mihaela Hedesiu) <img  style="vertical-align:middle" src="project-images\stoma1.jpg" alt="networks" width="100"/> 
    </summary>

### Development of an AI-Based Decision Support System for Automated Detection and Classification of Maxillofacial Bone Tumors on CBCT

#### Scop
Dezvoltarea unui sistem inteligent care să sprijine medicii stomatologi, radiologii și chirurgii oro-maxilo-faciali în detectarea, segmentarea și clasificarea automată a tumorilor osoase maxilo-faciale utilizând imagini CBCT (Cone Beam Computed Tomography).

#### Ideea de baza
Tumorile osoase ale regiunii maxilo-faciale reprezintă o provocare diagnostică importantă din cauza diversității morfologice și a asemănărilor dintre diferite leziuni benigne și maligne. Interpretarea imaginilor CBCT necesită expertiză ridicată și este consumatoare de timp, existând riscul unor variații între evaluatori. 
Proiectul urmărește dezvoltarea unui sistem bazat pe inteligență artificială care să analizeze volume CBCT și să ofere suport în procesul de diagnostic. Sistemul poate include mai multe componente: 
detectarea automată a regiunilor suspecte; 
segmentarea 2D/3D a tumorilor osoase; 
extragerea caracteristicilor radiomice și morfologice; 
clasificarea leziunilor în categorii precum benigne, agresive local sau maligne; 
generarea unor explicații vizuale (heatmaps, attention maps) pentru susținerea deciziei clinice.

Se vor investiga și compara metode bazate pe CNN-uri 3D, Vision Transformers și modele hibride CNN-Transformer. De asemenea, pot fi analizate tehnici de transfer learning, self-supervised learning, federated-learning și explainable AI pentru creșterea performanței și interpretabilității sistemului.

#### Data
- [DOLCHID](https://github.com/ZimoHZM/DOLCHID)
- [TCIA](https://github.com/google-deepmind/tcia-ct-scan-dataset)
- [dataset](https://academic.oup.com/dmfr/article/53/7/439/7700742#483529840)


#### Bibliografie
Chang H.J., Lee S.J., Yong T.H. et al. (2024). Deep learning-based detection and classification of jaw lesions on cone-beam CT images. Dentomaxillofacial Radiology [link](https://pmc.ncbi.nlm.nih.gov/articles/PMC12709009/).

Ariji Y., Fukuda M., Kise Y. et al. (2019). Automatic detection and classification of radiographic findings on panoramic and CBCT images using deep learning. Oral Radiology, 35, 313-321 [link](https://pubmed.ncbi.nlm.nih.gov/31320299/).

Chen J., Lu Y., Yu Q. et al. (2024). TransUNet: Transformers Make Strong Encoders for Medical Image Segmentation. IEEE Transactions on Medical Imaging.
Chen, J., Mei, J., Li, X., Lu, Y., Yu, Q., Wei, Q., ... & Zhou, Y. (2024). TransUNet: Rethinking the U-Net architecture design for medical image segmentation through the lens of transformers. Medical image analysis, 97, 103280 [link](https://www.sciencedirect.com/science/article/pii/S1361841524002056).


</details>


## Proiect 7
<details>
    <summary>  Identificarea leziunilor in dintii temporari si cei permanenti la copii(Owner: dna. dr. Mihaela Hedesiu) <img  style="vertical-align:middle" src="project-images\stoma2.jpg" alt="networks" width="100"/> 
    </summary>

### Identificarea leziunilor in dintii temporari si cei permanenti la copii

#### Scop

#### Ideea de baza

#### Data

#### Bibliografie



<!-- <details>
    <summary>  Simulator digital pentru practica dentara (Owner: dna. dr. Mihaela Hedesiu) <img  style="vertical-align:middle" src="project-images\stoma2.jpg" alt="networks" width="100"/> 
    </summary>

### AI-Driven Digital Simulator for Operational Optimization of Dental Practices

#### Scop
Dezvoltarea unui sistem stomatologic virtual care să permită simularea și optimizarea proceselor operaționale utilizând tehnici de inteligență artificială. Sistemul va sprijini managerii și medicii în luarea deciziilor privind programările, alocarea resurselor, utilizarea echipamentelor, gestionarea fluxului de pacienți și estimarea performanței cabinetului/clinice stomatologice. 

#### Ideea de baza
Clinicile stomatologice funcționează într-un mediu complex, în care performanța depinde simultan de factori clinici, operaționali și financiari. Probleme precum neprezentarea pacienților la programări (no-shows), timpii de așteptare, distribuția neuniformă a programărilor, utilizarea ineficientă a scaunelor dentare sau a personalului medical pot genera costuri semnificative și pierderi de venit. Studiile recente arată că modelele de Machine Learning pot prezice cu succes neprezentările și pot contribui la optimizarea programărilor. 
Proiectul urmărește construirea unui sistem inteligent care reproduce virtual activitatea unei clinici stomatologice și permite simularea diferitelor scenarii operaționale: 
estimarea fluxului zilnic de pacienți; 
predicția anulărilor și a neprezentărilor; 
optimizarea programărilor; 
optimizarea încărcării medicilor și a personalului auxiliar; 
analiza gradului de utilizare a echipamentelor; 
simularea impactului unor decizii manageriale asupra profitabilității;
identificarea factorilor care influențează costurile și veniturile.

Se pot investiga metode de: 
Machine Learning pentru predicție; 
Process Mining pentru modelarea proceselor; 
Discrete Event Simulation; 
Reinforcement Learning pentru optimizarea deciziilor; 
Explainable AI pentru justificarea recomandărilor oferite managerilor. 
Sistemul poate funcționa ca un instrument de tip "what-if analysis".

#### Data
- [dataset1](https://pmc.ncbi.nlm.nih.gov/articles/PMC9680883/#_ad93_) - Alabdulkarim, Y., Almukaynizi, M., Alameer, A., Makanati, B., Althumairy, R., & Almaslukh, A. (2022). Predicting no-shows for dental appointments. PeerJ Computer Science, 8, e1147.
- [dataset2](https://www.kaggle.com/datasets/joniarroba/noshowappointments)
- [dataset3](https://data.mendeley.com/datasets/wm6w2fvkfj/1)
- [MIMIC](https://physionet.org/content/mimiciv/)

#### Bibliografie

- Khashwayn, S., Bakhashwayn, M., & Alsubaie, A. (2026). Managing Dental Appointment No-Shows: A Systematic Review of Machine Learning Applications. International Dental Journal, 76(5), 109749 [link](https://pubmed.ncbi.nlm.nih.gov/42468354/)
- Cozmescu, A. F., Cernega, A., Didilescu, A. C., Imre, M. M., Dimitriu, B., & Pițuru, S. M. (2026). Administrative Perspectives on Digital Workflow Transformation and Artificial Intelligence Implementation in Dental Clinics. Dentistry Journal, 14(4), 206 [link](https://pubmed.ncbi.nlm.nih.gov/42041659/)
 -->

</details>



## Proiect 8
<details>
    <summary>  Diagram-as-Code AI Assistant  (Owner: Laura Cernau) <img  style="vertical-align:middle" src="project-images\dac.jpeg" alt="networks" width="100"/> 
    </summary>

### Diagram-as-Code AI Assistant 

#### Scop
Modern software architecture relies heavily on diagrams to communicate how a system is structured and how it fits into its environment. However, keeping documentation in sync with the code is often difficult and time-consuming. Generated diagrams also tend to stay at the code level (class diagrams, call graphs), which says little about the architecture itself. 

#### Ideea de baza
Design an AI-driven solution that generates architecture diagrams from natural language descriptions and/or source code, following the C4 model (Context, Containers, Components, Code). The focus should be on the architectural views: the system context, its containers (applications, services, databases, queues) and their components. Low-level views such as UML class diagrams should not be the main focus. The tool should support "diagram as code" approaches, generating structured diagram definitions rather than static images. 

Generate C4 views at the appropriate level of abstraction:  
- System Context: the system, its users and the external systems it interacts with 
- Container: deployable or runnable units and the communication between them (protocols, APIs, data stores) 
- Component: major building blocks inside a container and their responsibilities 
- Supplementary views where useful: dynamic (runtime flows) and deployment diagrams 

Generate diagrams from:  
- Plain text architecture descriptions 
- User stories 
- Code repositories, by identifying services, APIs, data stores, messaging and external dependencies, and abstracting them into C4 elements 
- Infrastructure-as-code (Terraform, Kubernetes manifests, docker-compose) as a source for container and deployment views 

Output diagrams in formats such as:  
- Structurizr DSL (preferred, since it is model-based and C4-native) 
- C4-PlantUML 
- Mermaid C4 diagrams 

Keep the views consistent: generate a single underlying model from which all C4 levels are derived, so the views don't contradict each other. 

**Advanced exploration (optional):** 
- Integrate the solution into a GitHub merge request workflow to:  
    - Automatically generate or update the C4 model when code changes 
    - Comment on merge requests with the impacted views, highlighting new or removed containers, components and relationships 
- Implement a Git hook that:  
    - Validates architectural consistency before allowing a commit, for example by flagging an undeclared dependency between containers or a component bypassing a defined interface 
    - Regenerates the affected views automatically when specific modules change 
- Compare diagram generation from static code analysis with LLM-based semantic interpretation, particularly in how well each one abstracts from code to the right C4 level. 
- Detect drift between the intended architecture (a hand-written C4 model) and the implemented architecture (one derived from code). 

#### Bibliografie
- Clemente, M., & Cândea, G. (2019). Software architecture documentation: A systematic mapping study. Journal of Systems and Software, 147, 124–147. [link](https://doi.org/10.1016/j.jss.2018.10.013)
- Devlin, J., Chang, M.‑W., Lee, K., & Toutanova, K. (2019). BERT: Pre‑training of deep bidirectional transformers for language understanding. Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics (NAACL‑HLT), 4171–4186. [link](https://doi.org/10.18653/v1/N19-1423)
- Jurafsky, D., & Martin, J. H. (2023). Speech and language processing (3rd ed., draft). Stanford University. [link](https://web.stanford.edu/~jurafsky/slp3/)
- Richards, M., & Ford, N. (2020). Fundamentals of software architecture. O’Reilly Media. 
- Reimers, N., & Gurevych, I. (2019). Sentence‑BERT: Sentence embeddings using Siamese BERT‑networks. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing. [link](https://arxiv.org/abs/1908.10084)

</details>

## Proiect 9
<details>
    <summary> Visual C4 Diagram Editor for VS Code with Company Modeling Rules (Owner: Laura Cernau, MARSH) <img  style="vertical-align:middle" src="project-images\c4-container.png" alt="networks" width="100"/> 
    </summary>

### Visual C4 Diagram Editor for VS Code with Company Modeling Rules 

#### Scop
Diagram-as-code formats such as Mermaid C4 are easy to version and review, but they are hard to write and read when diagrams grow: you can't see the result while editing the text, and adjusting the layout is tedious. Teams also tend to draw the same things differently. One person shows a third-party SaaS as an external system, another as a container, and internal systems end up with inconsistent naming, colors or boundaries. Without shared conventions, architecture diagrams across a company are hard to compare and trust. 

#### Ideea de baza
Develop a Visual Studio Code extension that provides a visual editor for Mermaid C4 diagrams, with two-way sync between the visual canvas and the underlying Mermaid code. The extension should include an assistant that helps users build diagrams according to a set of modeling rules defined by their company, for example how to represent internal systems, third-party systems, data stores or trust boundaries. 

Visual editing:  
- Render Mermaid C4 diagrams (Context, Container, Component, Dynamic, Deployment) in a VS Code webview 
- Add, edit, move and connect elements (Person, System, Container, Component, Boundary, Rel) from a palette 
- Two-way sync: changes on the canvas update the Mermaid code, and edits to the code refresh the canvas 
- Edit element properties (name, technology, description, tags) through a side panel 

Company modeling rules:  
- Define rules in a configuration file kept in the repository (e.g., .c4rules.yaml or JSON), such as:  
    - Internal systems use System, third-party systems use System_Ext with a "vendor" tag 
    - Every container must declare its technology 
    - Relationships must specify a protocol (HTTPS, gRPC, AMQP…) 
    - Naming conventions, mandatory boundaries, allowed element types per diagram level 
    - Styling conventions (colors and shapes per element category) 
- Validate diagrams against the rules and show violations as VS Code diagnostics (squiggles, Problems panel) with quick fixes 

Diagram assistant:  
- Suggest the correct element type when a user adds something (e.g., "Stripe" → external system per company rules) 
- Generate or extend a diagram from a natural language description while respecting the rules 
- Explain why a rule applies and how to fix a violation 

**Advanced exploration (optional):** 
- Share rules across teams through a central rule repository or a published rule package. 
- Provide a library of reusable, pre-approved elements (e.g., the company's identity provider or core platform services) that can be dragged into any diagram. 
- Use auto-layout algorithms (e.g., ELK, Dagre) and let users pin positions manually. 
- Run the same rule validation in CI so that merge requests with non-compliant diagrams are flagged. 
- Compare rule enforcement through deterministic validation with LLM-based guidance, especially for rules that are hard to formalise. 

#### Bibliografie


</details>



## Proiect 10
<details>
    <summary>  Clinical Trial Radar++: AI-Powered Recruitment Feasibility Prediction (Owner: Cristina Bogatean, Nagarro) <img  style="vertical-align:middle" src="project-images\clinicalTrial.png" alt="networks" width="100"/> 
    </summary>

### AI-Powered Recruitment Feasibility Prediction

#### Scop
Dezvoltarea unui sistem inteligent bazat pe inteligență artificială care să estimeze fezabilitatea unui studiu clinic încă din etapa de planificare, prin analizarea automată a informațiilor disponibile în registre publice de studii clinice. Sistemul va calcula indicatori precum durata estimată a recrutării, probabilitatea de atingere a țintei de înrolare și riscul de întârziere sau întrerupere a studiului, oferind totodată recomandări explicabile pentru optimizarea designului și a strategiei de recrutare.

#### Ideea de baza
Planificarea unui studiu clinic presupune numeroase decizii critice, precum alegerea țărilor și centrelor participante, definirea criteriilor de eligibilitate și estimarea numărului de pacienți care pot fi recrutați într-un interval de timp rezonabil. În practică, multe studii întâmpină dificultăți în recrutare, suferă întârzieri semnificative sau sunt chiar întrerupte prematur, generând costuri ridicate și întârzieri în dezvoltarea tratamentelor.

Clinical Trial Radar++ își propune să transforme datele istorice disponibile în registre publice precum ClinicalTrials.gov într-un instrument predictiv capabil să răspundă la întrebarea: 
„Poate acest studiu clinic să recruteze cu succes participanții necesari înainte de a fi lansat?” 
Pentru a răspunde acestei întrebări, sistemul va construi un set de date la scară largă pornind de la studii clinice finalizate sau în desfășurare și va extrage atât informații structurate (boală, fază, număr planificat de participanți, țări implicate, sponsor, tip de intervenție), cât și informații nestructurate provenite din descrierea protocolului, criteriile de includere și excludere sau endpoint-urile studiului.

Proiectul urmărește dezvoltarea unei arhitecturi hibride care combină modele Transformer pentru procesarea textului medical cu modele dedicate datelor tabulare și metadatelor studiului. Modelul rezultat va învăța relații complexe dintre caracteristicile protocolului și succesul recrutării, fiind capabil să prezică:
- durata estimată a recrutării;
- probabilitatea atingerii țintei de înrolare;
- riscul de întârziere sau de terminare prematură;
- gradul de dificultate al recrutării pentru diferite regiuni geografice.

Pe lângă componenta predictivă, sistemul va integra mecanisme de Explainable AI pentru a evidenția factorii care influențează estimările generate. Astfel, utilizatorii vor putea înțelege de ce un studiu este considerat riscant și vor primi recomandări concrete privind:
- selecția țărilor și a regiunilor cu potențial ridicat de recrutare;
- optimizarea strategiei de recrutare;
- simplificarea criteriilor de includere și excludere;
- reducerea factorilor care au contribuit istoric la întârzieri sau eșecuri de recrutare.

Rezultatul final va fi un instrument de suport decizional care combină analiza datelor istorice cu modele avansate de inteligență artificială pentru a ajuta sponsorii și organizațiile de cercetare clinică să proiecteze studii mai eficiente, cu risc redus și șanse mai mari de succes.

#### Bibliografie
Primary trial data
•	ClinicalTrials.gov API v2: https://clinicaltrials.gov/data-api/about-api
•	ClinicalTrials.gov bulk downloads: https://clinicaltrials.gov/data-download
•	AACT (SQL-ready ClinicalTrials dataset): https://aact.ctti-clinicaltrials.org/
•	AACT docs: https://aact.ctti-clinicaltrials.org/documentation
Additional trial registries (open portals / datasets)
•	EU Clinical Trials Register (public search): https://www.clinicaltrialsregister.eu/
•	ISRCTN registry (public search): https://www.isrctn.com/
Terminology + enrichment
•	MeSH: https://www.nlm.nih.gov/mesh/meshhome.html
•	MeSH downloads: https://www.nlm.nih.gov/databases/download/mesh.html
•	PubMed E-utilities: https://www.ncbi.nlm.nih.gov/books/NBK25501/
•	OpenAlex: https://openalex.org/
•	NIH RePORTER: https://api.reporter.nih.gov/
Optional feasibility proxies
•	WHO GHO: https://www.who.int/data/gho
•	World Bank: https://data.worldbank.org



</details>

## Proiect 11
<details>
    <summary>  Pharmacovigilance Signal Triage Copilot (Owner: Cristina Bogatean, Nagarro) <img  style="vertical-align:middle" src="project-images\pharmacovigilance.jpeg" alt="networks" width="100"/> 
    </summary>

### Pharmacovigilance Signal Triage Copilot

#### Scop
Dezvoltarea unui sistem inteligent bazat pe inteligență artificială care să sprijine activitățile de farmacovigilență prin identificarea timpurie, prioritizarea și explicarea semnalelor potențiale de siguranță asociate medicamentelor. Sistemul va analiza automat volume mari de rapoarte privind reacțiile adverse, va estima relevanța și riscul fiecărui semnal și va genera evidențe sintetizate și explicabile pentru a accelera procesul de evaluare realizat de experții în siguranță medicamentoasă.

#### Ideea de baza
Siguranța medicamentelor reprezintă o componentă esențială a sistemelor moderne de sănătate. După autorizarea unui medicament, informații noi despre reacțiile adverse pot apărea în urma utilizării sale pe scară largă, în populații diverse și în condiții reale de practică medicală. Din acest motiv, autoritățile de reglementare și companiile farmaceutice colectează permanent rapoarte privind reacțiile adverse provenite de la profesioniști din domeniul sănătății, pacienți și alte surse.

În practică, volumul acestor date este foarte mare și continuă să crească. Rapoartele conțin frecvent informații incomplete, folosesc denumiri diferite pentru același medicament sau aceeași reacție adversă și pot include cazuri duplicate sau dificil de interpretat. În consecință, experții în farmacovigilență petrec un timp considerabil pentru curățarea datelor, identificarea semnalelor relevante și compilarea documentației necesare investigațiilor ulterioare.

Pharmacovigilance Signal Triage Copilot își propune să funcționeze ca un asistent inteligent pentru procesul de triaj al semnalelor de siguranță, răspunzând la întrebarea: 
„Care sunt semnalele medicament–eveniment care necesită atenție imediată și de ce?” 
Sistemul va integra tehnici moderne de procesare a limbajului natural, analiză statistică și învățare automată pentru a transforma rapoartele brute într-o listă prioritizată de semnale. Procesul va include normalizarea denumirilor medicamentelor și a reacțiilor adverse, identificarea și eliminarea cazurilor duplicate, extragerea informațiilor relevante din descrieri textuale și calcularea unor indicatori standard utilizați în farmacovigilență.

O direcție avansată a proiectului este dezvoltarea unui model AI capabil să învețe din istoricul semnalelor investigate anterior și să estimeze probabilitatea ca un nou semnal să fie relevant din punct de vedere clinic și regulator. Astfel, în locul unei simple liste bazate pe reguli fixe, sistemul poate genera un scor inteligent de prioritate, care combină frecvența raportărilor, severitatea evenimentelor, evoluția în timp și asemănările cu semnale deja confirmate.

Pentru fiecare semnal identificat, sistemul va genera automat un Signal Packet, care include:
- descrierea semnalului și contextul său;
- evoluția temporală a raportărilor;
- indicatori statistici relevanți;
- exemple reprezentative de cazuri;
- explicații generate automat privind motivele prioritizării;
- recomandări pentru investigații suplimentare.

Prin integrarea tehnicilor de Explainable AI, utilizatorii vor putea înțelege factorii care au contribuit la clasificarea și prioritizarea unui semnal, sporind încrederea în recomandările sistemului. 
Rezultatul final va fi un instrument de suport decizional care reduce semnificativ timpul necesar procesului de triaj, crește șansele de detectare timpurie a problemelor de siguranță și permite experților să se concentreze asupra investigațiilor cu impact clinic ridicat, în loc să analizeze manual volume foarte mari de rapoarte neorganizate.

#### Bibliografie
Primary PV data
•	openFDA FAERS API: https://open.fda.gov/apis/drug/event/
•	FAERS background: https://www.fda.gov/drugs/questions-and-answers-fdas-adverse-event-reporting-system-faers/fda-adverse-event-reporting-system-faers-public-dashboard
Drug normalization + open drug data
•	RxNorm: https://lhncbc.nlm.nih.gov/RxNorm/
•	DrugCentral (open drug database): https://drugcentral.org/
•	ChEMBL (bioactivity + compounds): https://www.ebi.ac.uk/chembl/
•	Open Targets (target-disease associations): https://platform.opentargets.org/

Optional safety-related sources
•	FDA Recalls (open): https://open.fda.gov/apis/food/enforcement/  (useful pattern for “alerts/recalls” style)
•	PubMed E-utilities (literature): https://www.ncbi.nlm.nih.gov/books/NBK25501/

</details>


## Proiect 12
<details>
    <summary> AI pentru Terapii Personalizate (Owner Dr. Alexandra Pusta ) <img  style="vertical-align:middle" src="project-images\farma.jpg" alt="networks" width="100"/> 
    </summary>

### Sistem Inteligent pentru Detectarea și Cuantificarea Carboplatinei din Date Electrochimice

#### Scop
Dezvoltarea unui sistem inteligent care combină senzori electrochimici și modele avansate de AI/ML pentru detectarea, cuantificarea și monitorizarea carboplatinei în probe farmaceutice și sisteme de livrare controlată a medicamentelor. Sistemul va analiza automat semnale electrochimice (voltamograme, curbe curent-potențial etc.) și va estima concentrația medicamentului, oferind o alternativă rapidă, sensibilă și automatizată la metodele convenționale de analiză. 

#### Ideea de baza
Carboplatina este unul dintre cele mai utilizate medicamente chimioterapice pentru tratamentul mai multor tipuri de cancer. Pentru a reduce efectele adverse și pentru a crește eficiența terapeutică, aceasta este frecvent încapsulată în sisteme moderne de livrare, precum lipozomi sau nanosisteme. În astfel de aplicații este esențială monitorizarea precisă a proceselor de încărcare și eliberare a medicamentului, ceea ce necesită metode analitice rapide, sensibile și robuste. Cercetări recente au demonstrat că senzorii electrochimici bazați pe electrozi screen-printed permit detectarea eficientă a carboplatinei și pot fi utilizați pentru monitorizarea proceselor de eliberare din nanosisteme farmaceutice.

Proiectul își propune să adauge o componentă de iAI/ML peste infrastructura clasică de detecție electrochimică. În locul utilizării exclusive a metodelor de procesare și interpretare tradiționale, sistemul va învăța direct din semnalele electrochimice generate de senzori. Mai concret, se vor colecta sau genera seturi de date formate din:
voltamograme și curbe electrochimice asociate diferitelor concentrații de carboplatină; 
parametri experimentali ai măsurătorilor; 
date privind încărcarea și eliberarea carboplatinei din nanosisteme; 
eventual date provenite de la senzori diferiți sau din condiții experimentale variate. 
Pe baza acestor informații se vor dezvolta și compara modele de AI/ML capabile să estimeze concentrația carboplatinei direct din semnalul electrochimic. 
O direcție avansată a proiectului constă în dezvoltarea unei arhitecturi originale pentru analiza datelor electrochimice, de exemplu:
CNN-uri 1D pentru procesarea curbelor voltametrice; 
Vision Transformers aplicate reprezentărilor grafice ale semnalelor;
modele hibride CNN + Transformer; 
autoencodere pentru învățarea automată a reprezentărilor semnalelor electrochimice.

#### Bibliografie
- Pusta, A., Tertis, M., Ardusadan, C., Mirel, S., & Cristea, C. (2024). Electrochemical Sensing Device for Carboplatin Monitoring in Proof-of-Concept Drug Delivery Nanosystems. Nanomaterials, 14(9), 793 [link](https://www.mdpi.com/2079-4991/14/9/793)
- Qureshi, A., Shah, A., Iftikhar, F. J., Haleem, A., & Zia, M. A. (2024). Electrochemical analysis of anticancer and antibiotic drugs in water and biological specimens. RSC advances, 14(49), 36633-36655.
- Bocan, A., Siavash Moakhar, R., del Real Mata, C., Petkun, M., De Iure‐Grimmel, T., Yedire, S. G., ... & Mahshid, S. (2025). Machine‐learning‐aided advanced electrochemical biosensors. Advanced Materials, 37(33), 2417520 [link](https://advanced.onlinelibrary.wiley.com/doi/pdf/10.1002/adma.202417520).
</details>


##Project 13 
<details>
    <summary> LLM Security Guardian: OWASP Top 10 for LLM Applications Checker (Owner: Laura Cernau, Marsh) <img  style="vertical-align:middle" src="project-images\?.jpg" alt="networks" width="100"/> 
    </summary>

### Sistem Inteligent pentru Detectarea și Cuantificarea Carboplatinei din Date Electrochimice

#### Scop 
More and more applications embed large language models through chatbots, RAG pipelines, agents and copilots. These integrations add new kinds of vulnerabilities that traditional static analysis tools don't detect, such as prompt injection, leaked system prompts and over-privileged agents. The OWASP Top 10 for LLM Applications catalogues these risks, but checking a codebase against it is still largely manual. 

#### Ideea de baza
Design an AI-driven solution that analyses a code repository and reports whether it follows the OWASP Top 10 for LLM Applications. For each violation or weakness, it should give the file and line, an explanation, the severity, and a suggested fix. 
Detect risks such as:  
- Prompt injection: user input concatenated into prompts without separation or sanitisation 
- Sensitive information disclosure: secrets, PII or internal data sent to the model or returned in responses 
- Supply chain: unpinned or unverified models, plugins and dependencies 
- Improper output handling: LLM output passed directly to eval, SQL, shell commands or HTML rendering 
- Excessive agency: agents with broad tool permissions, write or delete access, or no human approval step 
- System prompt leakage: credentials or business logic embedded in system prompts 
- Vector and embedding weaknesses: RAG stores without access control or tenant isolation 
- Unbounded consumption: missing rate limits, token caps or timeouts 

Support several common stacks, for example:  
- Python (LangChain, LlamaIndex, OpenAI or Anthropic SDKs) 
- TypeScript or Node.js (Vercel AI SDK, LangChain.js) 

Produce output as:  
- A structured report (SARIF, JSON or Markdown) 
- A compliance scorecard per OWASP category 

Advanced exploration: 
- Integrate the checker into a GitHub merge request workflow to:  
    - Scan only the changed code and comment inline on risky lines 
    - Block merges when critical findings are present 
- Generate remediation patches automatically, such as input guards, output encoding or permission scoping. 
- Build a small deliberately vulnerable LLM app as a benchmark and measure detection rates. 
- Compare rule-based detection (Semgrep or CodeQL rules) with LLM-based semantic analysis, and with a hybrid of the two. 
- Add dynamic testing: generate adversarial prompts against the running app to confirm whether static findings can actually be exploited. 

#### Bibliografy
- Fourati, L. C., Awad, M., Ben Ali, M., & Jaafar, W. (2026). Large language models for cyberattack defense: a critical survey: L. Fourati et al. Knowledge and Information Systems, 68(1), 113 [link](https://dl.acm.org/doi/10.1007/s10115-026-02736-y).
- Wang, X., Huang, K., Liang, B., Li, H., & Du, X. (2026, March). Shadows in the Code: Exploring the Risks and Defenses of LLM-based Multi-Agent Software Development Systems. In Proceedings of the AAAI Conference on Artificial Intelligence (Vol. 40, No. 44, pp. 37970-37978) [link](https://dl.acm.org/doi/10.1609/aaai.v40i44.41134).
</details>

