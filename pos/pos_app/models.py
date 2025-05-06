from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_waitress = models.BooleanField(default=False)
    is_cashier = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.username}{self.first_name}{self.last_name}'
    

class TabelResto(models.Model):
    status_choices = (
        ("Aktif","Aktif"),
        ("Tidak Aktif","Tidak Aktif")
    )
    status_table_choices = (
        ("Kosong","Kosong"),
        ("Terisi","Terisi")
    )
    code = models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    capacity=models.IntegerField(default=0)
    table_status = models.CharField(max_length=15,choices=status_table_choices,default="Kosong")
    status=models.CharField(max_length=15,choices=status_choices,default="Aktif")
    user_create= models.ForeignKey(User,related_name="user_create_tabel_resto",blank=True,null=True,on_delete=models.SET_NULL)
    user_update= models.ForeignKey(User,related_name="user_update_tabel_resto",blank=True,null=True,on_delete=models.SET_NULL)
    create_on = models.DateTimeField (auto_now_add=True)
    last_modified= models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
class StatusModel(models.Model):
    menu_status_choice=(
        ("Ada","Ada"),
        ("Tidak Ada","Tidak Ada")
    )
    status_choices = (
        ("Aktif","Aktif"),
        ("Tidak Aktif","Tidak Aktif")
    )
    status=models.CharField(max_length=15,choices=status_choices,default="Aktif") 
    menu_status=models.CharField(max_length=15,choices=menu_status_choice,default="Ada")

    def __str__(self):
        return f"Status: {self.status}, Menu: {self.menu_status}"

    
class MenuResto(models.Model):
    code = models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    price=models.FloatField(default=0.00)
    description=models.CharField(default="-")
    image_menu=models.ImageField(upload_to="menu_images/",blank=True,null=True)
    category=models.CharField(max_length=100)
    status=models.ForeignKey(StatusModel,related_name="status_of_menu",blank=True,null=True,on_delete=models.SET_NULL)
    create_on = models.DateTimeField (auto_now_add=True)
    last_modified= models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
    

