from django.urls import path, include
from .views import home, logout_view, detele_task, edit_task, calendar, landing_page


app_name = 'core'

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('', landing_page, name='landing_page'),
    path('home', home , name='home'),
    path('edit_task/<int:task_id>/', edit_task, name='edit_task'),
    path('delete_task/<int:task_id>/', detele_task, name='delete_task'),
    path('calendar/', calendar, name='calendar'),
    path('users/', include('users.urls', namespace='users')),
] 