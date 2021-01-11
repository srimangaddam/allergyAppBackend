from django.conf.urls import url
from restaurantMenus import views

urlpatterns = [
    url(r'^api/restaurantMenus/add/$', views.restaurantMenu_change),  # noqa: E501
    url(r'^api/restaurantMenus/view/$', views.restaurantMenu_list,),  # noqa: E501
]
