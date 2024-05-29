from django.contrib import admin

# Register your models here.

# Register your models here.
from .models import Company
from .models import Service
from .models import Industry
from .models import News


# Register your models here.
admin.site.register(Company)
admin.site.register(Service)
admin.site.register(Industry)
admin.site.register(News)