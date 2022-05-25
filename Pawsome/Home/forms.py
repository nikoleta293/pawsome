from django.forms import ModelForm
from Users.models import User
from Pet.models import Pet

class RegistrationForm(ModelForm):

    class Meta:
        model = User
        fields = '__all__'


    def clean_password(self):
        cleaned_data = self.cleaned_data
        password = cleaned_data.get('password')

        # check for min length
        min_length = 8
        if len(password) < min_length:
            msg = 'Password must be at least %s characters long.' %(str(min_length))
            self.add_error('password', msg)

        # check for digit
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password', msg)

        # check for uppercase letter
        if not any(c.isupper() for c in password):
            msg = 'Password must contain at least 1 uppercase letter.'
            self.add_error('password', msg)

        # check for lowercase letter
        if not any(c.islower() for c in password):
            msg = 'Password must contain at least 1 lowercase letter.'
            self.add_error('password', msg)

        password_confirm = cleaned_data.get('password_confirm')


        if password and password_confirm:
            if password != password_confirm:
                msg = "The two password fields must match."
                self.add_error('password_confirm', msg)
        return cleaned_data


    def __str__(self):
        field_values = []
        for field in self._meta.get_all_field_names():
            field_values.append(getattr(self, field, ''))
        return ' '.join(field_values)


class PetForm(ModelForm):

     class Meta:
        model = Pet
        fields = '__all__'



