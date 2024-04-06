from django.urls import path
from .views import Dashboard,Delete_course,Update_Course,Create_Course,Add_Catagorey,List_Catagorey,Delete_catagorey,Update_Catagorey,Update_User,Register,Login,List_contact,Update_contact,delete_contact,List_user,Parvelege,detail_customer,True_customer,False_customer,Logout_user,Par_Create_User,Accessorey,access_user,access_user_False,List_Course,Update_Customer,Update_Website_specifications,Check_Comments

app_name = 'accounts'

urlpatterns = [
    path('Dashboard/',Dashboard,name='dashboard'),
    path('delete_course/<int:id>/',Delete_course,name='delete_course'),
    path('Update_Course/<int:pk>/',Update_Course.as_view(),name='update_course'),
    path('Create_Course/',Create_Course.as_view(),name='create_course'),
    path('Add_catagorey/',Add_Catagorey.as_view(),name='add_catagorey'),
    path('List_catagorey/',List_Catagorey,name='list_catagorey'),
    path('delete_catagorey/<int:id>/',Delete_catagorey,name='delete_catagorey'),
    path('Update_catagorey/<int:pk>/',Update_Catagorey.as_view(),name='update_catagorey'),
    path('Update_user/<int:pk>/',Update_User.as_view(),name='update_user'),
    path('login/',Login,name='login'),
    path('register/',Register,name='register'),
    path('contact_list/',List_contact,name='list_contact'),
    path('update_contact/<int:pk>/',Update_contact.as_view(),name='update_contact'),
    path('delete/<int:id>/',delete_contact,name='delete_contact'),
    path('list_user/',List_user,name='list_user'),
    path('parvalege/<int:id>/',Parvelege,name='parvalege'),
    path('detail_customer_p/<int:id>/',detail_customer,name='detail_customer_p'),
    path('True_Customer/<int:id>/',True_customer,name='true_customer'),
    path('False_Customer/<int:id>/',False_customer,name='false_customer'),
    path('logout_user',Logout_user,name='logout'),
    path('Par_Create_User/',Par_Create_User,name='Par_Create_User'),
    path('Accessorey/',Accessorey,name='access'),
    path('access_users/<int:id>/',access_user,name='access_users'),
    path('access_users_False/<int:id>/',access_user_False,name='access_users_false'),
    path('list_course/',List_Course,name='list_course'),
    path('Update_Customer/<int:pk>/',Update_Customer.as_view(),name='update_customer'),
    path('Update_About_Web/<int:pk>/',Update_Website_specifications.as_view(),name='update_about_web'),
    path('check_comments/',Check_Comments,name='check_comments'),
]