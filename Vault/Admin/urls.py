from django.urls import path
from Admin.views import *

urlpatterns = [
    path('', AdminOverview.as_view()),
    path('shares/', ShareOverview.as_view()),
    path('shares/add/', AddShare.as_view()),
    path('shares/edit/{share_id}/', EditShare.as_view()),
    path('shares/delete/{share_id}/', DeleteShare.as_view()),
    path('log_messages/', LogMessageOverview.as_view()),
    path('log_message/{log_message_id}/', SpecificLogmessageOverview.as_view()),
]