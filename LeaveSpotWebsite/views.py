from django.shortcuts import render,redirect
from .models import InsertCoordinator,InsertStudent, InsertStudentLeave
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse  
from LeaveSpotWebsite.functions.functions import handle_uploaded_file  
from .forms import StudentForm  



# Create your views here.

def index(request):
    return render(request,"index.html")

def Logout(request):
    auth.logout(request)
    return redirect('index')

def createAdmin(request):
    userId = "admin"
    Password = "ankit123"
    user = User.objects.create_user(username=userId, password=Password)
    user.save()
    print(HttpResponse("Admin Created Successfully"))

def adminLogin(request):
    if request.method == 'POST':
        Id = request.POST['AdminId']
        Password = request.POST['Password']
        user = auth.authenticate(username = Id, password = Password)

        if user is not None:
            auth.login(request, user)
            coordinatorData = InsertCoordinator.objects.all().count()
            studentData = InsertStudent.objects.all().count()
            studentleaveCount = InsertStudentLeave.objects.all().count()
            approvedLeavesCount = InsertStudentLeave.objects.filter(Status='Approved').count()
            return render(request,"Admin/dashboard.html",{'coordinatorData': coordinatorData, 'studentData': studentData, 'studentleaveCount': studentleaveCount, 'approvedLeavesCount': approvedLeavesCount})
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect("admin")
    else:
        return render(request,'admin')

def admin(request):
    return render(request,"Admin/index.html")

def adminDashboard(request):
    coordinatorData = InsertCoordinator.objects.all().count()
    studentData = InsertStudent.objects.all().count()
    studentleaveCount = InsertStudentLeave.objects.all().count()
    approvedLeavesCount = InsertStudentLeave.objects.filter(Status='Approved').count()
    return render(request,"Admin/dashboard.html",{'coordinatorData': coordinatorData, 'studentData': studentData, 'studentleaveCount': studentleaveCount, 'approvedLeavesCount': approvedLeavesCount})

def coordinatorProfile(request):
    coordinatorData = InsertCoordinator.objects.all()
    return render(request,"Admin/Coordinator_Profile.html",{'coordinatorData': coordinatorData} )

def InsertCoordinatorDetail(request):
    if request.method == 'POST':
        if request.POST.get('Name') and request.POST.get('Course') and request.POST.get('Semester') and request.POST.get('Section') and request.POST.get('Email_Id') and request.POST.get('Password'):
            saverecord = InsertCoordinator()
            saverecord.Name = request.POST.get('Name')
            saverecord.Course = request.POST.get('Course')
            saverecord.Semester = request.POST.get('Semester')
            saverecord.Section = request.POST.get('Section')
            saverecord.Email_Id = request.POST.get('Email_Id')
            saverecord.Password = request.POST.get('Password')
            saverecord.save()
            if User.objects.filter(username=saverecord.Email_Id).exists():
                messages.success(request,"User is already added. Record Saved Successfully....")
                coordinatorData = InsertCoordinator.objects.all()
                return render(request, 'Admin/Coordinator_Profile.html', {'coordinatorData': coordinatorData})
            else:
                user = User.objects.create_user(username=saverecord.Email_Id, password=saverecord.Password)
                user.save()
                messages.success(request,"Record Saved Successfully....")
                coordinatorData = InsertCoordinator.objects.all()
                return render(request, 'Admin/Coordinator_Profile.html', {'coordinatorData': coordinatorData})
    else:
        return render(request, 'Admin/Coordinator_Profile.html')

def coordinatorProfileUpdate(request):
    user_id = request.POST.get('UpdateId')
    UpdateProfile = InsertCoordinator.objects.get(pk = user_id)
    return render(request,"Admin/Coordinator_Update.html", {"user_id": UpdateProfile})

def UpdateCoordinator(request,id):
    Name = request.POST.get('Name')
    Course = request.POST.get('Course')
    Semester = request.POST.get('Semester')
    Section = request.POST.get('Section')
    Email_Id = request.POST.get('Email_Id')
    Password = request.POST.get('Password')
    updatestatus = InsertCoordinator.objects.filter(id=id).update(Name=Name, Course=Course, Semester=Semester, Section = Section, Email_Id= Email_Id, Password=Password)
    if updatestatus==1:
        userupdate = User.objects.get(username=Email_Id)
        userupdate.set_password(Password)
        userupdate.save() 
        messages.success(request,'Record Updated Successfully')
        coordinatorData = InsertCoordinator.objects.all()
        return render(request,"Admin/Coordinator_Profile.html",{'coordinatorData': coordinatorData})

