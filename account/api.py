from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from knox.models import AuthToken
from .raudal_permissions import IsSuperUserOrSelfUser

from .models import UserAuth
from .serializers import LoginSerializer, UserSerializer, RegisterUserSerializer, UpdateUserSerializer, ChangePasswordSerializer


class RegisterAPI(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        try:
            UserAuth.objects.get(username=request.data['username'])
            return Response(status=status.HTTP_409_CONFLICT)
        except:
            serializer: RegisterUserSerializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(data=serializer.data)


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class UserAPI(generics.RetrieveDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperUserOrSelfUser]
    queryset = UserAuth.objects.all()


class UsersAPI(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def get_queryset(self):
        return UserAuth.objects.all()


class UpdateUserAPI(generics.UpdateAPIView):
    serializer_class = UpdateUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserAuth.objects.all()


class UsernameRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request, *args, **kwargs):
        try:
            username = kwargs['username']
            user = UserAuth.objects.get(username__exact=username)
            serializer = UserSerializer(user, context=self.get_serializer_context())
            return Response(data=serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permissions = [permissions.IsAuthenticated, IsSuperUserOrSelfUser]
    queryset = UserAuth.objects.all()

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        old_password = request.data.pop('old_password')
        instance = self.get_object()
        serializer: ChangePasswordSerializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request=request, username=instance.username, password=old_password)
        if not user or not user.is_active:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)
