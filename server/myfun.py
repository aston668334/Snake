import pyimgur
import cv2

import pandas as pd
from haversine import haversine_vector, Unit ,haversine
import numpy as np



def to_url(PATH):
    """
    plt.figure(figsize=(240,240))
    plt.plot(ug)
    plt.savefig('send.png')
    """
    CLIENT_ID = "8fede842ec9cc9a"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")

    return (uploaded_image.link)



def host_distace_3(target,serum_type):
    data = pd.read_csv('./serum_done.csv')
    
    select_data = data[data[serum_type] == 1]
    
    data_list = list(select_data['經緯度'])
    coordinate_list =[]
    target_list = []
    for i in data_list:
        latitude = float(i.split(',')[0])
        longitude = float(i.split(',')[1])
        temp = (latitude , longitude)
        coordinate_list.append(temp)
        target_list.append(target)
        
    distance_list = list(haversine_vector(target_list, coordinate_list, Unit.KILOMETERS))
    
    vals = np.array(distance_list)
    sort_index = np.argsort(vals)[0:3]
    
#     shortest_distance = min(distance_list)
#     shortest_index = distance_list.index(shortest_distance)
    out  = select_data.iloc[list(sort_index)].to_dict('list')
    
    return (out)



def host_distace(target,serum_type):
    data = pd.read_csv('./serum_done.csv')
    
    select_data = data[data[serum_type] == 1]
    
    data_list = list(select_data['經緯度'])
    coordinate_list =[]
    target_list = []
    for i in data_list:
        latitude = float(i.split(',')[0])
        longitude = float(i.split(',')[1])
        temp = (latitude , longitude)
        coordinate_list.append(temp)
        target_list.append(target)
        
    distance_list = list(haversine_vector(target_list, coordinate_list, Unit.KILOMETERS))
       
    shortest_distance = min(distance_list)
    shortest_index = distance_list.index(shortest_distance)
    out  = select_data.iloc[shortest_index]
    
    return (out)