def DeleteCoordinator(request):
    id = request.POST.get('DeleteId')
    Email_Id = request.POST.get('DeleteEmail')
    deletestatus = InsertCoordinator.objects.filter(Id=id).delete()
    if deletestatus!="":
        userstatus = User.objects.get(username=Email_Id).delete()
        if userstatus!="":
            messages.success(request,'Record Deleted Successfully')
            coordinatorData = InsertCoordinator.objects.all()
            return render(request,"Admin/Coordinator_Profile.html",{'coordinatorData': coordinatorData})

def studentProfile(request):
    studentData = InsertStudent.objects.all()
    return render(request,"Admin/Student_Profile.html",{'studentData': studentData})

def InsertStudentDetail(request):
    if request.method == 'POST':
        if request.POST.get('Name') and request.POST.get('Id') and request.POST.get('Semester') and request.POST.get('Course') and request.POST.get('Section') and request.POST.get('Email_Id') and request.POST.get('Password'):
            saverecord = InsertStudent()
            saverecord.Name = request.POST.get('Name')
            saverecord.Id = request.POST.get('Id')
            saverecord.Course = request.POST.get('Course')
            saverecord.Semester = request.POST.get('Semester')
            saverecord.Section = request.POST.get('Section')
            saverecord.Email_Id = request.POST.get('Email_Id')
            saverecord.Password = request.POST.get('Password')
            saverecord.save()
            if User.objects.filter(username=saverecord.Id).exists():
                messages.success(request,"User is already added. Record Saved Successfully....")
                studentData = InsertStudent.objects.all()
                return render(request, 'Admin/Student_Profile.html', {'studentData': studentData})
            else:
                user = User.objects.create_user(username=saverecord.Id, password=saverecord.Password)
                user.save()
                studentData = InsertStudent.objects.all()
                messages.success(request,"Record Saved Successfully....")
                return render(request, 'Admin/Student_Profile.html',{'studentData': studentData})
    else:
        return render(request, 'Admin/Student_Profile.html')

def studentProfileUpdate(request):
    user_id = request.POST.get('UpdateId')
    UpdateProfile = InsertStudent.objects.get(pk = user_id)
    return render(request,"Admin/Student_Update.html",{'user_id':UpdateProfile})

def UpdateStudent(request,id):
    Name = request.POST.get('Name')
    Course = request.POST.get('Course')
    Semester = request.POST.get('Semester')
    Section = request.POST.get('Section')
    Email_Id = request.POST.get('Email_Id')
    Password = request.POST.get('Password')
    updatestatus = InsertStudent.objects.filter(Id=id).update(Name=Name, Course=Course, Semester=Semester, Section = Section, Email_Id= Email_Id, Password=Password)
    if updatestatus==1:
        userupdate = User.objects.get(username=id)
        userupdate.set_password(Password)
        userupdate.save() 
        messages.success(request,'Record Updated Successfully')
        studentData = InsertStudent.objects.all()
        return render(request,"Admin/Student_Profile.html",{'studentData': studentData})

def DeleteStudent(request):
    id = request.POST.get('DeleteId')
    deletestatus = InsertStudent.objects.filter(Id=id).delete()
    if deletestatus!="":
        userstatus = User.objects.get(username=id).delete()
        if userstatus!="":
            messages.success(request,'Record Deleted Successfully')
            studentData = InsertStudent.objects.all()
            return render(request,"Admin/Student_Profile.html",{'studentData': studentData})

def StudentLogin(request):
    return render(request,"Login/Student_Login.html")

def studentLogin(request):
    if request.method == 'POST':
        Id = request.POST['Id']
        Password = request.POST['Password']
        user = auth.authenticate(username = Id, password = Password)

        if user is not None:
            auth.login(request, user)
            studentData =  InsertStudent.objects.get(pk = Id)
            coordinatorData = InsertCoordinator.objects.get(Course=studentData.Course, Section=studentData.Section)
            return render(request,"Student/Student_Portal.html",{'studentData':studentData,'coordinatorData': coordinatorData})
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect("StudentLogin")
    else:
        return render(request,'StudentLogin')

def StudentLogin1(request):
    return render(request,"Student_Login.html")

