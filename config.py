# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21414727")

API_HASH = os.environ.get("API_HASH", "b4135f6b8cd476d931e78787a0cb77c1")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7093405647:AAEI4naYKiJYjX2smeVhMFHbz_TJ70CfpJQ") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Movilious") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Cluster0")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://abhishekkum:PassMongo@cluster0.cfviomt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/b13f89e74f5d221a94536.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6796937630').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
