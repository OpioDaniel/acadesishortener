from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
import requests
from django.http import JsonResponse
from .models import AcadeURL
from ..analytics.models import ClickEvent
from .forms import SubmitUrlForm
import pyshorteners


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            "form": form
        }
        return render(request, 'main/index.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
                'form': form
            }
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = AcadeURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
                'form': SubmitUrlForm()
            }
        return render(request, 'main/index.html', context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = AcadeURL.objects.filter(shortcode__iexact=shortcode)
        if qs.exists() and qs.count() == 1:
            obj = qs.first()
        obj = get_object_or_404(AcadeURL, shortcode=shortcode)
        ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect(obj.url)


# class HomeView(View):
#     def get(self, request, *args, **kwargs):
#         form = SubmitUrlForm()
#         context = {
#             "form": form
#         }
#         # full_link = request.get('full_link')
#         # print("going through : ", full_link)
#         return render(request, 'main/index.html', context)
#
#     def post(self, request, *args, **kwargs):
#         print(request.POST)
#         print(request.POST.get('url'))
#         form = SubmitUrlForm(request.POST)
#         context = {
#             "title": "shortener.co",
#             "form": form
#         }
#         template = 'main/index.html'
#         # print("before", form.cleaned_data)
#         if form.is_valid():
#             print("after", form.cleaned_data)
#             new_url = form.cleaned_data.get("url")
#             obj, created = AcadeURL.objects.get_or_create(url=new_url)
#             context = {
#                 "object": obj,
#                 "created": created,
#             }
#             if created:
#                 template = 'main/success.html'
#             else:
#                 template = 'main/already_exists.html'
#             # print(obj.get_short_url())
#         # print("going through : ", full_link)
#         return render(request, template, context)


# def acade_redirect_view(request, shortcode=None, *args, **kwargs):
    # print(request.user)
    # print(request.user.is_authenticated)
    # print(args)
    # print(kwargs)
    # obj = AcadeURL.objects.get(shortcode=shortcode)

    # try:
    #     obj = AcadeURL.objects.get(shortcode=shortcode)
    # except Exception as ex:
    #     obj = AcadeURL.objects.all().first()

    # obj_url = None
    # qs = AcadeURL.objects.filter(shortcode__iexact=shortcode)
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url
    # obj = get_object_or_404(AcadeURL, shortcode=shortcode)
    # print('a== ', shortcode)
    # return HttpResponseRedirect(obj.url)
    # return HttpResponse("hello {sc}".format(sc=obj.url))

# def urlshortener(request):
#     if request.method == 'POST':
#         full_link = request.POST.get('full_link')
#         full_link = full_link.strip()
#         print(full_link)
#         headers = {
#             'Authorization': 'Bearer f5800c2a76a863ebea40f5d7c0225a39f67cd301',
#             'Content-Type': 'application/json',
#         }
#         data = '{ "long_url": "'+full_link+'" }'
#         response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
#         # print(response.json())
#         sl = response.json().get('link')
#         ll = response.json().get('long_url')
#         rr = {'shorturl': sl, 'longurl': ll}
#     return JsonResponse(rr)



# def urlshortener(request):
#     if request.method == 'POST':
#         full_link = request.POST.get('full_link')
#         print(full_link)
#         API_KEY = "2102250082883d42e106dfad1f039085adb64"
#         # API_KEY = "0f6c7489c714438a8fc272e7a2cd13ed"
#         BASE_URL = "https://cutt.ly/api/api.php"
#         pay_load = {"key": API_KEY, "short": full_link, "name": ""}
#         request = requests.get(BASE_URL, params=pay_load)
#         data = request.json()
#         print(data)
#         rr = {'status': 'ok.', 'data': data}
#     return JsonResponse(rr)

# ACCESS_TOKEN = 'f5800c2a76a863ebea40f5d7c0225a39f67cd301'

# def urlshortener(request):
#     if request.method == 'POST':
#         full_link = request.POST.get('full_link')
#         full_link = full_link.strip()
#         print("going through : ", full_link)
#         rr = {}
#     return JsonResponse(rr)