def studentPortal(request):
    current_user = request.user
    Id = current_user.username
    studentData =  InsertStudent.objects.get(pk = Id)
    coordinatorData = InsertCoordinator.objects.get(Course=studentData.Course, Semester = studentData.Semester, Section=studentData.Section)
    return render(request,"Student/Student_Portal.html",{'studentData':studentData,'coordinatorData': coordinatorData})

def ApplyLeave(request):
    current_user = request.user
    Id = current_user.username
    studentData =  InsertStudent.objects.get(pk = Id)
    coordinatorData = InsertCoordinator.objects.get(Course=studentData.Course, Section=studentData.Section)
    student = StudentForm()
    return render(request,"Student/Apply_Leave.html",{'studentData':studentData,'coordinatorData': coordinatorData,'form':student})

def LeaveApplication(request):
    current_user = request.user
    Id = current_user.username
    if request.method == 'POST':
        if request.POST.get('Name') and request.POST.get('Id') and request.POST.get('Course') and request.POST.get('Semester') and request.POST.get('Section') and request.POST.get('No_of_Leaves') and request.POST.get('Reason') and request.POST.get('Dated') and request.POST.get('Doc_Req'):
            saverecord = InsertStudentLeave()
            saverecord.Id = request.POST.get('Id')
            saverecord.Name = request.POST.get('Name')
            saverecord.Course = request.POST.get('Course')
            saverecord.Semester = request.POST.get('Semester')
            saverecord.Section = request.POST.get('Section')
            saverecord.No_of_Leaves = request.POST.get('No_of_Leaves')
            saverecord.Reason = request.POST.get('Reason')
            saverecord.Dated = request.POST.get('Dated')
            saverecord.Doc_Req = request.POST.get('Doc_Req')
            saverecord.Status = "Pending"
            saverecord.save()
            student = StudentForm()
            messages.success(request,"Leave Applied Successfully....")
            studentData =  InsertStudent.objects.get(pk = Id)
            coordinatorData = InsertCoordinator.objects.get(Course=studentData.Course, Section=studentData.Section)
            return render(request, 'Student/Apply_Leave.html',{'studentData': studentData,'coordinatorData': coordinatorData,'form':student})
    else:
        messages.success(request,"Leave Not Applied Successfully....")
        student = StudentForm()
        studentData =  InsertStudent.objects.get(pk = Id)
        coordinatorData = InsertCoordinator.objects.get(Course=studentData.Course, Section=studentData.Section)
        return render(request, 'Student/Apply_Leave.html',{'studentData': studentData,'coordinatorData': coordinatorData,'form':student})

def LeaveApplicationStatus(request):
    current_user = request.user
    Id = current_user.username
    studentData =  InsertStudent.objects.get(pk = Id)
    studentLeaveData =  InsertStudentLeave.objects.filter(id = Id)
    coordinatorData = InsertCoordinator.objects.get(Course=studentData.Course, Section=studentData.Section)
    return render(request,"Student/Application_Status.html",{'studentData':studentData,'coordinatorData': coordinatorData, 'studentLeaveData': studentLeaveData})

def CoordinatorLogin(request):
    return render(request,"Login/Coordinator_Login.html")

def coordinatorLogin(request):
    if request.method == 'POST':
        Id = request.POST['Id']
        Password = request.POST['Password']
        user = auth.authenticate(username = Id, password = Password)

        if user is not None:
            auth.login(request, user)
            return redirect("coordinatorPortal")
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect("CoordinatorLogin")
    else:
        return render(request,'CoordinatorLogin')

def CoordinatorLogin1(request):
    return render(request,"Coordinator_Login.html")

def coordinatorPortal(request):
    return render(request,"Coordinator/Coordinator_Portal.html")

def TrackStatus(request):
    current_user = request.user
    Id = current_user.username
    coordinatorData = InsertCoordinator.objects.get(Email_Id=Id)
    studentData =  InsertStudent.objects.filter(Course=coordinatorData.Course,Semester = coordinatorData.Semester, Section=coordinatorData.Section)
    studentLeaveData =  InsertStudentLeave.objects.filter(Course=coordinatorData.Course, Semester = coordinatorData.Semester, Section=coordinatorData.Section)
    return render(request,"Coordinator/Track_Status.html",{'studentData':studentData,'coordinatorData': coordinatorData, 'studentLeaveData': studentLeaveData})

