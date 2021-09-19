from django.urls import path
from .views import RegisterView, LoginAPIView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginAPIView.as_view()),

]