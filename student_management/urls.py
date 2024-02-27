from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("pagination/",views.home,name='home') ,
    path("get/",views.StudentModelAPI.as_view()),
    path("page/",views.PaginationAPI.as_view()),
    path("standard/",views.StandardList.as_view())
    # path("get/<int:pk>/",views.StudentModelAPI.as_view())
]