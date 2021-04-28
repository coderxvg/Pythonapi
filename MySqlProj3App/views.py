from django.shortcuts import render
from rest_framework.parsers import  JSONParser
from .serializers import CcrFormSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from .models import CcrFormnew

# Create your views here.

def CcrFormGet(request):
    stu = CcrFormnew.objects.all()
    serializer = CcrFormSerializer(stu,many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')