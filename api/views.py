from django.shortcuts import render
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from .models import Sotrudniki, Podrazdeleniya, Doljnosti, Zadachi, Doljnost_sotrudnik, Sotrudnik_zadachi
from django.http import HttpResponse
from django.core import serializers as serialize
import json




class Sotrudniki_serializer(serializers.ModelSerializer):
    class Meta:
        model = Sotrudniki
        fields = ['id_sotrudnik', 'Code', 'Stavka', 'FIO']
        extra_kwargs = {
                'Stavka': {
                    'required': False,
                    'allow_null':True
                 }
            }
        
class Podrazdeleniya_serializer(serializers.ModelSerializer):
    category_name = serializers.RelatedField(source='Sotrudniki', read_only=True)
    class Meta:
        model = Podrazdeleniya
        fields = ('id_podrazdel', 'name_podrazdel', 'id_sotrudnik')
        extra_kwargs = {
                'id_sotrudnik': {
                    'required': False,
                    'allow_null':True
                 }
            }


def return_Sotrudniki(request):
    request = Sotrudniki.objects.all()
    request_json = serialize.serialize('json', request)
    return HttpResponse(request_json, content_type='application/json')
    

def return_Podradeleniya(request):
    request = Podrazdeleniya.objects.all()
    request_json = serialize.serialize('json', request)
    #print(request.values()[0]['id_nachal_id'])
    #query = Sotrudniki.objects.get(pk=request.values()[0]['id_nachal_id'])
    #print(request)
    #print(query.Code)
    #print(serialize.serialize('json', [query]))
    return HttpResponse(request_json, content_type='application/json')


def return_Doljnosti(request):
    request = Doljnosti.objects.all()
    request_json = serialize.serialize('json', request)
    #print(request_json)
    return HttpResponse(request_json, content_type='application/json')
    