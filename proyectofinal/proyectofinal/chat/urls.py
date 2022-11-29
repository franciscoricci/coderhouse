from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.ver_mensajes, name='list_messages'),
    path('write', views.send_msg, name='write_message'),
]