from django.urls import path
from .views import Home,Courses,Website,detail_Course,detail_Catagorey,course,customer,contact,Search_Course,delete_Comments,About_us


app_name = 'web'

urlpatterns = [
    
    path('Courses/',Courses,name='courses'),
    path('',Website,name='website'),
    path('detail_Catagorey/<int:id>/',detail_Catagorey,name='detail_Catagorey'),
    path('detail_course/<int:id>/',detail_Course,name='detail_course'),
    path('course/',course,name='course'),
    path('customer/',customer,name='customer'),
    path('contact/',contact.as_view(),name='contact'),
    path('search_course/',Search_Course,name='search_course'),
    path('delete_comment/<int:id>/',delete_Comments,name='delete_comment'),
    path('About_Use/',About_us,name='about_us')
]