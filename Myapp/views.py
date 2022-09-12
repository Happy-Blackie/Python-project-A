from calendar import month
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from . models import Payment_Table
from django.http import HttpResponse

        #For CSV
import csv

        #For PDF
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

import calendar
from calendar import HTMLCalendar



# Create your views here.

#Generate Textfile Payment List
def payment_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=payments.txt'

    #Designate the Model
    payments = Payment_Table.objects.all()

    #Create blank list
    lines = []

    #Loop through the model
    for payment in payments:
        lines.append(f'Name: {payment.Fname}\r\nTelophone: {payment. Phone_Number}\r\nDate:{payment.Date}\r\nAmount Piad: {payment.Amount_Paid}\r\n\r\n')
                        

    #lines = ['This is line 1\n',
            #'This is line 2\n',
            #'This is line 2\n',]

    #Write to textfile
    response.writelines(lines)
    return response



#Generate CSV File Payment List
def payment_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=payments.csv'

    #Create a CSV writer
    writer = csv.writer(response)

    #Designate the Model
    payments = Payment_Table.objects.all()

     #Add column headings to csv file
    writer.writerow(['Customers Name', 'Phone Number', 'Date', 'Amount Paid'])

    #Loop through the model
    for payment in payments:
         writer.writerow([payment.Fname, payment. Phone_Number, payment.Date, payment.Amount_Paid])                      
    return response




#Generate PDF File Payment List
def payment_pdf(request):
    # Create Bytestream buffer
    buf = io.BytesIO()

    #Create a canvas
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    #Create a text object
    textobj = c.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    #Add some lines of text
    #lines = [
        #"This is line 1\n"
        #"This is line 2\n"
        #"This is line 3\n"
    #]

    #Designate the Model
    payments = Payment_Table.objects.all()

     #Create blank list
    lines = []
    for payment in payments:
        lines.append(f'Name: {payment.Fname}') 
        lines.append(f'Telephone: {payment.Phone_Number}')
        lines.append(f'Date: {payment.Date}')
        lines.append(f'Amount paid: {payment.Amount_Paid}')
        lines.append("***************")

    #Loop
    for line in lines:
        textobj.textLine(line)

    #Finish up
    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)

    #Return something
    return FileResponse(buf,as_attachment=True,filename='payments.pdf')





def register_function(request):
    if request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

def login_function(request):
    if request.user.is_authenticated:
        return render(request, 'home_login.html')
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_login') 
        else:
            msg = 'Error Login(check your entry please)'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def home_function(request):
    return render(request,'home_register.html')

def home_login_function(request):
    return render(request,'home_login.html')

def calendar(request):
    
    return render(request,'calendar.html')


def signout(request):
    logout(request)
    return redirect('/')

def home_page_function(request):
    return render(request,'home_page.html')

def payments(request):
    if request.method == 'POST':
        fullname = request.POST['fname']
        phonenumber = request.POST['pnumber']
        date = request.POST['dte']
        amount = request.POST['amnt']
        if len(phonenumber) == 0:
            return redirect('payments')
        
        elif Payment_Table.objects.filter( Phone_Number=phonenumber).exists():
            messages.info(request,'Phone number already exist')
            return redirect('payments')
        else:
            records = Payment_Table(Fname=fullname,Phone_Number=phonenumber,
                                Date=date,Amount_Paid=amount)
            messages.info(request,'Payments Records  are already  sent to database')
            records.save()
              
            
    return render(request,'payments.html')

#extracting data from database models and displaying on webpage
def payrecords_function(request):
    allrecords = Payment_Table.objects.all()
    return render(request,'pay_records.html',{'all':allrecords})