import telegram
import asyncio

my_token = "7701817287:AAGU0hQCP93I9799HD1p7Qjvjp240R_qMjc"
bot = telegram.Bot(token = my_token)
# chat_id = "6995112280"  # phamhanh
chat_id = "7877025026"  #manhvu

async def send_telegram(photo_path="alert.png"):
    try:
        await bot.send_photo(chat_id="7877025026", photo=open(photo_path, "rb"), caption = "213")
        # await bot.send_message(chat_id="7877025026", text="Yeu huong vch")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")

send_telegram()