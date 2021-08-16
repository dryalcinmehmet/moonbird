from django.urls import path, include
from .views import QuestionApiView, RegistrationAPI, LoginAPI, LogoutAPI, ChangePasswordView


urlpatterns = [

    path('question/', QuestionApiView.as_view(), name="question-api"),
    path('question/<int:id>', QuestionApiView.as_view(), name="question-update-api"),


    # auth
    path('register/', RegistrationAPI.as_view()),
    path('login/', LoginAPI.as_view(),),
    path('logout/', LogoutAPI.as_view()),
    path('change-password/', ChangePasswordView.as_view())

]
