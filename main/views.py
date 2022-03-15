from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class MainIndex(View):

    def get(self, request):
        return render(request, 'main/index.html')



