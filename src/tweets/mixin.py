from django import forms
from django.forms.utils import ErrorList


class FormUserNeededMixin(object):
     def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FormUserNeededMixin, self).form_valid(form)

    #this code i believe is out-of-date 
    #  self.request.user.is_authenticated() isnt seen as a bool type
    # this method checks if see if user is auth before sending tweet
    # if not it tells them that theu must sign in before tweeting

     '''def form_valid(self, form):
        if self.request.user.is_authenticated():
            form.instance.user = self.request.user
            return super(FormUserNeededMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["User must be logged in to continue"])
            return self.form_invalid(form) '''

class UserOwnerMixin(FormUserNeededMixin, object):
    def form_valid(self, form):
        if form.instance.user == self.request.user:
            return super(UserOwnerMixin, self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS] = ErrorList(["This User is not allowed to change this data"])
            return self.form_invalid(form)