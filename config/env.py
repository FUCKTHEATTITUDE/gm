from os import getenv

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN',"5458696791:AAHLcBi665AvhM9MA20YtqK64VzZ14a_U8E")
MONGO_URI = getenv('MONGO_URI',"mongodb+srv://ALAN:20092001@cluster0.nmp83.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS',"1930954213").split()))
