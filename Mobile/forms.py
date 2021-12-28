from django import forms
from .models import MobileInformation
import re


class MobileForm(forms.ModelForm):
    class Meta:
        model = MobileInformation
        fields = ['Brand_Name', 'Model', 'Color', 'JAN_Code', 'Image']

    # def clean_Model(self):
    #     Model = self.cleaned_data.get('Model')
    #     for instance in MobileInformation.objects.all():
    #         if instance.Model == Model:
    #             raise forms.ValidationError(Model + ' Already exists ')
    #     return Model

    def clean_JAN_Code(self):
        JAN_Code = self.cleaned_data.get('JAN_Code')
        for instance in MobileInformation.objects.all():
            if instance.JAN_Code == JAN_Code:
                raise forms.ValidationError(JAN_Code + ' Already exists ')
        return JAN_Code

    def clean_Image(self):
        Image = self.cleaned_data.get('Image')
        results = re.findall(r'(?:http\:|https\:)?\/\/.*\.(?:png|jpg)', Image)
        if results:
            return Image
        else:
            raise forms.ValidationError('Invalid Image Url')


