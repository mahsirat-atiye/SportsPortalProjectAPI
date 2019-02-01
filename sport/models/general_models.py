from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

TYPE_CHOICES = (
    ('F', 'فوتبال'),
    ('B', 'بسکتبال')
)


class News(models.Model):
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default='F', verbose_name=_('نوع'))
    title = models.CharField(max_length=100, verbose_name=_('عنوان'))
    text = models.TextField(verbose_name=_('متن'))
    publish_date = models.DateField(verbose_name=_('تاریخ انتشار'))

    def __str__(self):
        s = self.title
        return s

    class Meta:
        verbose_name = _('خبر')
        verbose_name_plural = _('اخبار')
        # verbose_name_plural = "Pieces of news"


# tags and resources and related teams and related players were handled by many to many relationship

#     todo : images of non News

# recent news needed! during last 10/2 days


class Resource(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('نام'))
    news = models.ManyToManyField(News, verbose_name=_('خبر'))

    def __str__(self):
        s = self.name
        return s

    class Meta:
        verbose_name = _('منبع')
        verbose_name_plural = _('منابع')


#     many resources for many pieces of news!


class Tag(models.Model):
    text = models.CharField(max_length=100, verbose_name=_('متن'))
    news = models.ManyToManyField(News, verbose_name=_('خبر'))

    class Meta:
        verbose_name = _('تگ')
        verbose_name_plural = _('تگ ها')

    def __str__(self):
        s = self.text
        return s


#     many tags for many pieces of news!


class Comment(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('عنوان'))
    text = models.TextField(verbose_name=_('متن'))
    writer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('نویسنده'))
    news = models.ForeignKey(News, on_delete=models.CASCADE, verbose_name=_('خبر'))

    class Meta:
        verbose_name = _('نظر')
        verbose_name_plural = _('نظرات')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
                               label='نام کاربری',
                               required=True,
                               disabled=False,
                               help_text='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}),
                               label='رمز عبور',
                               required=True,
                               disabled=False,
                               help_text='')

    class Meta:
        model = User
        fields = ['username', 'password']


class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام کاربری'}),
                               label='نام کاربری',
                               required=True,
                               disabled=False,
                               help_text='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام'}),
                                 label='نام',
                                 required=True,
                                 disabled=False,
                                 help_text='')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی'}),
                                label='نام خانوادگی',
                                required=True,
                                disabled=False,
                                help_text='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'}),
                                label='رمز عبور',
                                required=True,
                                disabled=False,
                                help_text='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'}),
                                label='تکرار رمز عبور',
                                required=True,
                                disabled=False,
                                help_text='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'ایمیل'}),
                             label='ایمیل',
                             max_length=64,
                             help_text='یک ایمیل معتبر وارد کنید')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()
    # picture = models.ImageField(upload_to='static/profile_pictures', blank=True, null=True)
    # authentication_key = models.CharField(max_length=50)
    session_key = models.CharField(null=True, blank=True, max_length=160)
    authentication_key = models.CharField(null=True, blank=True, max_length=50)

# class FootballPlayerInGame(models.Model):
#     game = models.ForeignKey(Game, on_delete=models.CASCADE)
#     player = models.ForeignKey(Player,)
#


class ForgottenUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    key = models.TextField(max_length=32)


class ActivateUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    key = models.TextField(max_length=32)

