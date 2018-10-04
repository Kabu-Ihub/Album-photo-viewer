from django.urls import path
from . import views
# app_name ='love'
urlpatterns = [
    path('',views.home,name="home"),
    path("list/",views.web ,name ="try"),
    path("<id>/",views.post_detail ,name="detail"),
    path('simple/',views.simple_upload,name="simple_upload"),
    path('form/',views.model_form_upload,name= 'model_form_upload'),
    path("<id>/delete",views.post_delete,name="delete")
]