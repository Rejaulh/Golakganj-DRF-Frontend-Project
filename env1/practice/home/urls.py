from django.contrib import admin
from django.urls import path, include
from .views import *
from home import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", home),
    path("view1/", get_post_view),
    path("view/", view),
    path("schema_view/", schema_view),
    path("student-update/<id>/", student_update),
    path("delete/<id>/", delete),
    path("book/", book),
    # class view (APIView) urls
    path("admition/", views.AdmitionList.as_view()),
    path("admition/<int:pk>/", views.AdmitionDetail.as_view()),
    # token create manualy
    path("register/", views.RegisterUser.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)