from django.urls import path
from . import views
from django.urls.conf import include
from django.contrib.auth import views as auth_views

app_name = "app"
urlpatterns = [
   path('',views.index,name='index'),
   path('main/',views.main,name='main'),
   path('index/',views.index,name='index'),
   path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
   path('nasa/',views.nasa,name='nasa'),
   path('realtime/',views.realtime,name='realtime'),
]