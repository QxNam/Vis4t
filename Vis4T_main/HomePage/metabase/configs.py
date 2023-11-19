import dotenv
import os

dotenv.load_dotenv(r'..\Vis4T_main\.env')

METABASE_EMBEDDING_SECRET_KEY = os.getenv('METABASE_EMBEDDING_SECRET_KEY')
METABASE_SITE_URL = os.getenv('METABASE_SITE_URL')
METABASE_SESSION_ID = os.getenv('METABASE_SESSION_ID')