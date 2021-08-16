from django.urls import path, include
from .views import QuestionListView, QuestionDetailView, IndexView, HealthCheckView, SignInView, SignOutView, \
    PasswordResetView, PasswordChangeView, PasswordChangeSuccessView, SignUpView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('question', QuestionListView.as_view(), name="question"),
    path('question-detail/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('version', HealthCheckView.as_view(), name="version"),
    path("accounts/login/", SignInView.as_view(), name='login'),
    path("accounts/logout/", SignOutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name="auth/password_reset_form.html"), name='password-reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="auth/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="auth/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_reset_complete/', PasswordChangeSuccessView.as_view(), name='password_reset_complete'),
]
