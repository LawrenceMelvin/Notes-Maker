from django.urls import path
from . import views
urlpatterns=[
  path('',views.index,name='home'),
  path('add/',views.add,name='add'),
  path('del/<int:note_id>',views.delete,name='del'),
]