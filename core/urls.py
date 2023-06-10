from django.contrib import admin
from django.urls import path, include
from allauth.account.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('apps.blog.urls', namespace='blog')),
    path('login/', LoginView.as_view(), name='login'),
]
