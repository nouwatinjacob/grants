from django.urls import path, include

from . import views
from . import api as a


api = [
    path('application/add/', a.SubmitApplication.as_view()),
]

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('application/', views.Application.as_view(), name='application'),
    path('api/', include(api))
]