from django.shortcuts import render
from rest_framework.decorators import api_view, throttle_classes, schema
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.schemas import AutoSchema
from .admin import *
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import status

# Create your views here.
# View and Create Method
@api_view(["GET", "POST"])
def home(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj, many=True)
    if request.method == "POST":
        data = request.data
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status":404, "errors":serializer.errors, "message":"Something went wrong"})
        serializer.save()
        return Response({"status":200,"payload":serializer.data, "message":"save successfully"})
    return Response({"status":200, "payload":serializer.data})
# Update and Pach method
@api_view(["PUT"])
def student_update(request, id):
    try:
        student_obj = Student.objects.get(id=id)
        serializer = StudentSerializer(student_obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response({"status":404, "errors":serializer.errors, "message":"Something went wrong"})
        serializer.save()
        return Response({"status":200,"payload":serializer.data, "message":"save successfully"})
    except Exception as e:
        return Response({"status":403, "message":"Invalid Id"})
    # delete method
@api_view(["DELETE"])
def delete(request, id):
    try:
        student_obj = Student.objects.get(id=id)    
        student_obj.delete()
        return Response({"status":200, "message":"Delete the object"})
    except Exception as e:
        return Response({"status":403, "message":"Invalid id"})    




# views of Category and Book seializer
@api_view(["GET"])
def book(request):
    book_obj = Book.objects.all()
    serializer = BookSerializer(book_obj, many = True)
    return Response({"status":200, "payload":serializer.data})

@api_view(["GET","POST"])
def get_post_view(request):
    if request.method == "POST":
        return Response({"message":"Got some data!", "data":request.data})
    return Response({"message":"Hello World!"})

# API policy decorator
class OncePerDayUserThrottle(UserRateThrottle):
    rate = "1/day"
@api_view(["GET"])
@throttle_classes([OncePerDayUserThrottle])
def view(request):
    return Response({"message" : "Hello for today! see tomorrow"})

# view schema decorator
class CustomAutoSchema(AutoSchema):
    def get_link(self, path, method, base_url):
        pass
        # override view introspection here...
@api_view(["GET"])
@schema(CustomAutoSchema())
def schema_view(request):
    return Response({"message": "Hello for today! See you tomorrow!"})





    # Class based view (APIVIEW)
    """
    List all Admitions, or create a new Admition.
    """
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class AdmitionList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        admition_obj = Admition.objects.all()
        serializer = AdmitionSerializer(admition_obj, many= True)
        return Response({"status":200, "payload":serializer.data})

    def post(self, request):
        serializer = AdmitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":200, "payload":serializer.data, "message":"submited successfully"})
        return Response({"errors":serializer.errors, "status":403})
    
class AdmitionDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Admition.objects.get(pk=pk)
        except Admition.DoesNotExist:
            raise Http404
        
    def get(self,request,pk,formate=None):
        admition_obj = self.get_object(pk)
        serializer = AdmitionSerializer(admition_obj)
        return Response(serializer.data)
    
    def put(self, request, pk, formate=None):
        admition_obj = self.get_object(pk)
        serializer = AdmitionSerializer(admition_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":200, "payload":serializer.data, "message":"Data save successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk, formate=None):
        admition_obj = self.get_object(pk)
        serializer = AdmitionSerializer(admition_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":200, "payload":serializer.data, "message":"Data save successfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, formate=None):
        admition_obj = self.get_object(pk)
        admition_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# created token some users by manualy
from rest_framework.authtoken.models import Token
class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data["username"])
            token_obj= Token.objects.get_or_create(user=user)
            return Response({"status":200, "payload":serializer.data, "token":str(token_obj), "message":"user created successfully"})
        return Response({"errors":serializer.errors, "status":403, "message":"somethin went wrong"})