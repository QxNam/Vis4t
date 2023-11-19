import requests
from .configs import *
# SESSION = requests.Session()

def get_token(payload):
    return jwt.encode(payload, METABASE_EMBEDDING_SECRET_KEY, algorithm="HS256")

def get_iframe_from_dashboard_id(dashboard_id, class_name):
    payload = {
        "resource": {"dashboard": dashboard_id},
        "params": {"class_name": class_name}
    }
    token = get_token(payload)
    iframe_url = f"{METABASE_SITE_URL}/embed/dashboard/{token}/#bordered=false&titled=false"
    return iframe_url