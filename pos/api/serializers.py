from rest_framework import serializers
from pos_app.models import (User,TabelResto)

class TableRestoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TabelResto
        fields=('id','code','name','capacity','table_status','status')