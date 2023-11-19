import dotenv
import os

dotenv.load_dotenv(r'..\Vis4T_main\.env')

TYPESENSE_ADMIN_KEY = os.getenv('TYPESENSE_ADMIN_KEY')
TYPESENSE_SEARCH_KEY = os.getenv('TYPESENSE_SEARCH_KEY')
TYPESENSE_HOST = os.getenv('TYPESENSE_HOST')