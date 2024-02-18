from django.shortcuts import render, redirect
from django.conf import settings
from .models import PostModel, SecPI1_Model, MastersModel, PriceModel, ReportsModel, Categories, BookingModel
from .forms import MasterForm, SecPI1Form
import requests
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def beaty_view(request):
    vv = ""
    a = request.GET.get("category", "")
    a = a.strip("'")
    if a:
        # print(int(a))
        vv = SecPI1_Model.objects.filter(categories_id=int(a))
    else:
        vv = SecPI1_Model.objects.all()
    if request.method == "POST":
        img = request.FILES["img"]
        text = request.POST["text"]
        obj_1 = PostModel(img=img, text=text)
        obj_1.save()
        return redirect("beaty")
    obj = PostModel.objects.all()
    return render(request, template_name="index.html", context={"posts": obj, "lulu":vv})

def home_section1(request, id):
    home_post = PostModel.objects.get(id=id)
    return render(request, "forms/home_section1.html", {"home_post":home_post})

def master_view(request):
    master = MastersModel.objects.all()
    if request.method == "POST":
        img = request.FILES["img"]
        text_n = request.POST["text_n"]
        text = request.POST["text"]
        obj_1 = MastersModel(img=img, text_n=text_n, text=text)
        obj_1.save()

        return redirect("master")
    return render(request, template_name="masters.html", context={"master": master, })


def master_detail(request, id):
    master_d = MastersModel.objects.get(id=id)
    return render(request, "forms/detail_master.html", {"master_d": master_d})

def master_delete(request, id):
    master_d = MastersModel.objects.get(id=id)
    if request.method == "POST":
        master_d.delete()
        return redirect("master")
    return render(request, "forms/master_delete.html", {"master_d":master_d})


def master_update_view(request, id):
    master_id = MastersModel.objects.get(id=id)
    form = MasterForm(instance=master_id)
    if request.method == "POST":
        form = MasterForm(request.POST, instance=master_id)
        if form.is_valid():
            form.save()
            return redirect("master")
    return render(request, template_name="forms/master_update.html", context={
        "form": form,
    })


def contacts_view(request):
    return render(request, template_name="contacts.html")


def price_view(request):
    price = PriceModel.objects.all()
    if request.method == "Post":
        img_pr = request.FILES["img"]
        h1 = request.POST["h1"]
        price1 = request.POST["price1"]
        text1 = request.POST["text1"]
        h2 = request.POST["h2"]
        print(h2)
        price2 = request.POST["price2"]
        text2 = request.POST["text2"]
        h3 = request.POST["h3"]
        price3 = request.POST["price3"]
        text3 = request.POST["text3"]
        h4 = request.POST["h4"]
        price4 = request.POST["price4"]
        text4 = request.POST["text4"]
        price_1 = PriceModel(img=img_pr, h1=h1, text1=text1, h2=h2, text2=text2, h3=h3, text3=text3, h4=h4, text4=text4)
        price_1.save()
        return redirect("price")
    return render(request, template_name="price.html", context={
        "price": price,
    })


def reports_view(request):
    reports = ReportsModel.objects.all()
    if request.method == "POST":
        f_name = request.POST["f_name"]
        l_name = request.POST["l_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        report = request.POST["report"]
        message = "Your report sent."

        report_1 = ReportsModel(first_name=f_name, last_name=l_name, email=email, phone_num=phone, text=report)
        report_1.save()
        send_mail(
            'Contact Form', message, 'settings.EMAIL_HOST_USER', [email], fail_silently=False)
        return redirect('reports')

    return render(request, "reports.html", {
        "reports": reports,
    })

@login_required(login_url="login")
def booking_view(request):
    booking = BookingModel.objects.all()
    if request.method == "POST":
        f_name = request.POST["f_name"]
        l_name = request.POST["l_name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        date = request.POST["date"]
        time = request.POST["time"]
        message = f"Your booking sent and now wait till the date: {date} {time} ."

        book_1 = BookingModel(first_name=f_name, last_name=l_name, email=email, phone_num=phone, date=date, time=time)
        book_1.save()
        send_mail(
            'Booking:', message, 'settings.EMAIL_HOST_USER', [email], fail_silently=False)
        text = "Booking to the Hair salon Delote-beauty: \n"
        text += f"Name: {f_name} {l_name}\n"
        text += f"Email: {email}\n"
        text += f"Phone number: {phone}\n"
        text += f"Date: {date} {time}\n"
        token = '6830484924:AAHgzh3966eeKU-w1FX2dTAW7ZVkcJoae-c'
        id = "1292573250"
        url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id='
        requests.get(url + id + '&text=' + text)
        return redirect('booking')
    return render(request, "booking.html", {"booking":booking})


def handling_404(request, exception):
    return render(request, "forms/404.html", {})
