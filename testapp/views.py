# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from testapp.models import Student, Course, Payment_Method, Order,  Order_items



def classdetail(request):
  if request.method == 'POST':
    allClasses = request.POST.getlist('selectedClass')
    print("yesssssssssss", allClasses)
    request.session['allClasses'] = allClasses
    return redirect('http://127.0.0.1:8000/testapp/checkout/')
  else:
    course_set = Course.objects.select_related()
    return render(request, 'testapp/classdetail.html', {'course_set' : course_set } )

def checkoutPage(request):
  if request.method == 'POST':
    ## create new student instance
    fname = request.POST['fname']
    lname = request.POST['lname']
    street = request.POST['street']
    city = request.POST['city']
    country = request.POST['country']
    zipcode = request.POST['zipcode']
    stu = Student(first_name = fname, last_name = lname, age=20, email = 'student@email.com', gender = 'f', phone = '12345', address = street, zipcode_id = 3)
    stu.save()
    
    ## create new payment instance 
    paymentType = request.POST['CreditCardType']
    card_number = request.POST['cardNum']
    cvv = request.POST['cvv']
    exp_month = request.POST['month']
    exp_year = request.POST['year']
    exp_date = str(exp_year + '-' + exp_month + '-' + '01')
    pay = Payment_Method(card_number = card_number, payment_type = paymentType, expired_date = exp_date )
    pay.save()
    
    ## bring new student_id && payment_id to create new order instance 
    new_stu_id = stu.pk
    new_pay_id = pay.pk
    new_order = Order(ord_placed_date = '2017-12-07', ord_paid_date = '2017-12-07', payment_id_id = new_pay_id, student_id_id = new_stu_id)
    new_order.save()
    
    ## bring new order_id to create new order_items instance
    new_order_item = Order_items(quantity = 1, course_id_id = 3, order_id_id = new_order.pk)
    new_order_item.save()
    ## fetch required info for final page
    stdName = str(fname + ' ' + lname)
    allClasses = request.session['allClasses'][0]
    theClass = Course.objects.get(pk=allClasses)
    return render(request, 'testapp/finishPage.html', { 'comId': new_order_item.pk, 'stdName': stdName, 'course' : theClass })
  else: 
    allClasses = request.session['allClasses'][0]
    theClass = Course.objects.get(pk=allClasses)
    print('i am in checkout page func', theClass.course_name)
    return render(request, 'testapp/checkoutPage.html', {'selectedClass': theClass})