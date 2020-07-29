from django.urls import path
from myapp import views
app_name="myapp" #is used to create a namespace\

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name='home'),
    path('fact/<n>',views.fact,name='fact'),
    #path('secondary suffix', address of function, name of mapping)
    path('child/',views.child,name="child"),
    path('base/',views.base,name='base'),
]
