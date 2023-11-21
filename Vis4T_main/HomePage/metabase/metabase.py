import requests
from .configs import *
import jwt
# SESSION = requests.Session()

def get_token(payload):
    return jwt.encode(payload, METABASE_EMBEDDING_SECRET_KEY, algorithm="HS256")

def get_iframe_from_dashboard_id(dashboard_id):
    payload = {
        "resource": {"dashboard": dashboard_id},
        "params": {}
    }
    token = get_token(payload)
    iframe_url = f"{METABASE_SITE_URL}/embed/dashboard/{token}/#bordered=false&titled=false"
    return iframe_url

def get_class_dashboard_from_class_name(dashboard_id, class_name_id):
    payload = {
        "resource": {"dashboard": dashboard_id},
        "params": {
            "class_name_id": class_name_id
        },
    }
    token = get_token(payload)
    iframe_url = f"{METABASE_SITE_URL}/embed/dashboard/{token}/#bordered=false&titled=false"
    return iframe_url

def get_iframe_url(dashboard_id, **kwargs):
    class_name_id = kwargs.get('class_name')
    student_id = kwargs.get('student_id')
    semester_id = kwargs.get('semester_id', 1)
    params = {}
    if class_name_id:
        params['class_name_id'] = class_name_id
    if student_id:
        params['student_id'] = student_id
        params['semester_id'] = semester_id
    payload = {
        "resource": {"dashboard": dashboard_id},
        "params": params,
    }
    token = get_token(payload)
    iframe_url = f"{METABASE_SITE_URL}/embed/dashboard/{token}/#bordered=false&titled=false"
    return iframe_url