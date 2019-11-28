from django.contrib import admin
from .models import *
from Core.admin import BaseAdmin


class UserOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'salutation', 'skills', 'address')
    search_fields = ('id', 'username', 'email', 'salutation', 'skills', 'address')


class CityOptionsAdmin(BaseAdmin):
    list_display = ('id', 'city_name', 'city_code', 'created_on', 'created_by')
    search_fields = ('id', 'city_name', 'city_code')


class WorkPlacesOptionsAdmin(BaseAdmin):
    list_display = ('id', 'name', 'position', 'city', 'user')
    search_fields = ('id', 'name', 'position', 'city', 'user')


class EducationOptionsAdmin(BaseAdmin):
    list_display = ('id', 'school_college_name', 'attended_for', 'user')
    search_fields = ('id', 'school_college_name', 'attended_for', 'user')


class MyPlacesOptionsAdmin(BaseAdmin):
    list_display = ('id', 'place_name', 'lat_long', 'user')
    search_fields = ('id', 'place_name', 'lat_long', 'user')


class MyInterestOptionsAdmin(BaseAdmin):
    list_display = ('id', 'interest_code', 'user')
    search_fields = ('id', 'interest_code', 'user')


class MyLanguageOptionsAdmin(BaseAdmin):
    list_display = ('id', 'name', 'read', 'write', 'speak', 'user')
    search_fields = ('id', 'name', 'read', 'write', 'speak', 'user')


class MyProjectsOptionsAdmin(BaseAdmin):
    list_display = ('id', 'project_title', 'skills', 'team_size', 'client_name', 'user')
    search_fields = ('id', 'project_title', 'skills', 'team_size', 'client_name', 'user')


class SocialLinksOptionsAdmin(BaseAdmin):
    list_display = ('id', 'name', 'unique_id', 'user')
    search_fields = ('id', 'name', 'unique_id', 'user')


class MySkillsOptionsAdmin(BaseAdmin):
    list_display = ('id', 'user', 'skill')
    search_fields = ('id', 'user', 'skill')


class MyFollowersOptionsAdmin(BaseAdmin):
    list_display = ('id', 'user', 'follower')
    search_fields = ('id', 'user', 'follower')


admin.site.register(User, UserOptionsAdmin)
admin.site.register(City, CityOptionsAdmin)
admin.site.register(WorkPlace, WorkPlacesOptionsAdmin)
admin.site.register(Education, EducationOptionsAdmin)
admin.site.register(MyPlaces, MyPlacesOptionsAdmin)
admin.site.register(MyInterest, MyInterestOptionsAdmin)
admin.site.register(MyLanguage, MyLanguageOptionsAdmin)
admin.site.register(MyProjects, MyProjectsOptionsAdmin)
admin.site.register(SocialLinks, SocialLinksOptionsAdmin)
admin.site.register(MySkills, MySkillsOptionsAdmin)
admin.site.register(Followers, MyFollowersOptionsAdmin)
admin.site.register(Languages)
admin.site.register(Skills)
admin.site.register(Interests)
