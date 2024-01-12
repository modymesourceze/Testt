from os import getenv
from dotenv import load_dotenv
from os import environ

load_dotenv("config.env")

TOKEN = environ.get("TOKEN")
API_ID = int(environ.get("25281175"))
API_HASH = environ.get("6d99cb2b60a2c519fc1f99bd19565730")
API_ID1 = int(environ.get("25281175"))
API_HASH1 = environ.get("6d99cb2b60a2c519fc1f99bd19565730")
sudoers = [int(x) for x in environ.get("6581896306").split()]
LOG_GROUP_ID = environ.get("-1002015543535")
BASE_DB = environ.get("mongodb+srv://bot_vambir:Al2552001@cluster0.heabj.mongodb.net/vambir_bot?retryWrites=true&w=majority")
MONGO_URL = environ.get("mongodb+srv://bot_vambir:Al2552001@cluster0.heabj.mongodb.net/vambir_bot?retryWrites=true&w=majority")
ARQ_API_URL = environ.get("https://arq.hamker.in")
ARQ_API_KEY = environ.get("VXIWBI-DIQJVN-YSWZLO-TNYZIS-ARQ")
COMMAND_PREFIXES = list(getenv("ح ف ب غ س ك و م ا ت / ! . ذ ق ف ش").split())
F_SUB_CHANNEL = environ.get("Source_Ze")
BOT_PREFIX = environ.get(".")