from os import environ 

class Config:
    API_ID = environ.get("API_ID", "20176556")
    API_HASH = environ.get("API_HASH", "8136bd26f62a889221fc6d25cebe4e6a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7246880320:AAGPRcq_9Lr6x68Ytw1npiCVXthgVZjLg7w") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://akuspart:xswhARGUtukiR4bK@cluster0.dmxsf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6964148334').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
