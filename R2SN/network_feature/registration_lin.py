import ants
import numpy as np
import os

def registration(image_path, target_path, output_path):
    source_img = ants.image_read(image_path)
    target_image = ants.image_read(target_path)
    # source_img_nib = nib.load(os.path.join(Image_path, Image_list[i]))
    source_img = ants.denoise_image(source_img, ants.get_mask(source_img))
    source_img_n4 = ants.n4_bias_field_correction(source_img)
    output = ants.registration(target_image, source_img_n4, type_of_transform='SyN')['warpedmovout']
    image_data = output.numpy()
    image_data_flatten = np.sort(image_data.flatten())
    max_95 = int(len(image_data_flatten) * 0.95)
    data_255 = image_data / image_data_flatten[max_95] * 255


    output_img = ants.from_numpy(data_255, target_image.origin, target_image.spacing, target_image.direction)
    image_name = os.path.split(image_path)[1]
    if image_name.endswith(".nii.gz"):
        output_file = 'normalize_255_' + image_name
    else:
        output_file = 'normalize_255_' + image_name + '.gz'

    output_img.to_file(os.path.join(output_path, output_file))

    return output_file