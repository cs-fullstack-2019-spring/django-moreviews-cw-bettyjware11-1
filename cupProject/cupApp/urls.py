from django.urls import path
from . import views
# # Create a "hello" route
# # Create a "times2" route
# # Create a "total" route
# Create an 'all/' endpoint
urlpatterns = [

    path('hello/<str:name>', views.gethello, name="greeting"),
    path('times2/<int:number>', views.times2, name="times2"),
    path('total/<int:number>', views.total, name="total"),
    path('', views.index),
    path('all/purchaseTimes', views.purchaseTimes, name="times"),
    path('changeMaterial'),
]

# phoneApp
# from django.urls import path
# from . import views
#
#
# urlpatterns = [
#     path('', views.index, name="index"),
#     path('all/', views.all, name="all"),
#     path('add5/<int:number>', views.add5, name="add5"),
#     path('name3times/<str:name>', views.names100, name="names100"),
# ]


# computerApp
# from django.urls import path
# from . import views
#
#
# urlpatterns = [
#     path('', views.index),
#     path('computerIndex/', views.computerIndex),
#     path('createNew/', views.create),
# ]