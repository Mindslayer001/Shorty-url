from django.urls import path
from .views import index, root_link, add_link,delete_link

urlpatterns = [
    path("", index, name="home"),
    path("<str:link_slug>/", root_link, name="root-link"),
    path("link/create/", add_link, name="create-link"),
    path('link/delete/<str:linkname>/', delete_link, name='delete-link'),
]