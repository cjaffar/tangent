from django import forms

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class LeaveForm(forms.Form):
	leave_from=forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))
	leave_to=forms.DateField(widget=forms.SelectDateWidget(empty_label="Nothing"))