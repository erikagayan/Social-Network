from rest_framework import generics
from users.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from social_app.permissions import IsAdminOrIfAuthenticatedReadOnly


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(TokenObtainPairView):
    pass


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_object(self):
        return self.request.user
