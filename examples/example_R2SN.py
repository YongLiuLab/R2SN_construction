from R2SN import feature_extraction
if __name__ == '__main__':
    Image_path = r'D:\Python_project\venv\Brain\R2SN\R2SN\data\Image' #input image path
    Network_output_path = r'D:\Python_project\venv\Brain\R2SN\R2SN\data\Network' #output network path
    feature_extraction.R2SN_feature_extract(Image_path = Image_path,
                                            Network_output_path = Network_output_path,
                                            system = 'Windows', #Linux
                                            n_jobs = 1)