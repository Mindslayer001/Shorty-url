from django.urls import path
from .views import index, root_link, add_link, delete_link, UpdateLink, QRCodeView

urlpatterns = [
    path("", index, name="home"),
    path("link/delete/<str:link_slug>/", delete_link, name="delete-link"),
    path("link/create/", add_link, name="create-link"),
    path("link/<str:link_slug>/", root_link, name="root-link"),
    path("link/edit/<str:slug>", UpdateLink.as_view(), name="update-link"),
    path("link/qrcode/<str:link_slug>/", QRCodeView.as_view(), name="qr-generate"),
]
