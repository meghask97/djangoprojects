from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
class Cbvview(View):
	def get(self,requets):
		data='<h1>Welcome to Study Online.....<br> This is View class</h1>'
		return HttpResponse(data)