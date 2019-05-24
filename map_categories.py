#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import os

def map_cat(output, labels):
    data = []
    for i, row in output.iterrows():
        videoId = str(row.VideoId).split("/")[2].split(".")[0]
        
        labels_pairs = row.LabelConfidencePairs.split()
        tmp = zip(labels_pairs[::2], labels_pairs[1::2])
        
        labels_data = []
        for e in tmp:
            labels_data.append((labels[int(e[0])], e[1]))
            
        data.append([videoId, labels_data])
        
    return pd.DataFrame(data, columns=['videoId', 'categories'])
            

def main():
    
    path = "/home/felipegiori/Documents/UFMG/2019-1/MSI II/data"
    files = []
    
    for r, d, f in os.walk(path):
        for file in f:
            if ".tfrecord" in file:
                files.append(os.path.join(r, file))

    data = pd.read_csv("data/data1.csv")
    
    for file in files:
        output = pd.read_csv(file)
        labels = pd.read_csv("label_names_2018.csv").set_index("label_id").to_dict()["label_name"]
    
        tmp = map_cat(output, labels)
        data = pd.concat([data, tmp])
        
    data.to_csv("data_complete.csv", index=False)
    
    
if __name__ == '__main__':
    main()