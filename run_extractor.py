#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


path = "/tf/youtube-8m/feature_extractor/vid_output"
files = []

for r, d, f in os.walk(path):
    for file in f:
        if ".tfrecord" in file:
            files.append(os.path.join(r, file))
          
            

for f in files:
    #print('python inference.py --train_dir "model" --output_file="' + f.split("/")[5] + '.csv" --input_data_pattern="' + f + '" --batch_size 100 --sample_all')
    os.system('python inference.py --train_dir "model" --output_file="' + f.split("/")[5] + '.csv" --input_data_pattern="' + f + '" --batch_size 100 --sample_all')
    print(f.split("/")[5])