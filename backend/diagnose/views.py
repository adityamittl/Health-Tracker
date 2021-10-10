from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.files.storage import FileSystemStorage
from .Disease_Diagnosis.util import heart_disease, diabetes,thyroid

def index(request):
    blood = request_blood.objects.filter(requester=request.user)
    context = {
        'blood':blood
    }
    return render(request,'index.html',context=context)

def diagnose(request):
    return render(request, 'diagnose.html')

def social_help(request):
    if request.method=='POST':
        if request.FILES['myfile']:
            data = request_blood()
            myfile = request.FILES['myfile']
            fs = FileSystemStorage(location='media/blood_request')
            filename = fs.save(myfile.name, myfile)
            hid = request.POST.get('Hid')
            data.hid = blood_bank.objects.get(id = hid)
            data.prescription = filename
            data.requester = request.user
            data.unit = request.POST.get('quantity') 
            data.save()
            print(data)
            return redirect('dashboard')
    blood = blood_bank.objects.all()
    context = {
        'blood':blood
    }
    return render(request, 'social-help.html',context=context)

def blog(request):
    return render(request,'blog.html')

'''
Input Features-

Pregnancies - number of times person has been pregnant
Glucose - glucose levels in Hg 
BloodPressure - blood pressure in mm hg
SkinThickness - skin thickness in mm
Insulin - insulin levels in mIU/L
BMI - Body Mass Index in Kg/m2
DiabetesPedigreeFunction - likelihood of diabetes based on family history
Age - age in years

sample input = [1, 89, 66, 23, 94, 28.1, 0.167, 21]
'''

def diabetesr(request):
    if request.method=='POST':
        pragnancies = request.POST.get('prag')
        glucose = request.POST.get('glucose')
        bp = request.POST.get('bp')
        skinthickness = request.POST.get('skinthick')
        insulin = request.POST.get('insulin')
        bmi = request.POST.get('bmi')
        dpf = request.POST.get('DPF')
        age = request.POST.get('age')
        res = diabetes([pragnancies,glucose,bp,skinthickness,insulin,bmi,dpf,age])
        context={
            'data':res
        }
        return render(request,'diabetes.html',context=context)
    return render(request,'diabetes.html')

'''
Input Features-

Age - age in years
Sex - (1 = male, 0 = female)
On_thyroxine - (1 = yes, 0 = no)
Query_on_thyroxine - (1 = yes, 0 = no)
On_antithyroid_medication - (1 = yes, 0 = no)
Sick - (1 = yes, 0 = no)
Pregnant - (1 = yes, 0 = no)
Thyroid_surgery - (1 = yes, 0 = no)
I131_treatment - (1 = yes, 0 = no)
Query_hypothyroid - (1 = yes, 0 = no)
Query_hyperthyroid - (1 = yes, 0 = no)
Lithium - (1 = yes, 0 = no)
Goiter - (1 = yes, 0 = no)
Tumor - (1 = yes, 0 = no)
Hypopituitary - (1 = yes, 0 = no)
Psych - (1 = yes, 0 = no)
TSH - TSH levels in mIU/mL
T3 - T3 levels in pg/dl
TT4 - TT4 levels in ng/dl
T4U - Thyroxine Utilization Rates
FTI - Free Thyroxine Index

sample input = [24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.00025,0.03,0.143,0.133,0.108]
'''

def thyroism(request):
    if request.method=='POST':
        Age = int(request.POST.get('age'))
        Sex = int(request.POST.get('sex'))
        On_thyroxine = int(request.POST.get('On_thyroxine'))
        Query_on_thyroxine = int(request.POST.get('Query_on_thyroxine'))
        On_antithyroid_medication = int(request.POST.get('On_antithyroid_medication'))
        Sick = int(request.POST.get('Sick'))
        Pregnant = int(request.POST.get('Pregnant'))
        Thyroid_surgery = int(request.POST.get('Thyroid_surgery'))
        I131_treatment = int(request.POST.get('I131_treatment'))
        Query_hypothyroid = int(request.POST.get('Query_hypothyroid'))
        Query_hyperthyroid = int(request.POST.get('Query_hyperthyroid'))
        Lithium = int(request.POST.get('Lithium'))
        Goiter = int(request.POST.get('Goiter'))
        Tumor = int(request.POST.get('Tumor'))
        Hypopituitary = int(request.POST.get('Hypopituitary'))
        Psych = int(request.POST.get('Psych'))
        TSHh = float(request.POST.get('TSH'))
        T3 = float(request.POST.get('T3'))
        TT4h = float(request.POST.get('TT4'))
        T4Uh = float(request.POST.get('T4U'))
        FTIh = float(request.POST.get('FTI'))
        res = thyroid([Age,Sex,On_thyroxine,Query_on_thyroxine,On_antithyroid_medication,Sick,Pregnant,Thyroid_surgery,I131_treatment,Query_hypothyroid,Query_hyperthyroid,Lithium,Goiter,Tumor,Hypopituitary,Psych,TSHh,T3,TT4h,T4Uh,FTIh])
        context ={
            'data':res
        }
        return render(request,'thyroidismDetection.html',context=context)
    return render(request,'thyroidismDetection.html')

'''
Input Features-

age - age in years
sex - (1 = male, 0 = female)
cp - chest pain type (0 = No pain, 1 = low, 2 = moderate, 3 = Severe)
trestbps - resting blood pressure (in mm Hg)
chol - serum cholestoral in mg/dl
fbs - fasting blood sugar (1 = greator that 120 mg/dl; 0 = lesser that 120 mg/dl)
restecg - resting electrocardiographic results (0=normal, 1=ST-T wave abnormality, 2=left ventricular hypertrophy)
thalach - maximum heart rate achieved
exang - exercise induced angina (1 = yes, 0 = no)
oldpeak - ST depression induced by exercise relative to rest
slope - the slope of the peak exercise ST segment (0=upsloping, 1=flat, 2=downsloping)
ca - number of major vessels (0-3) colored by flourosopy
thal - (1 = normal; 2 = fixed defect; 3 = reversable defect)

sample input = [63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]
'''

def heartdis(request):
    if request.method=='POST':
        Age = request.POST.get('Age')
        cp = request.POST.get('cp')
        Sex = request.POST.get('Sex')
        thalach = request.POST.get('thalach')
        Treshbps = request.POST.get('Treshbps')
        exang = request.POST.get('exang')
        Chol = request.POST.get('Chol')
        oldpeak = request.POST.get('oldpeak')
        Fbs = request.POST.get('Fbs')
        ca = request.POST.get('ca')
        Restecg = request.POST.get('Restecg')
        thal = request.POST.get('thal')
        slope = request.POST.get('slope')
        res = heart_disease([Age,Sex,cp,Treshbps,Chol,Fbs,Restecg,thalach,exang,oldpeak,slope,ca,thal])
        context ={
            'data':res
        }
        return render(request,'heartDetection.html',context=context)
    return render(request,'heartDetection.html')