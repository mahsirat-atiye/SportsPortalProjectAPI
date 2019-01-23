from django.contrib import admin

# Register your models here.
from leads.models import News, Lead

admin.site.register(News)
admin.site.register(Lead)
