from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from minha_dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('minha_dashboard.urls')),
    path('login/', views.login_user),
    path('login/submit', views.submit_login),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)