from django.contrib import admin

from .models.education import Education
from .models.user import User
from .models.experience import Experience
from .models.project import Project
from .models.skills import Skill
from .models.social import Social

class UserAdmin(admin.ModelAdmin):
    list_display=('username','designation','image','about','resume','phone')

admin.site.register(Education)
admin.site.register(User,UserAdmin)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Social)
