from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('user',views.user,name='user'),
    path('user/topics',views.topics,name='topics'),
    path('user/<int:id>',views.chats,name='chats'),
    path('user/add',views.add,name='add'),
    path('user/topics/my',views.topics,name='mytopics'),
    path('signin',views.signin,name='signin'),
    path('update',views.update,name='update'),

]