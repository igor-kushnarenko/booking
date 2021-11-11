from django.urls import path, include

from board import views


urlpatterns = [
    path('user/<int:pk>', views.UserRetrieveUpdateView.as_view()),
    path('user/update/<int:pk>', views.UserUpdateView.as_view()),
    path('user/all', views.UserListView.as_view()),
]