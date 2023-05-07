from django.shortcuts import render
from django.views.generic.base import View


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(self.request, 'website/home.html')