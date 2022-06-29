#!/usr/bin/env python

from __future__ import print_function

import collections
import csv
import logging
import os
import warnings
import SimpleITK as sitk

import radiomics
from radiomics import featureextractor

def feature_extract(csv_path, params_path, radiomics_ouput_path):
  warnings.filterwarnings('ignore')
  outputFilepath = os.path.join(radiomics_ouput_path, (os.path.split(csv_path)[-1]).split('.')[0] + '_radiomics_features' + '.csv')
  # progress_filename =  os.path.join(radiomics_ouput_path, (os.path.split(csv_path)[-1]).split('.')[0] + '_log.txt')
  if os.path.exists(outputFilepath):
    os.remove(outputFilepath)
  # if os.path.exists(progress_filename):
  #   os.remove(progress_filename)
  # params = os.path.join(outPath, 'exampleSettings', 'Params.yaml')
  # params = ''
  # Configure logging

  rLogger = logging.getLogger('radiomics')

  # Set logging level
  # rLogger.setLevel(logging.INFO)  # Not needed, default log level of logger is INFO

  # Create handler for writing to log file
  # handler = logging.FileHandler(filename=progress_filename, mode='a')
  # handler.setFormatter(logging.Formatter('%(levelname)s:%(name)s: %(message)s'))
  # rLogger.addHandler(handler)

  # Initialize logging for batch log messages
  logger = rLogger.getChild('batch')

  # Set verbosity level for output to stderr (default level = WARNING)
  radiomics.setVerbosity(logging.INFO)
  # radiomics.setVerbosity(level=20)

  logger.info('pyradiomics version: %s', radiomics.__version__)
  logger.info('Loading CSV')

  flists = []
  try:
    with open(csv_path, 'r') as inFile:
      cr = csv.DictReader(inFile, lineterminator='\n')
      flists = [row for row in cr]
  except Exception:
    logger.error('CSV READ FAILED', exc_info=True)

  logger.info('Loading Done')
  logger.info('Patients: %d', len(flists))
  # print('Loading Done')
  # print('Patients: %d', len(flists))

  if os.path.isfile(params_path):
    extractor = featureextractor.RadiomicsFeatureExtractor(params_path)
  else:  # Parameter file not found, use hardcoded settings instead
    settings = {}
    settings['binWidth'] = 25
    settings['resampledPixelSpacing'] = None  # [3,3,3]
    settings['interpolator'] = sitk.sitkBSpline
    settings['enableCExtensions'] = True

    extractor = featureextractor.RadiomicsFeatureExtractor(**settings)
    # extractor.enableInputImages(wavelet= {'level': 2})

  # logger.info('Enabled input images types: %s', extractor.enabledImagetypes)
  # logger.info('Enabled features: %s', extractor.enabledFeatures)
  # logger.info('Current settings: %s', extractor.settings)

  headers = None

  for idx, entry in enumerate(flists, start=1):

    # logger.info("(%d/%d) Processing Patient (Image: %s, Mask: %s)", idx, len(flists), entry['Image'], entry['Mask'])
    print("({num1}/{num2}) Processing Patient (Image: {str1}, Mask: {str2}, Label: {str3})".format(num1 = idx, num2 = len(flists),
                                                                                    str1 = entry['Image'],
                                                                                    str2 = entry['Mask'] ,
                                                                                    str3 = entry['Label']))
    imageFilepath = entry['Image']
    maskFilepath = entry['Mask']
    label = entry['Label']

    if str(label).isdigit():
      label = int(label)
    else:
      label = None

    if (imageFilepath is not None) and (maskFilepath is not None) and (label is not None):
      featureVector = collections.OrderedDict(entry)
      featureVector['Image'] = os.path.basename(imageFilepath)
      featureVector['Mask'] = os.path.basename(maskFilepath)

      try:
        featureVector.update(extractor.execute(imageFilepath, maskFilepath, label))

        with open(outputFilepath, 'a') as outputFile:
          writer = csv.writer(outputFile, lineterminator='\n')
          if headers is None:
            headers = list(featureVector.keys())
            writer.writerow(headers)

          row = []
          for h in headers:
            row.append(featureVector.get(h, "N/A"))
          writer.writerow(row)
      except Exception:
        logger.error('FEATURE EXTRACTION FAILED', exc_info=True)

  # handler.close()
  # os.remove(progress_filename)

  return os.path.split(outputFilepath)[1]