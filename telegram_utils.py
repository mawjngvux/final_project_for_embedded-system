from telegram import Bot
import asyncio

def send_telegram(photo_path="alert.png"):
    bot = Bot(token='7701817287:AAGU0hQCP93I9799HD1p7Qjvjp240R_qMjc') 
    asyncio.run(bot.send_photo(chat_id="7877025026", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiểm!"))
    print("Send sucessfully")