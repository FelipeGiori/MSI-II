#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

# Divide dataset
vid_dataset = pd.read_csv("vid_dataset_re.csv", names=['path', 'label'])

#Divides the dataset into chucks of 100 rows
CHUNK_SIZE = 100
list_vid_dataset = [vid_dataset[i:i+CHUNK_SIZE] for i in range(0, len(vid_dataset), CHUNK_SIZE)]

os.system("mkdir tmp_vid_dataset")
os.system("mkdir vid_output")

for i, df in enumerate(list_vid_dataset):
    df.to_csv("tmp_vid_dataset/vid_dataset_" + str(i) + ".csv", header=False, index=False)
    os.system("python extract_tfrecords_main.py --input_videos_csv tmp_vid_dataset/vid_dataset_" + str(i) + ".csv \
    --output_tfrecords_file vid_output/output_" + str(i) + ".tfrecord")
    print("CHUNK %i of %i: DONE" %(i, len(list_vid_dataset)-1))
    

os.system("rm -rf tmp_vid_dataset")