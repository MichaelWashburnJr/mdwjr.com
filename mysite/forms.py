"""
File:		mysite/forms.py
Language: Python 2 with Django 1.6 Web Framework

Author: Michael D Washburn Jr <mdw7326@rit.edu>

Description: Form definitions for various views
"""

from django import forms
import re
from django.core.mail import send_mail

"""
Form to send an email to me.
"""
class ContactForm(forms.Form):
	sender = forms.EmailField(help_text="Valid email address required.", label="Your Email Address");
	subject = forms.CharField(max_length=100, help_text="100 characters max.");
	message = forms.CharField(widget=forms.Textarea);
	
	"""
	Sends the email
	"""
	def send_email(self):
		send_mail(self.cleaned_data["subject"], self.cleaned_data["message"], self.cleaned_data["sender"], ["mdw7326@rit.edu"]);

	"""
	Validates the data
	"""
	def clean(self):
		cleaned_data = super(ContactForm, self).clean();
		#get cleaned data
		sender = cleaned_data.get("sender");
		subject = cleaned_data.get("subject");
		message = cleaned_data.get("message");
		#check sender email
		if not sender:
			msg = u"Please enter your email address.";
			self._errors["sender"] = self.error_class([msg]);
		#check subject
		if not subject:
			msg = u"Please enter a message subject.";
			self._errors["subject"] = self.error_class([msg]);
		#check message
		if not message:
			msg = u"Please enter a message.";
			self._errors["message"] = self.error_class([msg]);

		return cleaned_data;
