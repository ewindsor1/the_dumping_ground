#!/usr/bin/env python
# coding: utf-8

import logging

#logger = logging.getLogger(__name__)
#
#while len(logger.handlers):
#    logger.removeHandler(logger.handlers[0])
#
#logging.basicConfig(filename = "minicar_randomforest_deploy.log", 
#                    format='%(asctime)s %(levelname)s:%(message)s', 
#                    level=logging.INFO, 
#                    datefmt='%I:%M:%S')
#logger = logging.getLogger()        # root logger
#open('minicar_randomforest_deploy.log', 'w').close()

import boto3
import collections as col
import datetime
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import os
import glob
from sklearn.ensemble import RandomForestClassifier
import pickle
import sagemaker.amazon.common as smac
import s3fs

#logging.info("Setup successful logger attempt")

df = pd.read_csv('s3://emma-eu-west-2/testdata/formattedSmallTestData.csv', sep='\t')


#ids = df['REGISTRATION_ID']


print("EMMA1")


with open('accenture_randomforest_2018-10-25_08:54.pkl', 'rb') as pickle_file:
    rf_clf = pickle.load(pickle_file)

print ("test pred output")

y_pred_whole_pop = rf_clf.predict(df)
y_prob_whole_pop = rf_clf.predict_proba(df)[:,1]

d = col.OrderedDict()
#d['REGISTRATION_ID'] = ids.values
d['propensity'] = y_prob_whole_pop
d['prediction'] = y_pred_whole_pop
d['RUN_DT'] = pd.to_datetime('today')

predictions = pd.DataFrame(d)

## save the predictions to disk
s3 = boto3.client('s3')
bucket = 'emma-eu-west-2'
now = datetime.datetime.now()
filename = 'test_predictions_{date}.csv'.format(date=now.strftime("%Y-%m-%d_%H:%M"))
predictions.to_csv(filename)
s3.upload_file(filename, bucket, 'testdata/{}'.format(filename))
