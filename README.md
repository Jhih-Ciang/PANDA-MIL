# PANDA-MIL

## Introduction

The Prostate cANcer graDe Assessment [(PANDA)](https://www.kaggle.com/c/prostate-cancer-grade-assessment) challenge comprises over 10K whole-slide images (WSIs) of digitized hematoxylin and eosin-stained biopsies originating from Radboud University Medical Center and Karolinska Institute. PANDA-MIL collects the eosin-stained biopsies with region-based masks from Karolinska Institute, indicating the benign (normal) and cancerous (abnormal) tissue, combined by stroma and epithelium. To fit the MIL-based task, we non-overlapped partition each WSI with the highest-level resolution into patches and only keep those patches comprising tissue over the 50% patch size. Each kept patch gets its patch-level annotations from PANDA, and a WSI comprising any abnormal patch is treated as an abnormal WSI. In sum, PANDA-MIL's training split contains 3925 instances with WSI-level annotations, and the testing split includes 975 instances with patch-level annotations.

## Dataset

The PANDA-MIL can be found in this [link](https://drive.google.com/drive/folders/1UO8cIyhd7T6jyohDFmgMtGmVZTy82T_V?usp=sharing).

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

```
@article{bulten2022artificial,
  title={Artificial intelligence for diagnosis and Gleason grading of prostate cancer: the PANDA challenge},
  author={Bulten, Wouter and Kartasalo, Kimmo and Chen, Po-Hsuan Cameron and Str{\"o}m, Peter and Pinckaers, Hans and Nagpal, Kunal and Cai, Yuannan and Steiner, David F and van Boven, Hester and Vink, Robert and others},
  journal={Nature medicine},
  volume={28},
  number={1},
  pages={154--163},
  year={2022},
  publisher={Nature Publishing Group US New York}
}
```
