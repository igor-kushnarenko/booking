from django.urls import path, include

from board import views


urlpatterns = [
    path('user/<int:pk>', views.UserRetrieveUpdateView.as_view()),
    path('user/update/<int:pk>', views.UserUpdateView.as_view()),
    path('user/destroy/<int:pk>', views.UserDestroyView.as_view()),
    path('user/all', views.UserListView.as_view()),
    path('user/new', views.UserCreateView.as_view()),

    path('service/<int:pk>', views.ServiceRetrieveUpdateView.as_view()),
    path('service/update/<int:pk>', views.ServiceUpdateView.as_view()),
    path('service/all', views.ServiceListView.as_view()),
    path('service/new', views.ServiceCreateView.as_view()),
]