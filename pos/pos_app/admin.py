from django.contrib import admin
from pos_app.models import User,TabelResto,Category,MenuResto,StatusModel
# Register your models here.
admin.site.register(User)
admin.site.register(TabelResto)
admin.site.register(StatusModel)
admin.site.register(Category)
admin.site.register(MenuResto)