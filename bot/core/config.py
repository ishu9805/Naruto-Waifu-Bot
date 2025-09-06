import os
from dotenv import load_dotenv

load_dotenv()

# Get values from environment variables with fallbacks
OWNER_ID = os.getenv('OWNER_ID', '6902029663').split(',')
PARTNER = os.getenv('PARTNER', '6902029663,7651091427').split(',')
sudo_users = os.getenv('SUDO_USERS', '6902029663').split(',')

# Bot configuration
TOKEN = os.getenv('TOKEN', '7980212347:AAEWnraCCFkp6An3RaBnx3GMneHmlssYRsA')
mongo_url = os.getenv('MONGO_URL', 'mongodb+srv://abhi47903:sashtadev143@naruto.svojv.mongodb.net/')

# Channel/Group IDs
GROUP_ID = int(os.getenv('GROUP_ID', '-1002198664660'))
LOG_CHANNEL = int(os.getenv('LOG_CHANNEL', '-1003074022043'))
CHARA_CHANNEL_ID = int(os.getenv('CHARA_CHANNEL_ID', '-1002117539029'))
required_group_id = int(os.getenv('REQUIRED_GROUP_ID', '-1002872842561'))

# API credentials
api_id = int(os.getenv('API_ID', 22792918))
api_hash = os.getenv('API_HASH', 'ff10095d2bb96d43d6eb7a7d9fc85f81')

# URLs
PHOTO_URL = os.getenv('PHOTO_URL', 'https://envs.sh/Eiz.mp4,https://envs.sh/EiL.mp4,https://envs.sh/Eic.mp4').split(',')
SUPPORT_CHAT = os.getenv('SUPPORT_CHAT', 'https://t.me/+77WFaB7bj9k2OTll')
UPDATE_CHAT = os.getenv('UPDATE_CHAT', 'https://t.me/blade_x_community')
BOT_USERNAME = os.getenv('BOT_USERNAME', 'https://t.me/Naruto_Waifu_Husbando_Bot?startgroup=true')

# Settings
STRICT_GBAN = os.getenv('STRICT_GBAN', 'True').lower() == 'true'
ALLOW_CHATS = os.getenv('ALLOW_CHATS', 'True').lower() == 'true'
ALLOW_EXCL = os.getenv('ALLOW_EXCL', 'True').lower() == 'true'
DEL_CMDS = os.getenv('DEL_CMDS', 'True').lower() == 'true'
INFOPIC = os.getenv('INFOPIC', 'True').lower() == 'true'
