from .network_feature.network import network
import os
import platform
from os.path import dirname


file_path = os.path.abspath(dirname(__file__))
system = platform.system()

def R2SN_feature_extract(Image_path,#Image input path
                        Network_output_path,#Network output path
                        Mask_path = os.path.join(file_path,'data','rBN_Atlas_246_1mm.nii'),
                        Target_path = os.path.join(file_path,'data','MNI152_T1_1mm.nii'),
                        params_path = os.path.join(file_path,'network_feature','Params.yaml'),
                        picked_feature_path = os.path.join(file_path,'network_feature','picked_features.txt'),
                        Image_output_path = None,
                        radiomics_output_path = None,
                        n_jobs = 1):
        network(Image_path = Image_path,
                Target_path = Target_path,
                Mask_path = Mask_path,
                Network_output_path = Network_output_path,
                params_path = params_path,
                picked_feature_path = picked_feature_path,
                Image_output_path = Image_output_path,
                radiomics_output_path = radiomics_output_path,
                system = system,
                n_jobs = n_jobs)

# if __name__ == '__main__':
#     R2SN_feature_extract(r'\data\Image',
#                          r'\data\Network',)
