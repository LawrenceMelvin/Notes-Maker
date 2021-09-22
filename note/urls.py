from django.urls import path
from . import views
urlpatterns=[
  path('',views.index,name='home'),
  path('add/',views.add,name='add'),
  path('del/<int:note_id>',views.delete,name='del'),
  path('register/',views.registration,name='register'),
  path('login/',views.loginpage,name='login'),
  path('logout/',views.logoutview,name='logout'),
]