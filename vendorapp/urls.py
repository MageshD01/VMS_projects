from django.urls import path
from . import views

urlpatterns = [
    # -------- Authentication --------
    path('', views.login_view, name="login"),  # default login
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('logout/', views.logout_user, name="logout"),

    # -------- Dashboard --------
    path('dashboard/', views.home, name="dashboard"),

    # -------- Vendor --------
    path('vendor/add/', views.vendor_form, name="vendor_form"),
    path('vendor/list/', views.vendor_list, name="vendor_list"),
    path('vendor/edit/<int:id>/', views.vendor_edit, name='vendor_edit'),
    path('vendor/delete/<int:id>/', views.vendor_delete, name='vendor_delete'),

    # -------- Product --------
    path('product/add/', views.product_form, name="product_form"),
    path('product/list/', views.product_list, name="product_list"),
    path('product/edit/<int:id>/', views.product_edit, name='product_edit'),
    path('product/delete/<int:id>/', views.product_delete, name='product_delete'),
]
