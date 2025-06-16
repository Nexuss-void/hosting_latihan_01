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
    status_choices = (
        ("Aktif","Aktif"),
        ("Tidak Aktif","Tidak Aktif")
    )
    status=models.CharField(max_length=15,choices=status_choices,default="Aktif") 

    def __str__(self):
        return self.status
    
class Category(models.Model):
    status_choices = (
        ("Aktif","Aktif"),
        ("Tidak Aktif","Tidak Aktif")
    )
    name=models.CharField(max_length=100)
    status=models.CharField(max_length=15,choices=status_choices,default="Aktif")
    user_create= models.ForeignKey(User,related_name="user_create_category",blank=True,null=True,on_delete=models.SET_NULL)
    user_update= models.ForeignKey(User,related_name="user_update_category",blank=True,null=True,on_delete=models.SET_NULL)
    create_on = models.DateTimeField (auto_now_add=True)
    last_modified= models.DateField(auto_now=True)

    def __str__(self):
        return self.name

def increment_menu_resto_code():
        last_code = MenuResto.objects.all().order_by('id').last()
        if not last_code:
            return 'MN-0001'
        code = last_code.code
        code_int = int(code[3:7])
        new_code_int = code_int + 1
        return 'MN-' + str(new_code_int).zfill(4)

class MenuResto(models.Model):
    menu_status_choice=(
        ("Ada","Ada"),
        ("Tidak Ada","Tidak Ada")
    )
    code = models.CharField(max_length=20,default=increment_menu_resto_code, editable = False)
    name=models.CharField(max_length=100)
    price=models.FloatField(default=0.00)
    description=models.CharField(default="-")
    image_menu=models.ImageField(default='default_images/empt.jpg',upload_to="menu_images/",blank=True,null=True)
    category=models.ForeignKey(Category,related_name='category_menu',blank=True,null=True,on_delete=models.SET_NULL)
    status=models.ForeignKey(StatusModel,related_name="status_of_menu",blank=True,null=True,on_delete=models.SET_NULL)
    menu_status=models.CharField(max_length=15,choices=menu_status_choice,default="Ada")
    user_create= models.ForeignKey(User,related_name="user_create_menu",blank=True,null=True,on_delete=models.SET_NULL)
    user_update= models.ForeignKey(User,related_name="user_update_menu",blank=True,null=True,on_delete=models.SET_NULL)
    create_on = models.DateTimeField (auto_now_add=True)
    last_modified= models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.price}"
    

