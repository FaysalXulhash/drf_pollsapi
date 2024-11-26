
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('poll.urls')),
    path('accounts/', include('accounts.urls')),
    path('rest/', include('rest_framework.urls')),
    #path('get_token/', obtain_auth_token),
]
