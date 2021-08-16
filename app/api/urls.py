from django.urls import path, include
from .views import QuestionApiView, RegistrationAPI, LoginAPI, LogoutAPI, ChangePasswordView
from search.views import OsosViewSet, OsosInsertData

urlpatterns = [

    path('question/', QuestionApiView.as_view(), name="question-api"),
    path('question/<int:id>', QuestionApiView.as_view(), name="question-update-api"),


    # auth
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view(),),
    path('logout/', LogoutAPI.as_view()),
    path('change-password/', ChangePasswordView.as_view()),

    #elk
    path('osos/', OsosViewSet.as_view({'get':'list'}), name="osos"),
    path('insert/', OsosInsertData.as_view(), name="insert"),

]
