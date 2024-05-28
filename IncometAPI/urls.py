from django.urls import path, include
from IncometAPI.views import *
from rest_framework.routers import DefaultRouter
# from posts import urls as posts_urls

# from Posts import views
router = DefaultRouter()
router.register(r'News',News1,basename="News")
router.register(r'Newsdetail',Newsdetail,basename="Newsdetail")
router.register(r'CoursesList',CoursesList,basename="CoursesList")
router.register(r'RatingList',RatingList,basename="RatingList")
router.register(r'stories',Stories,basename="stories")
router.register(r'CartList', CartList, basename='CartList')
router.register(r'BeginnerList', BeginnerList, basename='BeginnerList')
router.register(r'MediumList', MediumList, basename='MediumList')
router.register(r'AdvanceList', AdvanceList, basename='AdvanceList')
router.register(r'CertificateList', CertificateList, basename='CertificateList')
router.register(r'LearnList', LearnList, basename='LearnList')
router.register(r'LernerBeginnerList', LernerBeginnerList, basename='LernerBeginnerList')
router.register(r'LernerMediumList', LernerMediumList, basename='LernerMediumList')
router.register(r'LernerAdvanceList', LernerAdvanceList, basename='LernerAdvanceList')
# router.register(r'CreateBatch', Batch, basename='CreateBatch')
# router.register(r'updateBatch', Batch, basename='updateBatch')
# router.register(r'deleteBatch', Batch, basename='deleteBatch')
router.register(r'listBatch', CreateBatch, basename='listBatch')
# router.register(r'GroupCreateBatch', GroupCreateBatch, basename='GroupCreateBatch')
router.register(r'BuyCourse', BuyCourse, basename='BuyCourse')
# router.register(r'GetBuyCourse', GetBuyCourse, basename='GetBuyCourse')
router.register(r'My_Cource', My_Cource, basename='My_Cource')
router.register(r'CreateCourse_Section', CreateCouse_Section, basename='CreateCourse_Section')
router.register(r'CreateViewCourse_Review', CreateViewCourse_Review, basename='CreateViewCourse_Review')
router.register(r'GetCourse_Section', GetCouse_Section, basename='GetCouse_Section')
router.register(r'GetCourse_Review', GetCourse_Review, basename='GetCourse_Review')
router.register(r'GetBegnnerData', GetBegnnerData, basename='GetBegnnerData')
router.register(r'GetMediumData', GetMediumData, basename='GetMediumData')
router.register(r'GetAdvanceData', GetAdvanceData, basename='GetAdvanceData')
router.register(r'GetCertificateData', GetCertificateData, basename='GetCertificateData')

router.register(r'Educator_Testimoniala', Educator_TestimonialaView, basename='Educator_Testimoniala')
router.register(r'Educator_Intorvideo', Educator_IntorvideoView, basename='Educator_Intorvideo')
router.register(r'Educators', EducatorsView, basename='Educators')
router.register(r'CreateEducators', CreateEducators, basename='CreateEducators')
router.register(r'CategoryAPI', CategoryAPI, basename='CategoryAPI')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', include('Posts.urls'))
]
