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
import re
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

##????????????    
    if text == '????????????????????????':
        FlexMessage = json.load(open('outdoor_info.json','r',encoding='utf-8'))

        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))

    
####################################################################################    

#?????????(complete)

#done in richmenu (by uri)

####################################################################################
    
#???????????????????????????
    
    if text == '??????????????????':
            line_bot_api.reply_message(event.reply_token,TextSendMessage(
                text = text
                                
            ) 
            )   

####################################################################################
            
            
#???????????????(undo)

            
    if text == '?????????????????????':
            FlexMessage = json.load(open('card.json','r',encoding='utf-8'))

            line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
####################################################################################


#???????????????

    if text == '???????????????????????????':

        FlexMessage = json.load(open('sure_snake_type_or_not.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        ########### edit by chen_yz
        
        #????????????
    if '???????????????' in text:
        FlexMessage = json.load(open('color.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
       
        #????????????
    if '????????????' in text and '????????????' in text:
        FlexMessage = json.load(open('head.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        #????????????
    if '????????????' in text:
        FlexMessage = json.load(open('but_bit.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '????????????????????????' in text or ('??????' in text and '????????????' in text ):
        FlexMessage = json.load(open('sure_chiwei.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '??????' in text:
        FlexMessage = json.load(open('green_bit.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))    
        
    if '?????????' in text or '??????????????????' in text:
        FlexMessage = json.load(open('but_bit.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        
    
        #????????????
    if '??????' in text or '???????????????' in text:
        FlexMessage = json.load(open('dimple.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        #????????????
    if '????????????' in text or '??????' in text or '??????' in text or '???????????????' in text or '?????????' in text or '?????????' in text or '???????????????' in text:
        FlexMessage = json.load(open('clinical.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        #??????????????????
    if '??????????????????' in text or '7A' in text:
        
        FlexMessage = json.load(open('sure_guike.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
    if '??????????????????' in text or '7B' in text:
        FlexMessage = json.load(open('sure_baibu.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '??????????????????' in text or '7C' in text:
        FlexMessage = json.load(open('sure_yusan.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '??????????????????' in text or '7D' in text or '?????????' in text:
        FlexMessage = json.load(open('sure_suolian.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))

    if '??????????????????' in text or '7E' in text:
        FlexMessage = json.load(open('sure_yanjing.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '7F' in text:
        text1 = '??????????????????????????????????????????????????????????????????????????????????????????????????????????????????'
        line_bot_api.reply_message(event.reply_token,[
                           TextSendMessage(text = text1)

        ]
                          ) 
        
    ## ??????xx??????   (?????????)
#     if re.search("??????*??????",text):
    serums={''}
    if re.search('??????[\w]*??????',text):
        species = text[2:-2]
        line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=f'Hello world')
        )
        
        
    
    
    
    
    
    
    
    if '????????????' in text:
        # ???????????????.json
        pass 
        
        
    if '???????????????' in text:
        #???????????????.json
        pass
        
    
        
####################################################################################

#??????????????????(complete)
    if text == '?????????????????????':
        
        line_bot_api.reply_message(event.reply_token,TextSendMessage(
            text = '?????????????????????\n' + 'https://line.me/R/nv/location/'

        ) 
        )

    if  '?????????' in text:
        
        
            FlexMessage = json.load(open('hospital.json','r',encoding='utf-8'))

            
        
   
            data = pd.read_csv(os.path.join(path,str(userid) + '.csv'))
            
            location = eval(data.tail(1).to_dict('list')['location'][0])

            location_tuple = location
            serum_type = text.split(' ')[1] 

            hosp_location = myfun.host_distace_3(location_tuple,serum_type)
            
#             hosp_address =  hosp_location['????????????']
#             hosp_latitude = hosp_location['?????????'].split(',')[0]
#             hosp_longitude = hosp_location['?????????'].split(',')[1]


#             line_bot_api.reply_message(event.reply_token,LocationSendMessage(
#                 title='????????????',
#                 address= hosp_address ,
#                 latitude = hosp_latitude,
#                 longitude = hosp_longitude
#             ) 
#                 )
            print(hosp_location)
            
            hosp_address =  hosp_location['????????????'][0]
            hosp_latitude = hosp_location['?????????'][0].split(', ')[0]
            hosp_longitude = hosp_location['?????????'][0].split(', ')[1]
            FlexMessage['contents'][0]['body']['contents'][0]['text'] =  hosp_address
            FlexMessage['contents'][0]['body']['contents'][1]['action']['uri'] = 'https://www.google.com/maps/search/?api=1&query=' + str(hosp_latitude) + '%2C' +str(hosp_longitude)
            
            
            hosp_address =  hosp_location['????????????'][1]
            hosp_latitude = hosp_location['?????????'][1].split(', ')[0]
            hosp_longitude = hosp_location['?????????'][1].split(', ')[1]
            FlexMessage['contents'][1]['body']['contents'][0]['text'] =  hosp_address
            FlexMessage['contents'][1]['body']['contents'][1]['action']['uri'] = 'https://www.google.com/maps/search/?api=1&query=' + str(hosp_latitude) + '%2C' + str(hosp_longitude)

            hosp_address =  hosp_location['????????????'][2]
            hosp_latitude = hosp_location['?????????'][2].split(', ')[0]
            hosp_longitude = hosp_location['?????????'][2].split(', ')[1]
            FlexMessage['contents'][2]['body']['contents'][0]['text'] =  hosp_address
            FlexMessage['contents'][2]['body']['contents'][1]['action']['uri'] = 'https://www.google.com/maps/search/?api=1&query=' + str(hosp_latitude) +'%2C' + str(hosp_longitude)

            line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
            
#########################################################################################   

#??????(complete)
    
        

     
    if text == '?????????':
        #????????????.json
        pass
    
    



################################################################################################################################################################
    
    
#????????????(half_done)
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
    
    
#???????????????(complete)     
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
    
    datetime_dt = datetime.datetime.today()# ??????????????????
    datetime_str = datetime_dt.strftime("%Y/%m/%d %H:%M:%S")  # ???????????????
    
    
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
