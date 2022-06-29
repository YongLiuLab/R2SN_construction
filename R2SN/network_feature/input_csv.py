import os
import csv
import re
import nibabel as nib
import numpy as np
from .name_sort import sort_humanly

def make_csv(Img_path, Img_file, Mask_path, num_atlas, csv_folder):
    #make input csv
    # Mask = nib.load(Mask_path)
    # Mask_data = Mask.get_fdata()
    # num_atlas = len(np.unique(Mask_data)) - 1
    csv_name = Img_file.split('.')[0] + '.csv'
    csv_path = os.path.join(csv_folder,csv_name)
    if os.path.exists(csv_path):
        os.remove(csv_path)
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Image', 'Mask', 'Label'])
        for j in range(num_atlas):
            Image_file = os.path.join(Img_path, Img_file)
            Mask_file = Mask_path
            Label = j + 1
            writer.writerow([Image_file, Mask_file,Label])
    csvfile.close()
    return csv_name







