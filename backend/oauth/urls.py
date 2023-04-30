from django.urls import path

from .views import UserView, AuthorView, SocialLinkView

urlpatterns = [
    path('me/', UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('author/<int:pk', AuthorView.as_view({'get': 'list'})),
    path('author_get/', AuthorView.as_view({'get': 'retrieve'})),
    path('social_links/', SocialLinkView.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'})),
    path('social_links/<int:pk>', SocialLinkView.as_view({'put': 'update', 'delete': 'destroy'})),

]
