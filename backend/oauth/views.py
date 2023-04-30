from rest_framework import viewsets, parsers, permissions
from .serializers import UserSerializer, AuthorSerializer, SocialLinkSerializer
from .models import SocialLink, AuthUser, Follower
from .permissions import IsAuthor


# Create your views here.
class UserView(viewsets.ModelViewSet):
    """
    CRUD CustomUser
    """
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()


class AuthorView(viewsets.ReadOnlyModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthorSerializer


class SocialLinkView(viewsets.ModelViewSet):
    serializer_class = SocialLinkSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        return self.request.user.social_links.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
