# R2SN_construction

! [image] (https://github.com/YongLiuLab/R2SN_construction/blob/main/IMG.jpg)

R2SNs provide a novel, reliable and biologically plausible method to understand human morphological covariance based on sMRI.


## Source
If you use R2SN_code, please cite this orignal paper: [Original Paper](https://direct.mit.edu/netn/article/5/3/783/101835/Regional-radiomics-similarity-networks-R2SNs-in)

Zhao K, Zheng Q, Che T, et al. Regional radiomics similarity networks (R2SNs) in the human brain: Reproducibility, small-world properties and a biological basis [J]. Network Neuroscience, 2021, 1-15.

## Installation
### Install option 1 (for installing the R2SN_construction code in a chosen directory): clone repository, install locally

1) [Clone this repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

2) Navigate to the main R2SN_construction directory , then run:

       pip install .

### Install option 2: direct install from Pypi

       pip install R2SN

## Dependencies
- Python >= 3.8
- [Nibabel >= 3.2.1](https://github.com/nipy/nibabel)
- [Pyradiomics >= 3.0.1](https://github.com/AIM-Harvard/pyradiomics)
- [Scipy >= 1.6.2](https://github.com/scipy/scipy)
- [SimpleITK >= 2.1.1.2](https://github.com/SimpleITK/SimpleITK)
- [NumPy >= 1.21.5](https://github.com/numpy/numpy)
- [Pandas >= 1.2.3](https://github.com/pandas-dev/pandas)
- [Sklearn](https://github.com/scikit-learn/scikit-learn)

## Example

```
from R2SN import feature_extraction  

if __name__ == '__main__':
	Image_path = r'D:\Python_project\venv\Brain\R2SN\R2SN\data\Image' 	       	# input image path  
	Network_output_path = r'D:\Python_project\venv\Brain\R2SN\R2SN\data\Network' 	# output network path  
	n_jobs = 1								# number of process
	feature_extraction.R2SN_feature_extract(Image_path = Image_path,  
                                           			Network_output_path = Network_output_path,  
                                            			n_jobs = n_jobs)  
```

## Note
Here, the image_path is the ***dir*** of your original file. The Network_out_path is the ***dir*** of your choosed ouput dir. n_jobs is means the number of jobs runing simultaneously.

## Acknowledgement
Author: ***Fan Yang (2669742207@qq.com),Kun Zhao (kunzhao@buaa.edu.cn)***

Any questions, pls do not hesitate to contact kunzhao@buaa.edu.cn

The registeration section is based on ANTs toolkit.



