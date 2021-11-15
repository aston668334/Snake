import os
#ml

from predict import model_predict

from PIL import Image
import re
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
    MessageEvent, TextMessage, TextSendMessage, ImageMessage ,ImageSendMessage , FlexSendMessage ,LocationMessage ,LocationSendMessage, TemplateSendMessage , StickerSendMessage,
)

import json
import math



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

##野外安全(complete)
    if text == '野外安全注意事項':
        FlexMessage = json.load(open('outdoor_info.json','r',encoding='utf-8'))

        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))

    
    if text == '安全探索的六大原則':
    
        text1 = '1.勿接近已公告之危險水域與地區\n2.充分了解周遭環境資源'
        text2 = '3.密切注意氣候變化\n4.穿著正確服裝並攜帶必要藥品'
        text3 = '5.告知家人朋友活動範圍\n6.平日學習基本求生技能'
        text4 = '祝您旅途愉快'
        
        
        line_bot_api.reply_message(event.reply_token,[
                                   TextSendMessage(text = text1), 
                                   TextSendMessage(text = text2),
                                   TextSendMessage(text = text3),
                                   TextSendMessage(text = text4),
                                   
        ]
                                  ) 
        
    if text == '在空曠地區從事戶外活動遇暴雨':
        text1 = '在空曠地區從事戶外活動遇暴雨怎麼辦？'
        text2 = '小心雷擊，雨天的靜電比較小，閃電通常會被引到最高處，在曠野中遇到下雨，不要找高大的物體躲避，也不要接近孤立的凸出物：像是大樹、路燈、電線杆、鐵欄杆、涼亭等，讓自己愈貼近地面愈好。手持大型金屬柄雨傘也可能成為雷擊的目標，因此雷雨天請盡量減少佩戴金屬飾品'
        text3 = '快樂旅遊平安回家'
        line_bot_api.reply_message(event.reply_token,[
                           TextSendMessage(text = text1), 
                           TextSendMessage(text = text2),
                           TextSendMessage(text = text3),

        ]
                          ) 
        
        
       
    if text == '野外需要的裝備':
        text1 = '野外活動需要什麼裝備及穿著？'
        text2 = '帽子：防中暑、防蚊蟲叮咬、氣溫低時保\n上著：長袖， 防止叮咬感染；肩背、膝肘和臀部要有加強層，避免磨破'
        text3 = '下著：彈性長褲，便於活動及保護腳部；鞋襪大小要適當\n裝備：急救包、個人藥品；瑞士刀，用於砍伐阻礙路線的植被；水壺、乾糧，用於補充水分及能量'
        text4 = '祝您旅途愉快'
        line_bot_api.reply_message(event.reply_token,[
                           TextSendMessage(text = text1), 
                           TextSendMessage(text = text2),
                           TextSendMessage(text = text3),
                           TextSendMessage(text = text4),

        ]
                          ) 

    
####################################################################################    

#蛇圖鑑(complete)

#done in richmenu (by uri)

####################################################################################
    
#蛇常出沒位置及時間(give up)
    
    if text == '蛇常出沒位置及時間':
        text1 = '正在開發不好意思QQ' 
        line_bot_api.reply_message(event.reply_token,[
                                       TextSendMessage(text = text1),
                                       StickerSendMessage(package_id=11539, sticker_id= 52114110),
            ]
            )   

