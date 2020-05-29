from django.urls import path

from UserManager.views import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('view_all/', ViewUsersView.as_view()),
    path('view/{user_id}/', ViewSingleUserView.as_view()),
    path('add', AddSingleUserView.as_view()),
    path('edit', EditSingleUserView.as_view()),
    #path('edit/{user_id}/', EditSingleUserView.as_view()),
    path('inactivate/{user_id}', InactivateUserView.as_view()),
    path('department/{deparment_id}', DepartmentUserOverview.as_view())
]
