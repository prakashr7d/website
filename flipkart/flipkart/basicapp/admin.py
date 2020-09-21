from django.contrib import admin
from basicapp import models

admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Category)
admin.site.register(models.Comments)