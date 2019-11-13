import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import View


class EmployeeInfo(View):
    def get(self, request, *args, **kwargs):
        d1 = {"idno":101, "name":"Mithila", "salary":225000.00}
        json_data = json.dumps(d1)
        return HttpResponse(json_data, content_type="application/json")
    def post(self, request, *args, **kwargs):
        d1 = {"idno":102, "name":"Pratyusha", "salary":300000.00}
        json_data = json.dumps(d1)
        return HttpResponse(json_data, content_type="application/json")
    def put(self, request, *args, **kwargs):
        d1 = {"idno":103, "name":"Nithya", "salary": 450000.00}
        json_data = json.dumps(d1)
        return HttpResponse(json_data, content_type="application/json")
    def delete(self, request, *args, **kwargs):
        d1 = {"idno":104, "name":"Siri", "salary": 145000.00}
        json_data = json.dumps(d1)
        return HttpResponse(json_data, content_type="application/json")

