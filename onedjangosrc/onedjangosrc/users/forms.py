from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm, UserChangeForm as BaseUserChangeForm

from .models import User


class UserCreationForm(BaseUserCreationForm):

    class Meta:
        model = User
        # Doesn't affect Admin Panel, since there `UserAdmin`.`add_fieldsets` takes precedence over `fields`.
        fields = ('email', 'date_of_birth')


class UserChangeForm(BaseUserChangeForm):

    class Meta:
        model = User
        fields = '__all__'
