import datetime

from django.shortcuts import render, redirect, get_object_or_404
# from bs4 import BeautifulSoup, NavigableString, Tag
from pip._vendor.urllib3.connectionpool import xrange

from .models import *
from .forms import *


def base(request):
    general = SectionGeneral.objects.last()
    service = GeneralServices.objects.last()
    services = Services.objects.all()
    about = AboutMe.objects.last()
    works = Works.objects.all()
    reviews = Review.objects.all()
    contacts = Contacts.objects.last()
    information = Information.objects.all()

    context = {
        'general': general,
        'service': service,
        'services': services,
        'about': about,
        'works': works,
        'reviews': reviews,
        'contacts': contacts,
        'information': information,
    }
    return render(request, 'core/core_base.html', context)


def info(request, id=None):
    general = SectionGeneral.objects.last()
    information = Information.objects.all()
    contacts = Contacts.objects.last()
    info = get_object_or_404(Information, id=id)

    context = {
        'information': information,
        'info': info,
        'contacts': contacts,
        'general': general,
    }
    return render(request, 'core/info.html', context)


def review(request):
    general = SectionGeneral.objects.last()
    information = Information.objects.all()
    contacts = Contacts.objects.last()
    reviews = Review.objects.all()

    context = {
        'information': information,
        'reviews': reviews,
        'contacts': contacts,
        'general': general,
    }
    return render(request, 'core/review.html', context)


def review_create(request):
    general = SectionGeneral.objects.last()
    information = Information.objects.all()
    contacts = Contacts.objects.last()
    if request.method == 'POST':
        form = ReviewCreateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReviewCreateForm()

    context = {
        'information': information,
        'review': review,
        'contacts': contacts,
        'general': general,
        'form': form,
    }
    return render(request, 'core/review_create.html', context)



def calendar(request):
    today = datetime.date.today().strftime('%Y-%m-%d')
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = tomorrow.strftime('%Y-%m-%d')
    nextYear = int(datetime.date.today().year) + 1
    successDays = CheckedDate.objects.all()
    successTimes = CheckedTime.objects.all()

    weekends = []

    dates = []
    times = []
    for sdays in successTimes:
        dates.insert(0, sdays.date)
        times.insert(0, sdays.time)
    #
    # times = iter(times)
    # dates = iter(dates)
    #
    # res = list(zip(dates, times))
    # data = {}
    # for (x, y) in res:
    #     if x in data:
    #         data[x] = data[x] + y
    #     else:
    #         data[x] = y
    #
    # data = {
    #     'labels': data.keys(),
    #     'default': data.values()
    # }


    # print(data)

    minDate = datetime.date(2020, 1, 1)
    maxDate = datetime.date.today() + datetime.timedelta(days=750)
    daygenerator = (minDate + datetime.timedelta(x + 1) for x in xrange((maxDate - minDate).days))
    for day in daygenerator:
        if day.weekday() >= 5:
            weekends.append(str(day.strftime('%Y-%m-%d')))

    if request.method == 'POST':
        sdate = request.POST.get('date')
        stime = request.POST.get('time')
        if sdate and stime is not None:
            a = CheckedDate.objects.filter(date=sdate)
            print(a.first())
            if a.first() is None:
                createCheckedDate = CheckedDate(date=sdate)
                createCheckedDate.save()
            filteredDate = CheckedDate.objects.filter(date=sdate).first()
            createCheckedTime = CheckedTime(time=stime, date_id=filteredDate.id)
            createCheckedTime.save()
    filteredDate = CheckedDate.objects.all()
    for filtered in filteredDate:
        f_id = filtered.id
        b = len(CheckedTime.objects.filter(date_id=f_id))
        if b == 14:
            f_d = CheckedDate.objects.filter(id=f_id).first()
            weekends.append(f_d)
    choices = []
    for choice in dict(CheckedTime.TIME_CHOICES):
        choices.append(choice)

        # print(stime)
        # print(sdata)

    context = {
        'today': today,
        'tomorrow': tomorrow,
        'successDays': successDays,
        'weekends': weekends,
        'nextYear': nextYear,
        'choices': choices,
    }
    return render(request, 'core/calendar/calendar1.html', context)








