from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import timeEntry
from rest_framework.response import Response 


class YearView(ListAPIView):

  def get(self, _request, **kwargs):
    req_year = kwargs['year']

    query_request = timeEntry.objects.filter(year=req_year)

    return Response(query_request)


class GPView(ListAPIView):

  def get(self, _request, **kwargs):
      req_year = kwargs['year']
      req_gp = kwargs['gp']

      query_request = timeEntry.objects.filter(year=req_year, 
                                                gp=req_gp )

      return Response(query_request)
      

class SessionView(ListAPIView):

  def get(self, _request, **kwargs):
    req_year = kwargs['year']
    req_gp = kwargs['gp']
    req_session = kwargs['session']

    query_request = timeEntry.objects.filter(year=req_year,
                                              gp=req_gp,
                                              session=req_session)

    return Response(query_request)

class TeamView(ListAPIView):

  def get(self, _request, **kwargs):
    req_year = kwargs['year']
    req_gp = kwargs['gp']
    req_session = kwargs['session']
    req_team = kwargs['session']

    query_request = timeEntry.objects.filter(year=req_year,
                                              gp=req_gp,
                                              session=req_session,
                                              team= req_team,)
    return Response(query_request)

class DriverView(ListAPIView):

  def get(self, _request, **kwargs):
    req_year = kwargs['year']
    req_gp = kwargs['gp']
    req_session = kwargs['session']
    req_team = kwargs['team']
    req_driver = kwargs['driver']

    query_request = timeEntry.objects.filter(year=req_year,
                                              gp=req_gp,
                                              session=req_session,
                                              team= req_team,
                                              driver= req_driver)

    return Response(query_request)