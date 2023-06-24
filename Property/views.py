from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from Property.serializers import *
from Property.models import *
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q



# Create your views here.
class GetStateView(APIView):
    def get(self, request, format=None):
        try:
            state = State.objects.all()
            serializer = StateSerializer(state, many=True)
            return Response({
                'data':serializer.data,
                "status":status.HTTP_200_OK,
            })

        except Exception as e:
            return Response({
                'mesaage':'Something is wornng',
                'status': status.HTTP_400_BAD_REQUEST,
                'error':str(e)
            })


class GetCityView(APIView):
    def get(self,request,id,format=None):
        try:

            state = City.objects.filter(state__id = id)
            serializer = CitySerializer(state, many=True)
            return Response({
                'data':serializer.data,
                "status":status.HTTP_200_OK,
            })

        except Exception as e:
            return Response({
                'mesaage':'Something is wornng',
                'status': status.HTTP_400_BAD_REQUEST,
                'error':str(e)
            })


class GetCategoryView(APIView):
    def get(self,request,format=None):
        try:

            category = Category.objects.all()
            serializer = GetCategorySerializer(category, many=True)
            return Response({
                'data':serializer.data,
                "status":status.HTTP_200_OK,
            })

        except Exception as e:
            return Response({
                'mesaage':'Something is wornng',
                'status': status.HTTP_400_BAD_REQUEST,
                'error':str(e)
            })

# get data from state and city 
class GetDataApiview(APIView):  
    def get(self,request):
        try:
            state_id = request.GET.get("state_id",None)
            city_id = request.GET.get("city_id",None)
            

            qs = Property.objects.filter(Q(state_id__id=state_id) & Q(city_id__id=city_id) )
            serializer = GetDataSerializer(qs ,many = True,context={'request': request})
            
            if serializer:
                return Response({
                    'message':"we got following data",
                    'status':status.HTTP_200_OK,
                    'data':serializer.data,})         
            else:
                return Response({
                            'message':'no data available',
                            'status':'False',
                            'code':status.HTTP_400_BAD_REQUEST,
                        })
        except Exception as e:
            return Response({
                'mesaage':'Something is wornng',
                'status': status.HTTP_400_BAD_REQUEST,
                'error':str(e)
            })




#get data from only category wise
class GetDataByCategoryView(APIView):
    def get(self,request):
        try:
            category_id = request.GET.get("category_id",None)
            qs = Property.objects.filter(category_id__id=category_id)
            serializer = GetDataSerializer(qs ,many = True,context={'request': request})
            
            if serializer:
                return Response({
                    'message':"Got data by category",
                    'status':status.HTTP_200_OK,
                    'data':serializer.data,})         
            else:
                return Response({
                            'message':'no data available',
                            'status':'False',
                            'code':status.HTTP_400_BAD_REQUEST,
                        })
        except Exception as e:
            return Response({
                'mesaage':'Something is worng',
                'status': status.HTTP_400_BAD_REQUEST,
                'error':str(e)
            })
    
 
# get data and post contact us
class GetContactUsView(APIView):
    def get(self,request,format=None):
        try:

            contactus = ContactUs.objects.all()
            serializer = GetContactUsSerializer(contactus, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({
                'message':'something went wrong',
                'status':status.HTTP_400_BAD_REQUEST,})


    def post(self,request,format=None):
        serializer = GetContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# # get data from state and city 
# class PropertyViewSet(viewsets.ModelViewSet):
#     serializer_class = GetDataSerializer
#     queryset = Property.objects.all()
#     filter_backends = (DjangoFilterBackend,)
#     filterset_fields = ['state_id', 'city_id']




