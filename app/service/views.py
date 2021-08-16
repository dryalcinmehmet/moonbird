from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, AnswersSerializer
from django.views.generic import TemplateView, ListView, DetailView
from .version import Version
from django.contrib.auth import get_user_model
from .models import Questions, Answers
from .forms import SignupForm
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from .forms import QuoteForm
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"


class PasswordResetView(TemplateView):
    template_name = "auth/password_reset_form.html"

    def get(self, request, *args, **kwargs):
        form = PasswordResetForm()
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        if request.method == 'POST':
            form = PasswordResetForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Şifreniz başarıyla değiştirildi!')
                return redirect('password_reset_complete')
            else:
                return render(request, self.template_name, {
                    'errors': "Mevcut şifrenizi ve yeni şifrelerinizi doğru girdiğinizden emin olun!."
                })
        else:
            form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {
            'form': form
        })


class PasswordChangeView(LoginRequiredMixin, TemplateView):
    template_name = "auth/password_change_form.html"
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {
            'form': form
        })

    def post(self, request):
        if request.method == 'POST':
            # import ipdb; ipdb.set_trace()
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Şifreniz başarıyla değiştirildi!')
                return redirect('login')
            else:
                return render(request, self.template_name, {
                    'errors': [v for v in form.errors.values()][0]
                })
        else:
            form = PasswordChangeForm(request.user)
        return render(request, self.template_name, {
            'form': form
        })


class PasswordChangeSuccessView(LoginRequiredMixin, TemplateView):
    template_name = "auth/password_reset_complete.html"
    login_url = 'login'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'change_status': True
        })


class SignUpView(TemplateView):
    template_name = "auth/signup.html"
    login_url = 'login'

    def post(self, request, *args, **kwargs):
        form = SignupForm()
        if request.method == 'POST':
            form = SignupForm(request.POST)
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')

            if str(password1) != str(password2):
                return render(request, self.template_name,
                              {'register_error': 'Parolalar eşleşmiyor!'})

            if User.objects.filter(email=email).first():
                return render(request, self.template_name,
                              {'register_error': 'E-Mail adresiniz zaten sistemimizde kayıtlı!'})

            if form.is_valid():
                post = form.save(commit=False)
                post.username = email
                post.first_name = first_name
                post.last_name = last_name
                post.save()

                return redirect(self.login_url)

        return render(request, self.template_name, {'form': form})


class SignOutView(TemplateView):

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return redirect('login')


class SignInView(TemplateView):
    template_name = "auth/login.html"

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            UserModel = get_user_model()

            try:
                user = UserModel.objects.get(email=email)
                user = authenticate(username=user, password=password)
                if user:
                    if user.is_active:
                        login(request, user)
                        return redirect('home')
                    else:
                        return HttpResponse("Your account was inactive.")
                else:
                    return render(request, self.template_name,
                                  {'login_error': 'Bilgiler hatalı, lütfen tekrar deneyiniz!'})
            except Exception as error:
                return render(request, self.template_name,
                              {'login_error': '{} e-maili ile ilişkili kullanıcı bulunmamaktadır. Önce siteye kayıt olunuz! {}'.format(email, error)})

        else:
            return render(request, self.template_name, {})


class QuestionListView(LoginRequiredMixin, ListView):
    model = Questions
    template_name = "question_list.html"
    paginate_by = 10
    context_object_name = 'questions'


class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Questions
    template_name = "question_detail.html"
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        token, created = Token.objects.get_or_create(user=self.request.user)
        context['answers'] = Answers.objects.filter(question=kwargs['object'])
        context['token'] = token
        context['form'] = QuoteForm()
        return context


class HealthCheckView(TemplateView):
    template_name = "version.html"

    def get(self):
        return render(self.request, self.template_name, {'version': Version})
