from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'input-txt','placeholder': 'Username or Email'}), max_length = 50)
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'input-txt'}), max_length = 50)

    def is_valid(self):
        return True

class SignUpForm(forms.Form):
    username = forms.CharField(label = '', widget=forms.TextInput(attrs={'class': 'input-txt', 'placeholder':'Username'}), max_length = 50)
    email = forms.CharField(label = '', widget=forms.TextInput(attrs={'class': 'input-txt', 'placeholder':'Email'}), max_length = 50)

    password = forms.CharField(min_length = 8, label = '', widget=forms.PasswordInput(attrs={'class': 'input-txt', 'placeholder':'Password'}), max_length = 50)
    cfmPassword = forms.CharField(min_length = 8, label = '', widget=forms.PasswordInput(attrs={'class': 'input-txt', 'placeholder':'Confirm Password'}), max_length = 50)

    def is_valid(self):
        return True