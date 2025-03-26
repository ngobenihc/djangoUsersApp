from rest_framework import routers

from users.views import UserViewSets

name ="users"

route = routers.DefaultRouter()
route.register(r"user",UserViewSets)