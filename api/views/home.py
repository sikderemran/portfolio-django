from django.http import JsonResponse
from django.views import View
from ..models.user import User
from ..models.education import Education
from django.core import serializers
import json

class home(View):
    def get(self, request):
        response={
            'status':204,
            'data':[]
        }
        user=User.objects.order_by('id')[:1]
        if user:
            serialized_data = serializers.serialize('json', user)
            data=json.loads(serialized_data)
            response={
                'status':200,
                'data':data
            }
        return JsonResponse(response, safe=False)
