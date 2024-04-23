from django.shortcuts import render
import joblib

# Create your views here.
def breast_cancer(request):
    return render(request, 'breast_cancer/breast_cancer.html')

def result(request):

    # Load the pridiction model
    cls = joblib.load('breast_cancer/breast_cancer.sav')

    input_data = []
    feature_name_form = ["clump_thickness","uniformity_of_cell_size","marginal_adhesion",
                     "single_epithelial_cell_size","bare_nuclei","bland_chromatin",
                     "normal_nucleoli","mitoses"]
    
    feature_name = ['Clump Thickness','Uniformity of Cell Size','Marginal Adhesion',
                    'Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin',
                    'Normal Nucleoli','Mitoses']

    for i in feature_name_form:
        input_data.append(int(request.GET[i]))


    zipp = zip(feature_name, input_data)
    # Make prediction
    result = cls.predict([input_data])


    return render(request, 'breast_cancer/result.html', {'input_data': input_data, 'zipp': zipp, 'result': result})