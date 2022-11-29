from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('blog.urls')),
    path('messages/', include('chat.urls')),
    path('', RedirectView.as_view(url='pages/', permanent=False), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
