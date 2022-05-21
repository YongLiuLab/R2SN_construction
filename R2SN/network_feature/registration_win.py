import nibabel as nib
import numpy as np
import os
import time
import SimpleITK as sitk
from os.path import dirname

def registration(image_path, target_path, output_path):
    current_path = os.getcwd()
    os.chdir(os.path.abspath(dirname(__file__)))
    # os.chdir(os.path.join(current_path,'R2SN/network_feature'))

    image_file = (os.path.split(image_path)[1]).split('.')[0]
    n4_image_path = os.path.join(output_path,'n4_' + image_file + '.nii.gz')

    cmd_n4 = f"N4BiasFieldCorrection -d 3 -i {image_path} -o {n4_image_path}"
    os.system(cmd_n4)
    cmd_ANTS = f"ANTS 3 -m CC[{target_path}, {n4_image_path}, 1, 2] -t SyN[0.25] -r Gauss[3, 1.0] -o {os.path.join(output_path,image_file + '.nii.gz')} -i 40x20x10 --number-of-affine-iterations 100x100x100"
    os.system(cmd_ANTS)
    warp_dir1 = os.path.join(output_path, image_file + 'Warp.nii.gz')
    warp_dir2 = os.path.join(output_path, image_file + 'Affine.txt')
    warp_dir3 = os.path.join(output_path, image_file + 'InverseWarp.nii.gz')
    regist_img = os.path.join(output_path, 'regist_' + image_file + '.nii.gz')
    cmd_img = f"WarpImageMultiTransform 3 {n4_image_path} {regist_img} {warp_dir1} {warp_dir2} -R {target_path}"
    os.system(cmd_img)

    image = nib.load(regist_img)
    image_data = image.get_fdata()
    image_data_flatten = np.sort(image_data.flatten())
    max_95 = int(len(image_data_flatten) * 0.95)
    data_255 = image_data / image_data_flatten[max_95] * 255
    output_img = nib.Nifti1Image(data_255, image.affine, image.header)
    output_file = os.path.join(output_path, 'normalize_255_' + image_file + '.nii.gz')
    nib.save(output_img, output_file)
    os.chdir(current_path)

    os.remove(n4_image_path)
    os.remove(warp_dir1)
    os.remove(warp_dir2)
    os.remove(warp_dir3)
    os.remove(regist_img)

    return output_file