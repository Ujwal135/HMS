from django.urls import path
from .views import create_account,user_login,admin_dashboard,user_logout

urlpatterns = [
      path('accounts/',create_account, name='create_account'),
      path('login/',user_login, name ='login_page'),
      path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
      path('logout/',user_logout,name = 'logout')
]
