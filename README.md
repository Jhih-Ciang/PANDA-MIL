# PANDA-MIL

## Introduction

The Prostate cANcer graDe Assessment [(PANDA)](https://www.kaggle.com/c/prostate-cancer-grade-assessment) challenge comprises over 10K whole-slide images (WSIs) of digitized hematoxylin and eosin-stained biopsies originating from Radboud University Medical Center and Karolinska Institute. PANDA-MIL collects the eosin-stained biopsies with region-based masks from Karolinska Institute, indicating the benign (normal) and cancerous (abnormal) tissue, combined by stroma and epithelium. To fit the MIL-based task, we non-overlapped partition each WSI with the highest-level resolution into patches and only keep those patches comprising tissue over the 50% patch size. Each kept patch gets its patch-level annotations from PANDA, and a WSI comprising any abnormal patch is treated as an abnormal WSI. In sum, PANDA-MIL's training split contains 3925 instances of WSI-level annotations, and the testing split includes 975 instances of patch-level annotations.
