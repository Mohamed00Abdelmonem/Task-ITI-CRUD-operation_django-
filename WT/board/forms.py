from django import forms
from .models import car


class CAR(forms.ModelForm):
    class Meta:
        model = car
        fields = '__all__'

#
# class Lesson_Form(forms.ModelForm):
#     class Meta:
#         model = Lesson
#         fields = '__all__'
#
#
# class Comment(forms.ModelForm):
#     class Meta:
#         model = Comment_stu
#         fields = '__all__'
