from django.shortcuts import render, redirect
from Property import forms, models
from PendingAndBooking import models as Pmodels
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re



def simple_search(request):
    template = 'property_list.html'
    if request.method == "POST":
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        type = request.POST.get('type')
        capacity = request.POST.get('adults')
        city = request.POST.get('city')
        price = request.POST.get('price')
    else:
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        type = request.GET.get('type')
        capacity = request.GET.get('adults')
        city = request.GET.get('city')
        price = request.GET.get('price')



    if not check_in:
        print ("no check_in")
    else:
        check_in = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_in)
    if not check_out:
        print ("no check_out")
    else:
        check_out = re.sub(r'(\d{2})-(\d{2})-(\d{4})', '\\3-\\2-\\1', check_out)
    if not capacity:
        capacity = 0
    else:
        capacity = int(capacity)
    if not price:
        price = 0
    else:
        price = int(price)
    if not city:
        city = ''
    if type == 'ALL' or not type:
        type = ''



    print('check_in: {},check_out: {},type: {},capacity: {},city: {},price: {}'.format(check_in,check_out,type,capacity,city,price),sep='\n')

    if not check_in and not check_out:
        booked_properties = []
    elif not check_in:
        booked_properties = Pmodels.TransAndReview.objects.filter(Q(start_time__lt=check_out)
                                                             ).values_list('pid',flat=True).distinct()
    elif not check_out:
        booked_properties = Pmodels.TransAndReview.objects.filter(Q(end_time__gt=check_in)
                                                             ).values_list('pid',flat=True).distinct()
    else:
        booked_properties = Pmodels.TransAndReview.objects.filter(Q(start_time__lt=check_out) &
                                                                 Q(end_time__gt=check_in)
                                                                 ).values_list('pid',flat=True).distinct()

    for x in booked_properties:
        print('booked id is ',x)


    property_list = models.Property.objects.filter(Q(city__icontains=city) &
                                                   Q(types_property__icontains=type) &
                                                   Q(price__gte=price) &
                                                   Q(capacity__gte=capacity)
                                                   ).distinct().exclude(id__in=booked_properties)



    # ====================== sort part====================================

    property_list = sorted(property_list, key=lambda x: x.price, reverse=False)

    # ====================== end sort part =================================

    # 分页-----------------
    paginator = Paginator(property_list, 10)
    page = request.GET.get('page')

    try:
        properties = paginator.page(page)
    except PageNotAnInteger:
        properties = paginator.page(1)
    except EmptyPage:
        properties = paginator.page(paginator.num_pages)

    empty = len(property_list)
    print("empty is:",empty)
    context = {
        'properties': properties,
        'city': city,
        'check_in': check_in,
        'check_out': check_out,
        'capacity': capacity,
        'price': price,
        'type': type,
        'empty': empty,
    }
    return render(request, template, context)



