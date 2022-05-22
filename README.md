# R2SN_construction
R2SNs provide a novel, reliable and biologically plausible method to understand human morphological covariance based on sMRI.
## Acknowledgement
Author: ***Fan Yang (2669742207@qq.com),Kun Zhao (kunzhao@buaa.edu.cn)***

Any questions, pls do not hesitate to contact kunzhao@buaa.edu.cn

The registeration section is based on ANTs toolkit.
## Source
If you used R2SN_code, please refer this orignal paper.
[Original Paper](https://direct.mit.edu/netn/article/5/3/783/101835/Regional-radiomics-similarity-networks-R2SNs-in)

## Installation
This package can support two systems, you can choose the system followed your computer as "system==Windows" or "system==linux". Here, if you choose ***"system==Windows"*** , you should download the [ANTs windows](https://github.com/ANTsX/ANTs/releases). Otherwise, the [ANTspy](https://github.com/ANTsX/ANTsPy) code is needed if you choose ***"system=linux"***. The author suggest the ubuntu revison first.

There are two ways to install the R2SN_code.

***First way: pip install git+https://github.com/slaughterfan/R2SN_construction."*** 

***Second way: pip install R2SN==1.0.4***

## Example
from R2SN import feature_extraction  

if __name__ == '__main__':  

    Image_path = r'D:\Python_project\venv\Brain\R2SN\R2SN\data\Image' #input image path  
    Network_output_path = r'D:\Python_project\venv\Brain\R2SN\R2SN\data\Network' #output network path  
    feature_extraction.R2SN_feature_extract(Image_path = Image_path,  
                                            Network_output_path = Network_output_path,  
                                            system = 'Windows', #Linux  
                                            n_jobs = 1)  

## Note
You may meet some errors in using this package, like...

***1.*** 
