from django.contrib import admin
from django.urls import path, include
from user import views as view_user 
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("dashboard.urls")),
    path('register/', view_user.register, name ="user-register"),
    path('profile/', view_user.profile, name ="user-profile"),
    path('profile/update/', view_user.profile_update, name ="user-profile-update"),
    path('', auth_views.LoginView.as_view(template_name="user/login.html"), name="user-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="user/logout.html"), name="user-logout"),
    path('password_rest/', auth_views.PasswordResetView.as_view(), name="password_rest"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)