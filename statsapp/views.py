from django.shortcuts import render, redirect
from django.views import View
from .models import *
from userapp.models import Ombor
from asosiy.models import Mahsulot, Client


class StatsView(View):
    def get(self, request):
        o = Ombor.objects.get(user = request.user)
        tanlov = request.GET.get("ustun")
        soz = request.GET.get("soz")
        stats = Stats.objects.filter(ombor=o)
        if tanlov == "m" and soz != "":
            m = Mahsulot.objects.filter(nom__contains=soz) | Mahsulot.objects.filter(brend__contains=soz)
            if m:
                stats = Stats.objects.filter(mahsulot=m[0], ombor=o)
                for i in m:
                    stats = stats | Stats.objects.filter(mahsulot=i, ombor=o)
        elif tanlov == "c" and soz != "":
            cl = Client.objects.filter(ism__contains=soz) | Client.objects.filter(dokon__contains=soz)
            if cl:
                stats = Stats.objects.filter(client=cl[0], ombor=o)
                for i in cl:
                    stats = stats | Stats.objects.filter(client=i, ombor=o)
        elif tanlov == "s" and soz !="":
            stats = Stats.objects.filter(sana__contains=soz, ombor=o)
        data = {
            "st1":stats,
            "mahsulotlar":Mahsulot.objects.filter(ombor=o),
            "clients":Client.objects.filter(ombor=o)
        }
        return render(request, "stats.html", data)

    def post(self, request):
        Stats.objects.create(
            mahsulot = Mahsulot.objects.get(id=request.POST.get("mahsulot")),
            client = Client.objects.get(id=request.POST.get("client")),
            sana = request.POST.get("s"),
            miqdor = request.POST.get("miqdor"),
            umumiy = request.POST.get("u"),
            nasiya = request.POST.get("n"),
            tolandi = request.POST.get("t"),
            ombor = Ombor.objects.get(user=request.user),
        )
        m = Mahsulot.objects.get(id=request.POST.get("mahsulot"))
        m.miqdor = m.miqdor - int(request.POST.get("miqdor"))
        m.save()
        cl = Client.objects.get(id=request.POST.get("client"))
        cl.qarz = cl.qarz + int(request.POST.get("n"))
        cl.save()
        return redirect("/stats/")


class StatsEdit(View):
    def get(self, request, pk):
        data = {
            "s": Stats.objects.get(id=pk)
        }
        return render(request, "stats_update.html", data)

    def post(self, request, pk):
        Stats.objects.filter(id=pk).update(
            sana=request.POST.get("v"),
            miqdor = request.POST.get("m"),
            umumiy = request.POST.get("u"),
            tolandi = request.POST.get("t"),
            nasiya = request.POST.get("n")
        )
        return redirect("/stats/")

