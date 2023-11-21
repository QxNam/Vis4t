import dotenv
import os

dotenv.load_dotenv(r'..\Vis4T_main\.env')

HOST = os.getenv('HOST')
NAME = os.getenv('NAME')
DBUSER = os.getenv('DBUSER')
PORT = os.getenv('PORT')
PASSWORD = os.getenv('PASSWORD')

DEPLOYMENT_NAME = os.getenv('DEPLOYMENT_NAME')
OPENAI_API_BASE = os.getenv('OPENAI_API_BASE')
OPENAI_API_VERSION = os.getenv('OPENAI_API_VERSION')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
OPENAI_API_TYPE = os.getenv('OPENAI_API_TYPE')