from django.contrib import admin

# Register your models here.
from models import AttackerCommander,DefenderCommander

admin.site.register(AttackerCommander)

admin.site.register(DefenderCommander)
