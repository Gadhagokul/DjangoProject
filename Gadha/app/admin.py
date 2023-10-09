from django.contrib import admin
from .models import user1
@admin.register(user1)
class useradmin(admin.ModelAdmin):
    list_display=('id','name','email','phone','password')
# Register your models here.
