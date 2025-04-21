from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    # 空路径指向登陆视图
    path('',views.login_user,name='login'),
    path('login_user/',views.login_user,name="login_user"),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('register_user/',views.register_user,name='register_user'),
    # 用户资料
    path('user_profile/', views.user_profile, name='user_profile'),
]
