from django.db import models
from django.contrib import admin
class Bike_DB(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Bike_no=models.CharField(max_length=15)
    Brand_name=models.CharField(max_length=10)
    phone_no=models.IntegerField(primary_key=True)
    Licence=models.CharField(max_length=10)
    Address=models.TextField()
class Bike_DBAdmin(admin.ModelAdmin):
    list_display=["Name","Age","Bike_no","Brand_name","phone_no","Licence","Address"]
