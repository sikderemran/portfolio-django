from django.http import JsonResponse
from django.views import View
from ..models.user import User
from ..models.education import Education
from ..models.experience import Experience
from ..models.skills import Skill
from ..models.social import Social
from django.core import serializers
import json

class about(View):
    def get(self, request):

        user=User.objects.all()
        educations=Education.objects.all()
        experiences=Experience.objects.all()
        skills=Skill.objects.all()
        social=Social.objects.all()
        
        serialized_data = serializers.serialize('json', user)
        user_data=json.loads(serialized_data)

        serialized_data = serializers.serialize('json', educations)
        education_data=json.loads(serialized_data)

        serialized_data = serializers.serialize('json', experiences)
        experience_data=json.loads(serialized_data)

        serialized_data = serializers.serialize('json', skills)
        skill_data=json.loads(serialized_data)

        serialized_data = serializers.serialize('json', social)
        social_data=json.loads(serialized_data)

        response={
            'status':200,
            'data':{
                'user_data':user_data,
                'education_data':education_data,
                'experience_data':experience_data,
                'skill_data':skill_data,
                'social_data':social_data
            }
        }
        return JsonResponse(response, safe=False)
