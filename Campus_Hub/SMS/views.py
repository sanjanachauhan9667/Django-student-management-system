from django.shortcuts import render , redirect
from .models import StudentRecord
from django.contrib import messages

# Create your views here.

# Home --------------------------------------------------------------------------------
def home(request):
    return render(request,'SMS/home.html')

# Insert ------------------------------------------------------------------------------
def insert_record(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        course = request.POST.get('course')
    
        StudentRecord.objects.create(name=name, age=age, gender=gender, course=course)
    
        messages.success(request,"Record Inserted SucessFully!")
        return redirect ('insert')
    

    return render(request,'SMS/insert.html')

# Search -----------------------------------------------------------------------------
def search_record(request):
    student = []
    message = ''

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'Search':
            student_id = request.POST.get('id')

            if student_id:
                student = StudentRecord.objects.filter(id = student_id)

                if student:
                    message = 'Record Found!'
                else:
                    message = 'Record Not Found!'

            else:
                message = 'Invalid Id! Enter Correct ID'

        elif action == 'Search_All':
            student = StudentRecord.objects.all()
            message = 'List Of Students:'

    return render(request,'SMS/search.html',{'student':student, 'message':message})

# Update ---------------------------------------------------------------------------------

def update_record(request):

    if request.method == 'POST':
        student_id = request.POST.get('id')
        
        if not student_id:
            messages.error(request,'Enter Student ID')
            return redirect ('update')
        
        try:
            record = StudentRecord.objects.get(id = student_id)

            name = request.POST.get('name')
            age = request.POST.get('age')
            gender = request.POST.get('gender')
            course = request.POST.get('course')

            if name:
                record.name = name    
            if age:
                record.age = age     
            if gender:
                record.gender = gender
            if course:
                record.course = course  

            record.save()
            messages.success(request,"Record Updated SuccessFully!")   

        except StudentRecord.DoesNotExist:
            messages.error(request,"Student not Found!")   
        return redirect('update')   

    return render(request,'SMS/update.html')     

# delete ----------------------------------------------------------------------------------
def delete_record(request):

        students = []
        message = ''

        if request.method == 'POST':
            action = request.POST.get('action')

            if action == 'delete':
                    student_id = request.POST.get('id')

                    if not student_id:
                        message = 'Please Enter Student Id' 
                    else:
                        try:
                            students = StudentRecord.objects.get(id = student_id)
                            students.delete()
                            message = 'Student Deleted SuccessFully!'
                
                        except:
                            message = 'Invalid Student ID!'
                    
                    students = StudentRecord.objects.all()

            elif action == 'delete_all':
                StudentRecord.objects.all().delete()
                students = []
                message = 'All Students Deleted SuccessFully!'
        
        return render(request,'SMS/delete.html',{'students':students ,'message':message})

    


    
                                                                                             

            

        
            

        
            
