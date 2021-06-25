from django.urls import path
from .views import xtermjs, device_list
urlpatterns = [
    path('',device_list,name="device_list"),
    path('xtermjs/<int:user_id>',xtermjs, name="xtermjs")
]