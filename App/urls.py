from . import views
from django.urls import path
from .views import  BlogView, SupplicationsView, RecitationsView, PostList, PostView  


urlpatterns = [
  path('',                PostList.as_view(),           name="home"),
  path('<slug:slug>/',    PostView.as_view(),           name="post_detail"),
  path('blog/',           BlogView.as_view(),           name="blog"),
  path('supplications/',  SupplicationsView.as_view(),  name="supplications"),
  path('recitations/',    RecitationsView.as_view(),    name="recitations"),
]
