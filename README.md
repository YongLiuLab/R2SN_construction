# R2SN_construction
R2SNs provide a novel, reliable and biologically plausible method to understand human morphological covariance based on sMRI.
## Acknowledgement
Author: ***Fan Yang (2669742207@qq.com),Kun Zhao (kunzhao@buaa.edu.cn)***

Any questions, pls do not hesitate to contact kunzhao@buaa.edu.cn

The registeration section is based on ANTs toolkit.
## Requirment

Python>=3.8

## Source
If you used R2SN_code, please refer this orignal paper.
[Original Paper](https://direct.mit.edu/netn/article/5/3/783/101835/Regional-radiomics-similarity-networks-R2SNs-in)

Zhao K, Zheng Q, Che T, et al. Regional radiomics similarity networks (R2SNs) in the human brain: Reproducibility, small-world properties and a biological basis [J]. Network Neuroscience, 2021, 1-15.

## Installation
This package can support two systems, you can choose the system followed your computer as "system==Windows" or "system==linux". Here, if you choose ***"system==Windows"*** , you should download the [ANTs windows](https://github.com/ANTsX/ANTs/releases). Otherwise, the [ANTspy](https://github.com/ANTsX/ANTsPy) code is needed if you choose ***"system=linux"***. The author suggest the ubuntu revison first.

There are two ways to install the R2SN_code.

***First way: pip install git+https://github.com/YongLiuLab/R2SN_construction."*** or you also can download this package and ***cd the workdir to ../R2SN_construction*** and then ***“pip install .”*** 

***Second way: pip install R2SN==1.0.4***

## Example
from R2SN import feature_extraction  


Image_path = r'D:\Python_project\venv\Brain\R2SN\R2SN\data\Image' #input image path  
Network_output_path = r'D:\Python_project\venv\Brain\R2SN\R2SN\data\Network' #output network path  
feature_extraction.R2SN_feature_extract(Image_path = Image_path,  
                                            Network_output_path = Network_output_path,  
                                            system = 'Windows', #Linux  
                                            n_jobs = 1)  

## Note
Here, the image_path is the ***dir*** of your original file. The Network_out_path is the ***dir*** of your choosed ouput dir. Moreover, the system="Windows" or system="Linunx". n_jobs is means how much works runing at the same time, maybe you can use n_jobs=4 in your PC and n_jobs=8 in your more power computer.

Following aspects should be noted in your study

***1.*** We suggest that you can run this package in python>=3.8. else, maybe the requirment should be changed when installing R2SN packcage, such as change the "scipy==1.6.2" to "scipy>=1.5.4". But maybe some error would appear.
