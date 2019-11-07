from django.contrib import admin
from .models import *


class UserOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'salutation', 'skills', 'address')
    search_fields = ('id', 'username', 'email', 'salutation', 'skills', 'address')


class CityOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_name', 'city_code', 'created_by')
    search_fields = ('id', 'city_name', 'city_code', 'created_by')


class WorkPlacesOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'city', 'user')
    search_fields = ('id', 'name', 'position', 'city', 'user')


class EducationOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'school_college_name', 'attended_for', 'user')
    search_fields = ('id', 'school_college_name', 'attended_for', 'user')


class MyPlacesOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'lat_long', 'user')
    search_fields = ('id', 'place_name', 'lat_long', 'user')


class MyInterestOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'interact_code', 'user')
    search_fields = ('id', 'interact_code', 'user')


class MyLanguageOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'read', 'write', 'speak', 'user')
    search_fields = ('id', 'name', 'read', 'write', 'speak', 'user')


class MyProjectsOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_title', 'skills', 'team_size', 'client_name', 'user')
    search_fields = ('id', 'project_title', 'skills', 'team_size', 'client_name', 'user')


class SocialLinksOptionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'unique_id', 'user')
    search_fields = ('id', 'name', 'unique_id', 'user')


admin.site.register(User, UserOptionsAdmin)
admin.site.register(City, CityOptionsAdmin)
admin.site.register(WorkPlace, WorkPlacesOptionsAdmin)
admin.site.register(Education, EducationOptionsAdmin)
admin.site.register(MyPlaces, MyPlacesOptionsAdmin)
admin.site.register(MyInterest, MyInterestOptionsAdmin)
admin.site.register(MyLanguage, MyLanguageOptionsAdmin)
admin.site.register(MyProjects, MyProjectsOptionsAdmin)
admin.site.register(SocialLinks, SocialLinksOptionsAdmin)

