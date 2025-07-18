from students import views
from django.urls import path

urlpatterns = [
    path('',views.redirect_root),  # Redirect root to student view
    path('student/',views.student),
    path('show/',views.show),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>/',views.update),
    path('delete/<int:id>/',views.delete),
]