from django.urls import path 
from .views import (
                    GPView,
                    YearView,
                    SessionView,
                    TeamView,
                    DriverView,
)


urlpatterns = [
  path('<int:year/', ),
  path('<int:year/<str:gp>'),
  path('<int:year/<str:gp>/<str:session>'),
  path('<int:year/<str:gp>/<str:session>/<str:team>/'),
  path('<int:year>/<str:gp>/<str:session>/<str:team>/<str:driver>/', )
]