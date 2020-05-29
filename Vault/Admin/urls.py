from django.urls import path
from Admin.views import *

urlpatterns = [
    path('', AdminOverview.as_view()),
    path('network_shares/', NetworkShareOverview.as_view()),
    path('network_shares/add/', AddNetworkShare.as_view()),
    path('network_shares/edit/{network_share_id}/', EditNetworkShare.as_view()),
    path('network_shares/delete/{network_share_id}/', DeleteNetworkShare.as_view()),
    path('log_messages/', LogMessageOverview.as_view()),
    path('log_message/{log_message_id}/', SpecificLogmessageOverview.as_view()),
]