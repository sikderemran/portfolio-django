from django.http import JsonResponse
from django.views import View
from ..models.project import Project

from django.core import serializers
import json

class work(View):
    def get(self, request):

        works=Project.objects.all()
    
        serialized_data = serializers.serialize('json', works)
        work_data=json.loads(serialized_data)

        response={
            'status':200,
            'data':{
                'work_data':work_data
            }
        }
        return JsonResponse(response, safe=False)
