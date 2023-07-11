# PANDA-MIL

## Introduction

The Prostate cANcer graDe Assessment [(PANDA)](https://www.kaggle.com/c/prostate-cancer-grade-assessment) challenge comprises over 10K whole-slide images (WSIs) of digitized hematoxylin and eosin-stained biopsies originating from Radboud University Medical Center and Karolinska Institute. PANDA-MIL collects the eosin-stained biopsies with region-based masks from Karolinska Institute, indicating the benign (normal) and cancerous (abnormal) tissue, combined by stroma and epithelium. To fit the MIL-based task, we non-overlapped partition each WSI with the highest-level resolution into patches and only keep those patches comprising tissue over the 50% patch size. Each kept patch gets its patch-level annotations from PANDA, and a WSI comprising any abnormal patch is treated as an abnormal WSI. In sum, PANDA-MIL's training split contains 3925 instances with WSI-level annotations, and the testing split includes 975 instances with patch-level annotations.

[raw data](https://drive.google.com/file/d/1Rlc4Mydcd0nEi_icw2AJG_nJqIVQ55Ku/view?usp=sharing)

[extracted i3d features](https://drive.google.com/drive/folders/1TWmtx7puXsXvFLmvqweq7n8H2S6_yks5?usp=sharing)



## Citation
We hope the codebase is beneficial to you. If this repo works positively for your research, please consider citing our paper. Thank you for your time and consideration.
```
@inproceedings{wu2023Contrastive,
  author    = {Jhih-Ciang Wu, Ding-Jie Chen and Chiou-Shann Fuh},
  title     = {Contrastive Feature Decoupling for Weakly-supervised Disease Detection},
  booktitle = {MICCAL},
  year      = {2023},
}
```
