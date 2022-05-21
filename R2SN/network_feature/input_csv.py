import os
import csv
import re
from .name_sort import sort_humanly

def make_csv(Img_path, Img_file, Mask_path, csv_folder):
    #make input csv
    Mask_list = sort_humanly(os.listdir(Mask_path))
    csv_name = Img_file.split('.')[0] + '.csv'
    csv_path = os.path.join(csv_folder,csv_name)
    if os.path.exists(csv_path):
        os.remove(csv_path)
    with open(csv_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Image', 'Mask'])
        for j in range(0, len(Mask_list)):
            Image_file = os.path.join(Img_path, Img_file)
            Mask_file = os.path.join(Mask_path,Mask_list[j])
            writer.writerow([Image_file, Mask_file])
    csvfile.close()
    return csv_name







