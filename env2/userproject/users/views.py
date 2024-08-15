from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from users.serializers import WorkerSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework import generics, permissions
from .models import UserProfile
from .serializers import *
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.models import Token


# class RegisterView(generics.CreateAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#             "user": {
#                 "username": user.username,
#                 "email": user.email,
                
#             },
#         }, status=status.HTTP_201_CREATED)
    
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": RegisterSerializer(user).data,
            "token": token.key,
            "message": "User created successfully",
        }, status=status.HTTP_201_CREATED)

    # Login View
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    # def post(self, request):
    #     try:
    #         refresh_token = request.data["refresh"]
    #         token = RefreshToken(refresh_token)
    #         token.blacklist()
    #         return Response(status=status.HTTP_205_RESET_CONTENT)
    #     except Exception as e:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    



class UserListCreate(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.userprofile.save()


from rest_framework_simplejwt.authentication import JWTAuthentication   
from rest_framework.permissions import IsAuthenticated
class WorkerView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        worker_obj = Worker.objects.all()
        serializer = WorkerSerializer(worker_obj, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class WorkerDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Worker.objects.get(pk=pk)
        except Worker.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        worker_obj = self.get_object(pk)
        serializer = WorkerSerializer(worker_obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Worker_obj = self.get_object(pk)
        serializer = WorkerSerializer(Worker_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
        Worker_obj = self.get_object(pk)
        serializer = WorkerSerializer(Worker_obj, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        Worker_obj = self.get_object(pk)
        Worker_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)