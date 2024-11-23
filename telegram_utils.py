# # chat_id = "6995112280"  # phamhanh
# # chat_id = "7877025026"  #manhvu

from telegram import Bot
import asyncio
from datetime import datetime

def send_telegram(photo_path="alert.png", start_hour=9, start_minute=30, end_hour=18, end_minute=45):
    now = datetime.now()  
    current_time = now.hour * 60 + now.minute 
    start_time = start_hour * 60 + start_minute 
    end_time = end_hour * 60 + end_minute  

    if start_time <= current_time < end_time:
        bot = Bot(token='7701817287:AAGU0hQCP93I9799HD1p7Qjvjp240R_qMjc') 
        asyncio.run(bot.send_photo(chat_id="6995112280", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiểm!"))
        print("Send successfully")
    else:
        print(f"Không nằm trong khoảng thời gian từ {start_hour}:{start_minute:02d} đến {end_hour}:{end_minute:02d}. Không gửi ảnh.")

send_telegram(photo_path="alert.png", start_hour=9, start_minute=30, end_hour=18, end_minute=45)