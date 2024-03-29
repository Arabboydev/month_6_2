from django.urls import path
from .views import grands, iqtidorli_talabalar


urlpatterns = [
    path('grands/', grands),
    path('iqtidor/', iqtidorli_talabalar),
]