####################################################################################
            
            
#被咬怎麼半(complete)

            
    if text == '被蛇咬到怎麼辦':
        
        url = 'https://i.imgur.com/8HFVVcT.png'
        
        text1 = '        等待就醫時，先做初步的處置\n1.保持冷靜勿驚慌，離開毒蛇可能攻擊到的範圍，立即打119求救'
        text2 = '2.脫去受傷處的衣物、手錶、戒指等束縛物\n3.避免喝含有酒精或咖啡因的飲品'
        text3 = '4.減緩毒液擴散：盡量減少活動，心情跟呼吸保持平靜，減少血液循環的加速。患肢保持不動，而且位置要低於心臟的高度'
        text4 = '5.不要冰敷，避免冰敷使循環變差，造成組織大量壞死\n6.點選下方功能表查詢「我遇到什麼種類的蛇」，可以得出您遇到蛇的種類及得出是否需要注射血清'

        
            
        line_bot_api.reply_message(event.reply_token,[
                                   ImageSendMessage(original_content_url= url, preview_image_url=url),
                                   TextSendMessage(text = text1), 
                                   TextSendMessage(text = text2),
                                   TextSendMessage(text = text3),
                                   TextSendMessage(text = text4),

                                   
        ]
                                   )
        
# ####################################################################################


