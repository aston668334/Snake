import os
#ml
# import image_predict

from PIL import Image

import pyimgur
import cv2
import numpy
import pandas as pd
import myfun
import datetime
if os.getenv('DEVELOPMENT') is not None:
    from dotenv import load_dotenv

    load_dotenv(dotenv_path='../.env')

import sys

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage ,ImageSendMessage , FlexSendMessage ,LocationMessage ,LocationSendMessage, TemplateSendMessage , 
)

import json




app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET') or 'YOUR_SECRET'
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN') or 'YOUR_ACCESS_TOKEN'

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# Echo function
# @handler.add(MessageEvent, message=TextMessage)
# def message_text(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text)
#     )

# CSV Example
# import csv
# @handler.add(MessageEvent, message=TextMessage)
# def message_text(event):
#     rows_list = []
#     with open(os.path.abspath("maskdata.csv"), newline='') as csvfile:
#         rows = csv.reader(csvfile, delimiter=',')
#         for row in rows:
#             rows_list.append(row)
#
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=str(rows_list[1]))
#     )

############################################################################################################################################
@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
#     print(event)
    user = line_bot_api.get_profile(event.source.user_id)
    userid = user.user_id
#     print("!!!!!!!!!!!!!!!!!")
#     print(user)
#     print("!!!!!!!!!!!!!!!!!")

    
    text = event.message.text
    path = './user_data'
    dirs = os.listdir(path)
    
####################################################################################

##野外安全    
    if text == '野外安全注意事項':
        FlexMessage = json.load(open('outdoor_info.json','r',encoding='utf-8'))

        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))

    
####################################################################################    

#蛇圖鑑(complete)

#done in richmenu (by uri)

####################################################################################
    
#蛇常出沒位置及時間
    
    if text == '蛇常出沒位置':
            line_bot_api.reply_message(event.reply_token,TextSendMessage(
                text = text
                                
            ) 
            )   

####################################################################################
            
            
#被咬怎麼半(undo)

            
    if text == '被蛇咬到怎麼辦':
            FlexMessage = json.load(open('card.json','r',encoding='utf-8'))

            line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
####################################################################################


