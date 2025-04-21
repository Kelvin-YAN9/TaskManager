from django import forms
from django.forms import ModelForm
from .models import Task,PRIORITY_CHOICES,PREDEFINED_CATEGORIES

class TaskForm(ModelForm):
    # 明确指定日期字段和输入格式
    created = forms.DateField(
        input_formats=['%m/%d/%Y'],  # 指定日期输入格式为 月/日/年
        widget=forms.DateInput(
            attrs={'class': 'form-control', 'placeholder': '月/日/年'}
        )
    )

    class Meta:
        model = Task
        fields = ('title', 'description', 'created', 'complete','priority','category')
        labels = {
            'title': '标题:',
            'description': '描述:',
            'created': '创建时间:',
            'complete': '完成状态:',
            'priority': '优先级:',
            'category': '分类:',
        }
        exclude = ['manager']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '任务标题'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '描述'}),
            'complete': forms.CheckboxInput(attrs={'class': 'mycheck my-3'}),
            # 添加优先级选择框
            'priority': forms.Select(choices=PRIORITY_CHOICES,attrs={'class': 'form-control'}),
            # 添加分类选择框
            'category': forms.Select(choices=PREDEFINED_CATEGORIES, attrs={'class': 'form-control'}),
        }

'''
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = TaskCategory.objects.filter(manager=user)
'''
'''
from django import forms
from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'created','complete')
        labels = {
            'title':'Title:',
            'description':'Description:',
            'created':'Created:',
            'complete':'Done:'
        }
        exclude = ['manager']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'任务标题'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'描述'}),
            'created': forms.DateInput(attrs={'class':'form-control', 'placeholder':'月/日/年'}),
            'complete':forms.CheckboxInput(attrs={'class':'mycheck my-3'}),
        }
        #we are converting this to modelform concept
        #complete the wigdets
        #change the type of date used
        #update the views 

'''