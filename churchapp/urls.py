from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.register, name='signup'),
    path('signin', views.login_view, name='signin'),
    path('signout', views.logout_view, name='signout'),
    path('events', views.events, name='events'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    # path('news', views.news, name='news'),
    path('notices', views.notices, name='notices'),
    path('notice-form', views.notice_form, name='notice-form'),
    # path('notice-detail/<int:id>', views.notice_details, name='notice-detail'),
    path('notice-detail/<int:pk>', views.notice_details, name='notice-detail'),

    #temporary url
    path('create-superuser/', views.create_superuser),
]
