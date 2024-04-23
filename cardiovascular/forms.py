
from django import forms

class CardiovascularForm(forms.Form):
    age = forms.IntegerField(label='Age', required=True)
    sex = forms.ChoiceField(label='Sex', choices=[(0, 'Male'),(1, 'Female')], required=True)
    chestPain = forms.ChoiceField(label='Chest Pain Type', choices=[(3, 'Typical Angina'),(0, 'Atypical Angina'),(1, 'Non-Anginal Pain'),(2, 'Asymptomatic')], required=True)
    restingBP = forms.IntegerField(label='Resting Blood Pressure', required=True)
    cholesterol = forms.IntegerField(label='Cholesterol', required=True)
    fastingBS = forms.IntegerField(label='Fasting Blood Sugar', required=True)
    restingECG = forms.ChoiceField(label='Resting ECG', choices=[(0, 'Normal'),(1, 'ST-T Wave Abnormality'),(2, 'Left Ventricular Hypertrophy')], required=True)
    maxHR = forms.IntegerField(label='Maximum Heart Rate', required=True)
    exerciseAngina = forms.ChoiceField(label='Exercise Induced Angina', choices=[(0, 'No'),(1, 'Yes')], required=True)
    oldPeak = forms.FloatField(label='Old Peak', required=True)
    STslope = forms.ChoiceField(label='ST Slope', choices=[(0, 'Upsloping'),(1, 'Flat'),(2, 'Downsloping')], required=True)
