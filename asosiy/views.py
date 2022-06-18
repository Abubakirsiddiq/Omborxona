from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import Ombor


class MahsulotView(View):
    def get(self, request):
        o = Ombor.objects.get(user=request.user)
        m = Mahsulot.objects.filter(ombor=o)
        return render(request, "products.html", {"products":m})

    def post(self, request):
        Mahsulot.objects.create(
        nom = request.POST.get("pr_name"),
        brend = request.POST.get("pr_brand"),
        kelgan_narx = request.POST.get("pr_price1"),
        sotuv_narx = request.POST.get("pr_price2"),
        miqdor = request.POST.get("pr_amount"),
        ombor = Ombor.objects.get(user=request.user)
        )
        return redirect("/asosiy/mahsulotlar/")


class MahsulotEdit(View):
    def get(self, request, pk):
        data = {
            "m": Mahsulot.objects.get(id=pk)
        }
        return render(request, "product_update.html", data)

    def post(self, request, pk):
        Mahsulot.objects.filter(id=pk).update(
            nom = request.POST.get("nom"),
            brend = request.POST.get("b"),
            kelgan_narx = request.POST.get("k_n"),
            sotuv_narx = request.POST.get("s_n"),
            miqdor = request.POST.get("m")
        )
        return redirect("/asosiy/mahsulotlar/")


class ClientView(View):
    def get(self, request):
        o = Ombor.objects.get(user=request.user)
        m = Client.objects.filter(ombor=o)
        return render(request, "clients.html", {"clients":m})

    def post(self, request):
        Client.objects.create(
        ism = request.POST.get("client_name"),
        dokon = request.POST.get("client_shop"),
        tel = request.POST.get("client_phone"),
        manzil = request.POST.get("client_address"),
        qarz = request.POST.get("client_debt"),
        ombor = Ombor.objects.get(user=request.user)
        )
        return redirect("/asosiy/client/")


class ClientEdit(View):
    def get(self, request, pk):
        data = {
            "c": Client.objects.get(id=pk)
        }
        return render(request, "client_update.html", data)

    def post(self, request, pk):
        Client.objects.filter(id=pk).update(
            dokon=request.POST.get("d"),
            ism = request.POST.get("i"),
            tel = request.POST.get("t"),
            manzil = request.POST.get("m"),
            qarz = request.POST.get("q")
        )
        return redirect("/asosiy/client/")


class BolimView(View):
    def get(self, request):
        return render(request, "bulimlar.html")

