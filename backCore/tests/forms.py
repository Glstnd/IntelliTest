from django import forms
from django.forms.models import inlineformset_factory
from .models import Test, Module


ModuleFormSet = inlineformset_factory(Test,
                                      Module,
                                      fields=['title',
                                              'description'],
                                      extra=2,
                                      can_delete=True)
