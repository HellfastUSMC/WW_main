from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('buildings/', include(('buildings.urls', 'buildings'), namespace='buildings')),
    path('flats/', include(('flats.urls', 'flats'), namespace='flats')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
]