#遇到蛇模蛇

    if text == '我遇到什麼種類的蛇':

        FlexMessage = json.load(open('sure_snake_type_or_not.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        ########### edit by chen_yz
        
        #蛇的顏色
    if '不是這些蛇' in text:
        FlexMessage = json.load(open('sure_guike.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        #咬痕種類
    if '但不確定' or '灰棕色' or '黑白相間環紋' or '綠色' in text:
        FlexMessage = json.load(open('sure_guike.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        #最後一步確定
    if '確定是龜殼花' in text:
        
        FlexMessage = json.load(open('sure_guike.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
    if '確定是百步蛇' in text:
        FlexMessage = json.load(open('sure_baibu.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '確定是雨傘節' in text:
        FlexMessage = json.load(open('sure_yusan.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '確定是鎖鍊蛇' in text:
        FlexMessage = json.load(open('sure_suolian.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '確定是赤尾青竹絲' in text:
        FlexMessage = json.load(open('sure_chiwei.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))

    if '確定是眼鏡蛇' in text:
        FlexMessage = json.load(open('sure_yanjing.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
                
        
        
        #     if re.search("我被*咬了",text):
    serums={'龜殼花':['出血性毒蛇','抗龜殼花及赤尾鮐蛇毒血清'],
           '赤尾青竹絲':['出血性毒蛇','抗龜殼花及赤尾鮐蛇毒血清'],
           '百步蛇':['出血性毒蛇','抗百步蛇毒血清'],
           '雨傘節':['神經性毒蛇','抗雨傘節及飯匙倩蛇毒血清'],
           '眼鏡蛇':['神經性毒蛇','抗雨傘節及飯匙倩蛇毒血清'],
           '鎖鏈蛇':['混合性毒蛇','抗鎖鏈蛇毒血清」，以對抗蛇毒']}
    
    if re.search('我被[\w]*咬了',text):
        species = text[2:-2]
        line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=f'您所遇到的是{species}，為{serums[species[0]]}，需要'\
                   f'注射「{serums[species[1]]}」，以對抗蛇毒。')
        )
    
    
    
    
    
    
    
    if '確定蛇種' in text:
        # 有沒有腫脹.json
        pass 
        
        
    if '有沒有腫脹' in text:
        #有沒有瘀血.json
        pass
        
    
        
####################################################################################

#哪有蛇毒血清(complete)
    if text == '哪裡有抗毒血清':
        
        line_bot_api.reply_message(event.reply_token,TextSendMessage(
            text = '先選擇您的地點\n' + 'https://line.me/R/nv/location/'

        ) 
        )

    if  '我需要' in text:
        
        
            FlexMessage = json.load(open('hospital.json','r',encoding='utf-8'))

            
        
   
            data = pd.read_csv(os.path.join(path,str(userid) + '.csv'))
            
            location = eval(data.tail(1).to_dict('list')['location'][0])

            location_tuple = location
            serum_type = text.split(' ')[1] 

            hosp_location = myfun.host_distace_3(location_tuple,serum_type)
            
#             hosp_address =  hosp_location['單位名稱']
#             hosp_latitude = hosp_location['經緯度'].split(',')[0]
#             hosp_longitude = hosp_location['經緯度'].split(',')[1]


#             line_bot_api.reply_message(event.reply_token,LocationSendMessage(
#                 title='最近醫院',
#                 address= hosp_address ,
#                 latitude = hosp_latitude,
#                 longitude = hosp_longitude
#             ) 
#                 )
            print(hosp_location)
            
            hosp_address =  hosp_location['單位名稱'][0]
            hosp_latitude = hosp_location['經緯度'][0].split(', ')[0]
            hosp_longitude = hosp_location['經緯度'][0].split(', ')[1]
            FlexMessage['contents'][0]['body']['contents'][0]['text'] =  hosp_address
            FlexMessage['contents'][0]['body']['contents'][1]['action']['uri'] = 'https://www.google.com/maps/search/?api=1&query=' + str(hosp_latitude) + '%2C' +str(hosp_longitude)
            
            
            hosp_address =  hosp_location['單位名稱'][1]
            hosp_latitude = hosp_location['經緯度'][1].split(', ')[0]
            hosp_longitude = hosp_location['經緯度'][1].split(', ')[1]
            FlexMessage['contents'][1]['body']['contents'][0]['text'] =  hosp_address
            FlexMessage['contents'][1]['body']['contents'][1]['action']['uri'] = 'https://www.google.com/maps/search/?api=1&query=' + str(hosp_latitude) + '%2C' + str(hosp_longitude)

            hosp_address =  hosp_location['單位名稱'][2]
            hosp_latitude = hosp_location['經緯度'][2].split(', ')[0]
            hosp_longitude = hosp_location['經緯度'][2].split(', ')[1]
            FlexMessage['contents'][2]['body']['contents'][0]['text'] =  hosp_address
            FlexMessage['contents'][2]['body']['contents'][1]['action']['uri'] = 'https://www.google.com/maps/search/?api=1&query=' + str(hosp_latitude) +'%2C' + str(hosp_longitude)

            line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
            
#########################################################################################   

#沒事(complete)
    
        

     
    if text == '我沒事':
        #回復真棒.json
        pass
    
    



################################################################################################################################################################
    
    
#影像辨識(half_done)
@handler.add(MessageEvent, message=ImageMessage)
def message_Image(event):
    user_image = line_bot_api.get_message_content(event.message.id)
    user = line_bot_api.get_profile(event.source.user_id)

    with open('./server_image/'+ str(user.user_id) + '.jpg' , 'wb') as fd:
        for chunk in user_image.iter_content():
            fd.write(chunk)
        
    Path = './server_image/'+ str(user.user_id) + '.jpg'
    img = Image.open(Path).convert("RGB")
    out_predict = image_predict.image_predict(img)
    
    line_bot_api.reply_message(event.reply_token,TextSendMessage(
    text = out_predict

    ) 
    )   
#     url = myfun.to_url('./server_image/'+ str(user.user_id) + '.jpg')
    
#     line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url=url , preview_image_url=url))
##################################################################################################################################################################    
    
    
#傳位置記錄(complete)     
@handler.add(MessageEvent, message=LocationMessage)
def message_text(event):
    user_address = event.message.address
    user_latitude = event.message.latitude
    user_longitude = event.message.longitude
    user = line_bot_api.get_profile(event.source.user_id)
    
    
    FlexMessage = json.load(open('request_serum.json','r',encoding='utf-8'))

    line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))

    
    
    userid = user.user_id
    path = './user_data'
    dirs = os.listdir(path)
    
    datetime_dt = datetime.datetime.today()# 獲得當地時間
    datetime_str = datetime_dt.strftime("%Y/%m/%d %H:%M:%S")  # 格式化日期
    
    
    if str(userid) + '.csv' in  dirs:
        
        data = pd.read_csv(os.path.join(path,str(userid) + '.csv'))
        temp = {'userid':userid,
        'location': (float(user_latitude),float(user_longitude)),
                'date_time': datetime_str
        }
        data = data.append(temp, ignore_index=True)

        data.to_csv(os.path.join(path,str(userid) + '.csv'),index = False)
        
    else:

        data = pd.DataFrame([] , columns = ['userid','location','date_time'])

        temp = {'userid':userid,
        'location': (float(user_latitude),float(user_longitude)),
                'date_time': datetime_str
        }
        data = data.append(temp, ignore_index=True)

        data.to_csv(os.path.join(path,str(userid) + '.csv'),index = False)
               
    
    
#     FlexMessage = json.load(open('card.json','r',encoding='utf-8'))
    
#     line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage)) 
###################################################################################################




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
