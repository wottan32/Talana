from django.urls import include, path
from django.contrib import admin



# Serializers define the API representation.
from . import views

urlpatterns = [
    path('admin/', admin.sites.urls),
    path('', views.SaveUser, name='SaveUser'),

    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
