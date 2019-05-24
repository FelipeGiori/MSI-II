#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


def start_df(data):
    labels = pd.read_csv("label_names_2018.csv").set_index("label_id").to_dict()["label_name"]
    tmp = pd.DataFrame(index=data.videoId.values, columns=labels.values())
    tmp = tmp.fillna(0.0)
    return tmp

def str_2_tuple_List(s):
    return eval("[%s]" % s)


def main():
    data = pd.read_csv("data_complete.csv")
    tmp = start_df(data)
    
    for i, row in data.iterrows():
        videoId = row['videoId']
        categories = str_2_tuple_List(row['categories'])[0]
        for cat in categories:
            label = cat[0]
            value = cat[1]
            tmp.at[videoId, label] = value
            
    tmp.to_csv("data_label_as_columns.csv")
            
    
    
def main2():
    tmp2 = pd.DataFrame(index=data.videoId.values, columns=['categories'])
    
    for i, row in data.iterrows():
        videoId = row['videoId']
        categories = str_2_tuple_List(row['categories'])[0]
        labels = []
        for cat in categories:
            labels.append(cat[0])
            
        str_label = " "
        str_label = str_label.join(labels)
        tmp2.at[videoId, 'categories'] = str_label
        
    tmp2.to_csv("data_str_column.csv")
    
    
if __name__ == '__main__':
    main()