# import telegram
# import asyncio

# async def send_telegram(photo_path="alert.png"):
#     try:
#         my_token = "7701817287:AAGU0hQCP93I9799HD1p7Qjvjp240R_qMjc"
#         bot = telegram.Bot(token=my_token)
#         await bot.sendPhoto(chat_id="7877025026", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!")
#     except Exception as ex:
#         print("Can not send message telegram ", ex)

#     print("Send sucess")

from telegram import Bot
import asyncio

def send_telegram(photo_path="alert.png"):
    bot = Bot(token='7701817287:AAGU0hQCP93I9799HD1p7Qjvjp240R_qMjc')  # Thay bằng token của bot
    # Sử dụng asyncio.run để gọi coroutine send_photo
    asyncio.run(bot.send_photo(chat_id="7877025026", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiểm!"))
    print("Send sucessfully")