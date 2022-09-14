from django.urls import path

from . import views
# from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

# router = DefaultRouter()
# router.register('', views.PostList, basename='post')
# urlpatterns = router.urls

urlpatterns = [
    path('post/<str:pk>/',views.PostDetail.as_view(), name='detailcreate'),
    path('search/', views.PostListDetailfilter.as_view(), name='postsearch'),
    path('', views.PostList.as_view(), name='listcreate'),
    # POST ADMIN URLS
    path('admin/list/', views.AdminPostList.as_view(), name='listpost'),
    path('admin/create/', views.CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', views.AdminPostDetail.as_view(), name='admindetailpost'),
    path('admin/edit/<int:pk>/', views.EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', views.DeletePost.as_view(), name='deletepost'),

]
