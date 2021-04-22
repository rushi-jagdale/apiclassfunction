from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse,HttpResponse
import json


# Create your views here.

#Class based view

class Jsoncbv(View):
    
    def get(self,request,*args,**kwargs):
        emp_data ={
            'eno':123,
            'name':'rushi',
        }
        
        return JsonResponse(emp_data)

    def post(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'this is post mehtod'})
        emp_data ={
            'eno':123,
            'name':'rushi',
        }
        emp_data = json.dumps(emp_data)
        return HttpResponse(emp_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'this is put mehtod'})
        return HttpResponse(json_data,content_type='application/json')
    
    def delete(self,request,*args,**kwargs):
        json_data = json.dumps({'msg':'this is delete mehtod'})
        return HttpResponse(json_data,content_type='application/json')

#function based view
def jsonfbv(request):
    
    data = {
        'sno':234,
        'sname':'shivani',
    }
    return JsonResponse(data)

