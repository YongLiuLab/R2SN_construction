from __future__ import print_function
from .input_csv import make_csv
from .feature_extract_parallel import feature_extract_parallel
from .feature_extract import feature_extract
from .network_compute import network_compute
from .name_sort import sort_humanly
from multiprocessing import cpu_count, Pool
import time
import nibabel as nib
import numpy as np
import shutil
import os
import time


def network_per(args):
    Image_path, Image_file, Network_output_path, Target_path, \
    Image_output_path, Mask_path, temp_path, \
    params_path, radiomics_output_path, picked_feature_path, \
    Image_output, radiomics_output,system = args

    if system == 'Windows':
        from .registration_win import registration
    elif system == 'Linux':
        from .registration_lin import registration
    else:
        raise Exception(f"Error: System invalid")

    t0 = time.time()
    print(f'Image: {Image_file} registration start!')
    Image_regis = registration(os.path.join(Image_path, Image_file), Target_path,
                               Image_output_path)  # registration_file_name
    t1 = time.time()
    print(f'Image: {Image_file} preprocessing finished, cost time{t1 - t0}.')

    # Feature_extraction
    Input_csv = make_csv(Image_output_path, Image_regis, Mask_path, temp_path)  # csv_file_name
    t2 = time.time()
    print(f'Image: {Image_file} feature extraction start!')
    feature_extract_file = feature_extract(os.path.join(temp_path, Input_csv), params_path,
                                           radiomics_output_path)

    # # feature_extract_file = feature_extract_parallel(os.path.join(temp_path, Input_csv), params_path, radiomics_output_path)
    # feature_extract_file = r'D:\Python_project\venv\Brain\R2SN\R2SN\temp\normalize_255_ASL_001_radiomics_features.csv'
    t3 = time.time()
    print(f'Image: {Image_file} preprocessing finished, cost time{t3 - t2}.')

    # Network construction
    t4 = time.time()
    print(f'Image: {Image_file} network construction start!')
    network_compute(feature_extract_file, Image_file, Network_output_path, picked_feature_path, radiomics_output_path)
    t5 = time.time()
    print(f'Image: {Image_file} network construction finished, cost time{t5 - t4}.')
    print(f'Image: {Image_file} all finished, cost time{t5 - t0}.')

    os.remove(os.path.join(temp_path,Input_csv))

    if Image_output is False:
        os.remove(os.path.join(temp_path, Image_regis))

    if radiomics_output is False:
        os.remove(os.path.join(temp_path, feature_extract_file))



def network(Image_path,#xxx/xxx/
            Target_path,#xxx.nii
            Mask_path,#xxx/rBN_Atlas_246
            Network_output_path,#xxx/
            params_path = 'network_feature/Params.yaml',
            picked_feature_path = r'network_feature/picked_features.txt',
            Image_output_path = None,
            radiomics_output_path = None,
            system = 'Windows',
            n_jobs = 1):
    #path check
    # if system == 'Windows':
    #     from R2SN.network_feature.registration_win import registration
    # elif system == 'Linux':
    #     from R2SN.network_feature.registration_lin import registration
    # else:
    #     raise Exception(f"Error: System invalid")

    if not os.path.exists(Image_path):
        raise Exception(f"Error: Image_path invalid")

    if not os.path.exists(Target_path):
        raise Exception(f"Error: Target_path invalid")

    if not os.path.exists(Mask_path):
        raise Exception(f"Error: Mask_path invalid")

    if not os.path.exists(Network_output_path):
        raise Exception(f"Error: Network_output_path invalid")

    if not os.path.exists(picked_feature_path):
        raise Exception(f"Error: picked_feature_path invalid")

    #temp folder
    temp_path = os.path.join(os.getcwd(),'temp')
    radiomics_temp_path = os.path.join(os.getcwd(),'_TEMP')

    #delete temp folder
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)
    if os.path.exists(radiomics_temp_path):
        shutil.rmtree(radiomics_temp_path)

    if Image_output_path is None:
        Image_output = False
        Image_output_path = temp_path
    else:
        if not os.path.exists(Image_output_path):
            raise Exception(f"Error: Image_output_path invalid")

    if radiomics_output_path is None:
        radiomics_output = False
        radiomics_output_path = temp_path
    else:
        if not os.path.exists(radiomics_output_path):
            raise Exception(f"Error: radiomics_output_path invalid")


    if not os.path.exists(temp_path):
        os.mkdir(temp_path)

    Image_list = sort_humanly([f for f in os.listdir(Image_path) if '.nii' or '.nii.gz' in f])
    pool = Pool(n_jobs)
    pool.map(network_per, [(Image_path, f, Network_output_path,Target_path,
                            Image_output_path, Mask_path, temp_path,
                            params_path, radiomics_output_path, picked_feature_path,
                            Image_output, radiomics_output, system) for f in Image_list])
    shutil.rmtree(temp_path)

    # for i in range(len(Image_list)):
    #     #Preprocessing
    #     t0 = time.time()
    #     Image_file = Image_list[i]#image_file name
    #     print(f'Image{i}: {Image_file} registration start!')
    #     Image_regis = registration(os.path.join(Image_path, Image_file), Target_path, Image_output_path)#registration_file_name
    #     t1 = time.time()
    #     print(f'Image{i}: {Image_file} preprocessing finished, cost time{t1 - t0}.')
    #
    #     #Feature_extraction
    #     Input_csv = make_csv(Image_output_path, Image_regis, Mask_path, temp_path)#csv_file_name
    #     t2 = time.time()
    #     print(f'Image{i}: {Image_file} feature extraction start!')
    #     feature_extract_file = feature_extract(os.path.join(temp_path, Input_csv), params_path,
    #                                                     radiomics_output_path)
    #     # feature_extract_file = feature_extract_parallel(os.path.join(temp_path, Input_csv), params_path, radiomics_output_path)
    #     t3 = time.time()
    #     print(f'Image{i}: {Image_file} preprocessing finished, cost time{t3 - t2}.')
    #     feature_extract_file = r'D:\Python_project\venv\Brain\R2SN\R2SN\temp\normalize_255_ASL_001_radiomics_features.csv'
    #     #Network construction
    #     t4 = time.time()
    #     print(f'Image{i}: {Image_file} network construction start!')
    #     network_compute(feature_extract_file, Image_file, Network_output_path, picked_feature_path, radiomics_output_path)
    #     t5 = time.time()
    #     print(f'Image{i}: {Image_file} network construction finished, cost time{t5 - t4}.')
    #     print(f'Image{i}: {Image_file} all finished, cost time{t5 - t0}.')

        # os.remove(os.path.join(temp_path,Input_csv))
        #
        # if Image_output is False:
        #     os.remove(os.path.join(temp_path, Image_regis))
        #
        # if radiomics_output is False:
        #     os.remove(os.path.join(temp_path, feature_extract_file))

    # shutil.rmtree(temp_path)







