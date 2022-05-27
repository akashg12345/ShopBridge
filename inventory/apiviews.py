from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from inventory.models import Items
from  inventory.serializers import ItemsSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView


## Exception handlings need to be present.(As per the need of Assingment)
## TO RETRIEVE THE ITEMS FROM INVENTORY

####### -----------------------------  @API_VIEW ---------------------

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET","POST","PUT","DELETE"])  ##  By default get request if no input is provided to @api_view
def student_api_view(request,pk = None):

    if request.method =="GET":

        data = request.data
        
        sid = pk
        ## if id is provided alongwith request than will fetch single data
        if sid :                           
            try :
                stud_obj = Items.objects.get(id = pk)

            ## if provided id doesnt exist will raise error     
            except Items.DoesNotExist:     
                msg = {"error":"given id doent exists"}
                res = JSONRenderer().render(msg)
                return HttpResponse(res,content_type = "application/json")
            ser = ItemsSerializer(stud_obj)
            
            return Response(ser.data)

        stud_obj = Items.objects.all()
        python_native = ItemsSerializer(stud_obj,many = True)
    
        return JsonResponse({"msg" : "Data retrieve success"})

###--------------------------------------------------- USING CONCRETE APIVIEW ------------------------------

### TO FETCH ALL THE ITEMS IN INVENTORY
class ItemsList(ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

### TO ADD NEW ITEMS TO INVENTORY   
class ItemsCreate(CreateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

### TO GET SINGLE DATA 
class ItemsRetrieve(RetrieveAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

### TO UPDATE EXISTING ITEMS IN INVENTORY
class ItemsUpdate(UpdateAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

### TO DELETE THE GIVEN ITEMS FROM INVENTORY
class ItemsDestroy(DestroyAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer




