urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', views.user_logout, name='logout'),
    ]
