from django.urls import path,include
from rest_framework import routers
from myapp.views import ContactformviewSet
from .views import ResumeSubmissionViewSet
from . import views

router=routers.DefaultRouter()
router.register(r'contactform',ContactformviewSet)
router.register(r'resumesubmission', ResumeSubmissionViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',include(router.urls)),
     path('api/save_contact_form/', views.save_contact_form, name='save_contact_form'),
     path('uploadresume/', views.upload_resume, name='upload_resume'),
]
