from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from ToDoApp.views import TodoView

router = DefaultRouter()
router.register('add',TodoView,basename='add')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls))
]