#遇到蛇模蛇

    if text == '我遇到什麼種類的蛇':

        FlexMessage = json.load(open('sure_snake_type_or_not.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))

        ########### edit by chen_yz
        
        #蛇的顏色
    if '不是這些蛇' in text:
        FlexMessage = json.load(open('color.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
       
        #蛇的頭型
    if '但不確定' in text and '牙洞咬痕' in text:
        FlexMessage = json.load(open('head.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        #咬痕種類
    if '但不確定' in text:
        FlexMessage = json.load(open('but_bit.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '確定是赤尾青竹絲' in text or ('綠色' in text and '牙洞咬痕' in text ):
        FlexMessage = json.load(open('sure_chiwei.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '綠色' in text:
        FlexMessage = json.load(open('green_bit.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))    
        
    if '灰棕色' in text or '黑白相間環紋' in text:
        FlexMessage = json.load(open('bit.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        
    
        #蛇的頰窩
    if '圓形' in text or '記不清頭型' in text:
        FlexMessage = json.load(open('dimple.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        #臨床表現
    if '參差咬痕' in text or '紅色' in text or '黃色' in text or '記不清顏色' in text or '三角形' in text or '有頰窩' in text or '記不清頰窩' in text:
        FlexMessage = json.load(open('clinical.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
        #最後一步確定
    if '確定是龜殼花' in text or '7A' in text:
        
        FlexMessage = json.load(open('sure_guike.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
        
    if '確定是百步蛇' in text or '7B' in text:
        FlexMessage = json.load(open('sure_baibu.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '確定是雨傘節' in text or '7C' in text:
        FlexMessage = json.load(open('sure_yusan.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '確定是鎖鍊蛇' in text or '7D' in text or '無頰窩' in text:
        FlexMessage = json.load(open('sure_suolian.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))

    if '確定是眼鏡蛇' in text or '7E' in text:
        FlexMessage = json.load(open('sure_yanjing.json','r',encoding='utf-8'))
        line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
    
    if '7F' in text:
        text1 = '您遇到的不是毒蛇，有可能是無毒或毒性極低的蛇，但也請儘快前往附近醫院就醫診斷'
        line_bot_api.reply_message(event.reply_token,[
                           TextSendMessage(text = text1)

        ]
                          ) 
        
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
            FlexMessage['contents'][0]['body']['contents'][1]['contents'][0]['margin'] =  str(max(20*(4-(math.ceil((len(hosp_address)/9)))),0)) + 'px'
            FlexMessage['contents'][0]['body']['contents'][2]['action']['uri'] = 'https://www.google.com/maps/search/?api=1&query=' + str(hosp_latitude) + '%2C' +str(hosp_longitude)
            
            
            hosp_address =  hosp_location['單位名稱'][1]
            hosp_latitude = hosp_location['經緯度'][1].split(', ')[0]
            hosp_longitude = hosp_location['經緯度'][1].split(', ')[1]
            FlexMessage['contents'][1]['body']['contents'][0]['text'] =  hosp_address
            FlexMessage['contents'][1]['body']['contents'][1]['contents'][0]['margin'] =  str(max(20*(4-(math.ceil((len(hosp_address)/9)))),0)) + 'px'
            FlexMessage['contents'][1]['body']['contents'][2]['action']['uri'] = 'https://www.google.com/maps/search/?api=1&query=' + str(hosp_latitude) + '%2C' + str(hosp_longitude)

            hosp_address =  hosp_location['單位名稱'][2]
            hosp_latitude = hosp_location['經緯度'][2].split(', ')[0]
            hosp_longitude = hosp_location['經緯度'][2].split(', ')[1]
            FlexMessage['contents'][2]['body']['contents'][0]['text'] =  hosp_address
            FlexMessage['contents'][2]['body']['contents'][1]['contents'][0]['margin'] =  str(max(20*(4-(math.ceil((len(hosp_address)/9)))),0)) + 'px'
            FlexMessage['contents'][2]['body']['contents'][2]['action']['uri'] = 'https://www.google.com/maps/search/?api=1&query=' + str(hosp_latitude) +'%2C' + str(hosp_longitude)

            line_bot_api.reply_message(event.reply_token, FlexSendMessage('profile',FlexMessage))
            
#########################################################################################   

#沒事(complete)
    
        

     
    if  re.search('我真的[\w]*沒事',text):
        #回復真棒.json
#         if re.search("我被*咬了",text):
#     if '我被龜殼花咬了' in text:
        line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=f'Hello world')
        )
        pass
    
            #     if re.search("我被*咬了",text):
    serums={'龜殼花':['出血性毒蛇','抗龜殼花及赤尾鮐蛇毒血清'],
           '赤尾青竹絲':['出血性毒蛇','抗龜殼花及赤尾鮐蛇毒血清'],
           '百步蛇':['出血性毒蛇','抗百步蛇毒血清'],
           '雨傘節':['神經性毒蛇','抗雨傘節及飯匙倩蛇毒血清'],
           '眼鏡蛇':['神經性毒蛇','抗雨傘節及飯匙倩蛇毒血清'],
           '鎖鏈蛇':['混合性毒蛇','抗鎖鏈蛇毒血清」，以對抗蛇毒']}
    
    if re.search('我被[\w]*咬了',text):
        print(text)
        species = text[2:-2]
        print(f"species={species})")
        line_bot_api.reply_message(
        event.reply_token,
        TextMessage(text=f'您所遇到的是{species}，為{serums[species][0]}，需要注射「{serums[species][1]}」，以對抗蛇毒。')
        )
    
    



################################################################################################################################################################
    
    
#影像辨識(half_done)
@handler.add(MessageEvent, message=ImageMessage)
def message_Image(event):
    user_image = line_bot_api.get_message_content(event.message.id)
    user = line_bot_api.get_profile(event.source.user_id)
    
    
    datetime_dt = datetime.datetime.today()# 獲得當地時間
    datetime_str = datetime_dt.strftime("%Y%m%d_%H%M%S")  # 格式化日期
    
    with open('./server_image/'+ str(user.user_id) +'_'+ datetime_str + '.jpg' , 'wb') as fd:
        for chunk in user_image.iter_content():
            fd.write(chunk)
        
    Path = './server_image/'+ str(user.user_id) +'_' +datetime_str  + '.jpg'
    img = Image.open(Path).convert("RGB")

    a = model_predict()
    out_predict = a.predict(img)

    
#     line_bot_api.reply_message(event.reply_token,TextSendMessage(
#     text = out_predict

#     ) 
#     )   
    url = 'https://www.google.com/search?q=' + out_predict.split('-')[0] +'+'+ out_predict.split('-')[1]+ '&oq=' +out_predict.split('-')[0] +'+'+ out_predict.split('-')[1] +'&aqs=chrome..69i57.471j0j7&sourceid=chrome&ie=UTF-8'
    line_bot_api.reply_message(event.reply_token,TextSendMessage(
    text = ('是不是' +out_predict.split('-')[0] +' '+ out_predict.split('-')[1] + '呢?\n你看看\n' + url)

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
