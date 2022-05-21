import pandas as pd
import numpy as np
import os
from scipy.stats import pearsonr
from datetime import datetime

#radiomics to network
def network_compute(feature_csv,file_name,output_path, picked_feature_path, csv_folder):
    f = open(picked_feature_path, 'r')
    picked_feature = eval(f.read())
    f.close()
    data = pd.read_csv(os.path.join(csv_folder,feature_csv),sep=',',usecols=picked_feature)
    # data.to_csv(os.path.splitext(feature_csv)[0] + '_input_feature.csv')
    feature = data.values
    normalize_featrue = (feature - feature.min(axis = 0))/(feature.max(axis = 0) - feature.min(axis = 0))
    num_region = feature.shape[0]
    network = np.zeros([num_region,num_region])
    for i in range(num_region):
        for j in range(i,num_region):
            network[i,j] = pearsonr(normalize_featrue[i,:],normalize_featrue[j,:])[0]
    for i in range(1,num_region):
        for j in range(0,i):
            network[i,j] = network[j,i]
    np.save(os.path.join(output_path, file_name.split('.')[0] + '_network.npy'),network)