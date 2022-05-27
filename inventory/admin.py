from django.contrib import admin
from inventory.models import Items,Categories

# Register your models here.
admin.site.register([Items,Categories])
