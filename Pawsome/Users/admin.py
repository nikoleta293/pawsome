from django.contrib import admin
from . models import Users,PetOwner,Professional,Organizations

# Register your models here.

admin.site.register(Users)
admin.site.register(Professional)
admin.site.register(PetOwner)
admin.site.register(Organizations)


