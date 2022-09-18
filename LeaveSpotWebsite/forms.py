from django import forms  
class StudentForm(forms.Form):   
    file= forms.FileField(allow_empty_file=True,required=False, label="") # for creating file input  

