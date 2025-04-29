from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from pos_app.models import User,TabelResto
from api.serializers import TableRestoSerializer

class TableRestoListApiView(APIView):
    def get(self,request,*args,**kwargs):
        table_restos=TabelResto.objects.all()
        serializer=TableRestoSerializer(table_restos,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        data={
            'code':request.query_params.get('code'),
             'name':request.query_params.get('name'),
             'capacity':request.query_params.get('capacity'),
            # 'code':request.data.get('code'),
            # 'name':request.data.get('name'),
            # 'capacity':request.data.get('capacity'),
        }
        serializer=TableRestoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response={
                'status':status.HTTP_201_CREATED,
                'message':'Data Berhasil Dibuat....',
                'data':serializer.data,
            }
            return Response(response,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class TableRestoDetailApiView(APIView):
    def get_object(self,id):
        try:
            return TabelResto.objects.get(id=id)
        except TabelResto.DoesNotExist:
            return None
    
    def get (self,request,id,*args,**kwargs):
        table_resto_instance=self.get_object(id)
        if not table_resto_instance:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message':'Data Tidak Ada....',
                    'data':[],
                },status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer=TableRestoSerializer(table_resto_instance)
        response={
            'status': status.HTTP_400_BAD_REQUEST,
                    'message':'Data Berhasil Diambil....',
                    'data':serializer.data,
        }
        return Response(response,status=status.HTTP_200_OK)
    
    def put(self,request,id,*args,**kwargs):
        table_resto_instance=self.get_object(id) 
        if not table_resto_instance:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message':'Data Tidak Ada....',
                    'data':[],
                },status=status.HTTP_400_BAD_REQUEST
            )
        
        data={
            'code': request.data.get('code'),
            'name': request.data.get('name'),
            'capacity': request.data.get('capacity'),
            'table_status': request.data.get('table_status'),
            'status': request.data.get('status'),
            # 'code': request.query_params.get('code'),
            # 'name': request.query_params.get('name'),
            # 'capacity': request.query_params.get('capacity'),
            # 'table_status': request.query_params.get('table_status'),
            # 'status': request.query_params.get('status'),
        }
        serializer=TableRestoSerializer(instance=table_resto_instance,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            response={
                'status':status.HTTP_200_OK,
                'message':'Update Data Berhasil...',
                'data':serializer.data,
            }
            return Response(response,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id,*args,**kwargs):
        table_resto_instance=self.get_object(id)
        if not table_resto_instance:
            return Response(
                {
                    'status': status.HTTP_400_BAD_REQUEST,
                    'message':'Data Tidak Ada....',
                    'data':[],
                },status=status.HTTP_400_BAD_REQUEST
            )
        
        table_resto_instance.delete()
        response={
            'status': status.HTTP_200_OK,
            'message':'Delete Data Berhasil....',
        }
        return Response(response,status=status.HTTP_200_OK)
    
class TableRestoGetPostApiView(ListCreateAPIView):
    serializer_class=TableRestoSerializer
    queryset=TabelResto.objects.all()

class TableRestoGetUpdateDeleteApiView(RetrieveUpdateDestroyAPIView):
    serializer_class=TableRestoSerializer
    queryset=TabelResto.objects.all()
