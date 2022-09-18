from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index,name="index"),
    path('logout/', views.Logout,name='Logout'),
    path('createAdmin/',views.createAdmin,name="createAdmin"),
    path('my-admin/',views.admin,name="admin"),
    path('admin-dashboard/',views.adminDashboard,name="adminDashboard"),
    path('my-admin-dashboard/',views.adminLogin,name="AdminLogin"),
    path('coordinator-profile/',views.coordinatorProfile,name="coordinatorProfile"),
    path('coordinator-profile-update/',views.coordinatorProfileUpdate,name="coordinatorProfileUpdate"),
    path('student-profile/',views.studentProfile,name="studentProfile"),
    path('student-profile-update/',views.studentProfileUpdate,name="studentProfileUpdate"),
    path('Student-Login/',views.StudentLogin,name="StudentLogin"),
    path('studentLogin/',views.studentLogin,name="studentLogin"),
    path('leaveApplication/',views.LeaveApplication,name="leaveApplication"),
    path('Coordinator-Login/',views.CoordinatorLogin,name="CoordinatorLogin"),
    path('coordinatorLogin/',views.coordinatorLogin,name="coordinatorLogin"),
    path('Student-Login/',views.StudentLogin1,name="StudentLogin1"),
    path('Coordinator-Login/',views.CoordinatorLogin1,name="CoordinatorLogin1"),
    path('student-portal/',views.studentPortal,name="studentPortal"),
    path('apply-leave/',views.ApplyLeave,name="ApplyLeave"),
    path('leave-application-status/',views.LeaveApplicationStatus,name="LeaveApplicationStatus"),
    path('coordinator-portal/',views.coordinatorPortal,name="coordinatorPortal"),
    path('track-status/',views.TrackStatus,name="TrackStatus"),
    path('approve-reject/',views.ApproveReject,name="ApproveReject"),
    path('insert-student/',views.InsertStudentDetail,name="InsertStudent"),
    path('insert-coordinator/',views.InsertCoordinatorDetail,name="InsertCoordinator"),
    path('update-coordinator/<str:id>/',views.UpdateCoordinator,name="UpdateCoordinator"),
    path('update-student/<str:id>/',views.UpdateStudent,name="UpdateStudent"),
    path('delete-student/',views.DeleteStudent,name="DeleteStudent"),
    path('delete-coordinator/',views.DeleteCoordinator,name="DeleteCoordinator"),
    path('reject-leave/',views.RejectLeave,name="RejectLeave"),
    path('approve-leave/',views.ApproveLeave,name="ApproveLeave"),
    path('upload-file/',views.uploadFile,name="UploadFile"),
    path('file-upload/',views.fileupload,name="fileupload"),
]
       
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)