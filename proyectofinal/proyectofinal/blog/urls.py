from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name="login"),
    path('logout/', views.logout_request, name= "logout"),
    path('post/', views.postear, name= "post"),
    path('delete/<post_id>', views.delete, name= "delete_post"),
    path('pages/<post_id>', views.ver_post, name= "ver_post"),
    path('profile/', views.profile, name= "users-profile"),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('about/', views.about, name= "about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)