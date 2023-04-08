from Vis4T_main.wsgi import *
from HomePage.models import *
from HomePage.serializers import *
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView


def get_object(pk: str):
        try:
            return University_class.objects.get(class_name=pk)
        except University_class.DoesNotExist:
            raise Http404
    
def get(pk, format=None):
    pk = pk.upper()
    class_ = get_object(pk)
    student_ = Student.objects.filter(class_name=class_)
    student_serializer = StudentSerializer(student_, many=True)
    student_data = student_serializer.data
    
    response = {
        'student': student_data
    }
    return {'data': response}

print(get('khmt13a'))