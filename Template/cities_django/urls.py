from django.contrib import admin
from django.urls import path
from django.conf.urls import include 

# similar to Routes & Links from Express

# Pretty much boilerplate; just sub out tunr and add multiple paths/apps if using
urlpatterns = [
    path('admin/', admin.site.urls),
    # would specify path if necessary, but only one app running here so you can leave it as ('')
    #   -> would also have to add new apps in under Installed_Apps under settings.py
    path('', include('cities_app.urls')),
    path('api-auth', include ('rest_framework.urls', namespace='rest_framework'))
]