from django import forms 
from .models import User_detail ,Query_Doubt

class UserForm(forms.ModelForm):
 class Meta:
        model = User_detail
        #fields = ['member_id',password,name]
        fields = '__all__'
        exclude=["date"]
        
        widgets = {
           
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
           
            'about_user': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter About your self', 'rows': 3}),
           
            'user_cv': forms.FileInput(attrs={'class': 'form-control', 'required': True}),
        
        }

class UserQuery(forms.ModelForm):
    class Meta:
        model=Query_Doubt
        fields = '__all__'
        exclude=["member_id","answer","question_date","answer_date"] 

        widgets= {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name',}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Subject'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'question': forms.Textarea(attrs={'class': 'form-control','placeholder':'Ask your Questions','rows':3}),
            
            # 'question_date': forms.DateField(),
            # 'answer_date': forms.DateField(),

        }
        
   




        


