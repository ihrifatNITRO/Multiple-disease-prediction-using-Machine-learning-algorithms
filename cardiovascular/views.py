import re
from django.shortcuts import render
from .forms import CardiovascularForm
import joblib


# Create your views here.
def cvd(request):
    return render(request, 'cardiovascular/cvd.html')

def result(request):

    # Load the pridiction model
    cls = joblib.load('cardiovascular/cvd_model.sav')

    input_data = []
    feature_name_form = ['age','sex','chestPain','restingBP','cholesterol','fastingBS',
                         'restingECG','maxHR','exerciseAngina','oldPeak','STslope']
                         
    feature_name = ['Age', 'Sex', 'Chest Pain Type', 'Resting Blood Pressure', 
                    'Cholesterol', 'Fasting Blood Sugar', 'Resting ECG',
                    'Maximum Heart Rate', 'Exercise Induced Angina', 'Old Peak', 'ST Slope']

    for i in feature_name_form:
        input_data.append(int(request.GET[i]))
        

    zipp = zip(feature_name, input_data)
    # Make prediction
    result = cls.predict([input_data])

    return render(request, 'cardiovascular/result.html', {'input_data': input_data, 'zipp': zipp, 'result': result})

