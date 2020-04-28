from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name="register"),
    path('login', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('asset/', views.asset, name="asset"),
    path('register_asset/', views.register_asset, name="register_asset"),
    path('get_assets/', views.get_assets, name="get_assets"),
    path('calculate/', views.calculate, name="calculate"),
    path('appreciation/', views.appreciation, name="appreciation"),
    path('depreciation/', views.depreciation, name="depreciation"),
    path('delete_assets/', views.delete_assets, name="delete_assets"),
    path('edit_assets/', views.edit_assets, name="edit_assets"),




]