def ApproveReject(request):
    current_user = request.user
    Id = current_user.username
    coordinatorData = InsertCoordinator.objects.get(Email_Id=Id)
    studentLeaveApproved =  InsertStudentLeave.objects.filter(Course=coordinatorData.Course, Semester = coordinatorData.Semester, Section=coordinatorData.Section, Status="Approved")
    studentLeaveRejected =  InsertStudentLeave.objects.filter(Course=coordinatorData.Course, Semester = coordinatorData.Semester, Section=coordinatorData.Section, Status="Rejected")
    studentLeavePending =  InsertStudentLeave.objects.filter(Course=coordinatorData.Course, Semester = coordinatorData.Semester, Section=coordinatorData.Section, Status="Pending")
    return render(request,"Coordinator/Appr_Rejct.html",{'studentLeaveApproved':studentLeaveApproved,'coordinatorData': coordinatorData, 'studentLeavePending': studentLeavePending,'studentLeaveRejected':studentLeaveRejected})

def RejectLeave(request):
    Id = request.POST.get('Id')
    dated = request.POST.get('Dated')
    leavestatus = InsertStudentLeave.objects.filter(Id=Id,Dated=dated).update(Status='Rejected')
    if leavestatus==1:
        messages.success(request,'Leave Rejected Successfully')
        current_user = request.user
        Id1 = current_user.username
        coordinatorData = InsertCoordinator.objects.get(Email_Id=Id1)
        studentLeaveApproved =  InsertStudentLeave.objects.filter(Course=coordinatorData.Course, Semester = coordinatorData.Semester, Section=coordinatorData.Section, Status="Approved")
        studentLeaveRejected =  InsertStudentLeave.objects.filter(Course=coordinatorData.Course, Semester = coordinatorData.Semester, Section=coordinatorData.Section, Status="Rejected")
        studentLeavePending =  InsertStudentLeave.objects.filter(Course=coordinatorData.Course, Semester = coordinatorData.Semester, Section=coordinatorData.Section, Status="Pending")
        return render(request,"Coordinator/Appr_Rejct.html",{'studentLeaveApproved':studentLeaveApproved,'coordinatorData': coordinatorData, 'studentLeavePending': studentLeavePending,'studentLeaveRejected':studentLeaveRejected})

def ApproveLeave(request):
    Id = request.POST.get('Id')
    Dated = request.POST.get('Dated')
    leavestatus = InsertStudentLeave.objects.filter(Id=Id,Dated=Dated).update(Status='Approved')
    if leavestatus==1:
        messages.success(request,'Leave Approved Successfully')
        current_user = request.user
        Id1 = current_user.username
        coordinatorData = InsertCoordinator.objects.get(Email_Id=Id1)
        studentLeaveApproved =  InsertStudentLeave.objects.filter(Course=coordinatorData.Course, Semester = coordinatorData.Semester, Section=coordinatorData.Section, Status="Approved")
        studentLeaveRejected =  InsertStudentLeave.objects.filter(Course=coordinatorData.Course, Semester = coordinatorData.Semester, Section=coordinatorData.Section, Status="Rejected")
        studentLeavePending =  InsertStudentLeave.objects.filter(Course=coordinatorData.Course, Semester = coordinatorData.Semester, Section=coordinatorData.Section, Status="Pending")
        return render(request,"Coordinator/Appr_Rejct.html",{'studentLeaveApproved':studentLeaveApproved,'coordinatorData': coordinatorData, 'studentLeavePending': studentLeavePending,'studentLeaveRejected':studentLeaveRejected})

def uploadFile(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            current_user = request.user
            Id = current_user.username
            studentData =  InsertStudent.objects.get(pk = Id)
            coordinatorData = InsertCoordinator.objects.get(Course=studentData.Course, Section=studentData.Section)
            student = StudentForm()
            messages.success(request,'Document Uploaded Successfully')
            return render(request,"fileupload.html",{'studentData':studentData,'coordinatorData': coordinatorData,'form':student})

def fileupload(request):
    current_user = request.user
    Id = current_user.username
    studentData =  InsertStudent.objects.get(pk = Id)
    coordinatorData = InsertCoordinator.objects.get(Course=studentData.Course, Section=studentData.Section)
    student = StudentForm()
    return render(request,"fileupload.html",{'studentData':studentData,'coordinatorData': coordinatorData,'form':student})