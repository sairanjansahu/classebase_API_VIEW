from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(Product_category)

admin.site.register(Product)