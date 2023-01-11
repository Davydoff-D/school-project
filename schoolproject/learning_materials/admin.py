from django.contrib import admin

from .models import Group, Material, Question, AnswerModel
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget


class QuestionAdminForm(forms.ModelForm):
    question_text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Question
        fields = '__all__'


class MaterialAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Material
        fields = '__all__'


class AnswerAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = AnswerModel
        fields = '__all__'


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'group',)
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    form = MaterialAdminForm
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    empty_value_display = '-пусто-'


class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    search_fields = ('question_text',)
    empty_value_display = '-пусто-'


class AnswerAdmin(admin.ModelAdmin):
    form = AnswerAdminForm
    search_fields = ('text',)
    empty_value_display = '-пусто-'


admin.site.register(Material, MaterialAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(AnswerModel, AnswerAdmin)
