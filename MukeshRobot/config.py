
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "22016511" 
    API_HASH = "8267335b1cbd700a179dbe9a9a482d1e"
    TOKEN ="6851855443:AAFmoWl1ZN76tqVfDIagwKclt0zJ4Dh-mOc"  
    OWNER_ID = 6675703731
    
    SUPPORT_CHAT = "the_support_chat"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph//file/0ec1fb2c5769d3a062829.jpg"
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://saftpgt170:fePHBBhN9pB2lKnj@cluster0.7tdp3qi.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL="postgres://nfdksjkc:tF9g9bJkfc4bkQN9tIgzYfX1X-lc0cB6@lucky.db.elephantsql.com/nfdksjkc" 
    CASH_API_KEY = (
        "ONZ1SLDG89PVVMR7"  
    )
    TIME_API_KEY = ""
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
