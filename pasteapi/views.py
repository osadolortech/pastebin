from .serializer import PasteSerializer
from .models import PasteBin
from django.views import View
from rest_framework import viewsets
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.

class PasteView(viewsets.ModelViewSet):
    queryset = PasteBin.objects.all()
    serializer_class = PasteSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class Redirect(View):
    def get(self,shorten_url):
        shorten_url = settings.HOST_URL +'/'+self.kwargs['shorten_url']
        redirect_link = PasteBin.objects.filter(shorten_url=shorten_url).first().text
        return redirect(redirect_link)