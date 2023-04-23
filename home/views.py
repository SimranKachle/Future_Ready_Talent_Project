from django.shortcuts import render; 
from home.models import Contact
from django. contrib import messages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np 

# def home(request):
#     return render(request,'home.html')

# def predict(request):
#     return render(request,'predict.html')

# def home2(request):
#     return render(request,'home2.html')
def home3(request):
    return render(request,'home3.html')

def result(request):
    data = pd.read_csv("static/diabetes.csv")
    X = data.drop("Outcome",axis=1)
    Y= data['Outcome']
    X_train,X_test,Y_train,Y_test =train_test_split(X,Y,test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train,Y_train)
    
    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])
    var6 = float(request.GET['n6'])
    var7 = float(request.GET['n7'])
    var8 = float(request.GET['n8'])
    
    pred = model.predict(np.array([var1,var2,var3,var4,var5,var6,var7,var8]).reshape(1,-1))
    
    result1=""
    
    if pred==[1]:
        result1="Positive : Based on the information you provided, our diabetes risk assessment tool has identified that you have a higher risk of developing diabetes! "
    else:
        result1="Negative : Based on the information you provided, our diabetes risk assessment tool has identified that you have a lower risk of developing diabetes!"
    
    
    return render(request,'home3.html',{"result2":result1})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email') 
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject = subject, message=message)
        contact.save()
        messages.success(request,'Message sent Successfully!')
    return render(request,'home3.html')