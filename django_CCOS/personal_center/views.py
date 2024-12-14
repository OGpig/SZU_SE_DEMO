import logging

from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse

from customer.models import Customer
from personal_center.models import User


# Create your views here.

def information(request):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')


    user_id = request.session['user_id']
    customer = Customer.objects.filter(customer_id=user_id).first()

    if customer.address:
        # print("已经填过地址")
        return redirect("customer:show_info")

    user = User.objects.filter(user_id=user_id).first()
    user_id = user.user_id
    user_name = user.user_name
    user_avatar = user.user_avatar
    user_role = user.user_role
    user_sex = user.user_sex
    user_describe = user.user_describe
    user_birthday = user.user_birthday
    user_school = user.user_school
    user_phone = user.user_phone
    user_email = user.user_email
    user_pwd = customer.customer_password

    request.session['is_login'] = True
    request.session['user_id'] = user_id
    request.session['user_name'] = user_name
    request.session['user_avatar'] = user_avatar
    request.session['user_role'] = user_role
    request.session['user_sex'] = user_sex
    request.session['user_describe'] = user_describe
    request.session['user_birthday'] = user_birthday
    request.session['user_school'] = user_school
    request.session['user_phone'] = user_phone
    request.session['user_email'] = user_email
    request.session['user_pwd'] = user_pwd

    # return render(request, 'customer/information.html', locals())
    return render(request, 'personal_center/customer_info.html', locals())




def updateInfo(request):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')

    if request.method == 'POST':
        # 从请求中获取表单数据
        user_id = request.POST.get('user_id')
        user_name = request.POST.get('user_name')
        user_avatar = request.POST.get('user_avatar')
        user_role = request.POST.get('user_role')
        user_describe = request.POST.get('user_describe')
        user_birthday = request.POST.get('user_birthday')
        user_school = request.POST.get('user_school')
        user_phone = request.POST.get('user_phone')
        user_email = request.POST.get('user_email')
        user_pwd = request.POST.get('user_pwd')
        user_sex = request.POST.get('user_sex')

        user = User.objects.filter(user_id=user_id).first()

        if user_name != None:
            user.user_name = user_name

        if user_avatar != None:
            user.user_avatar = user_avatar
        if user_role != None:
            user.user_role = user_role
        if user_describe != None:
            user.user_describe = user_describe
        if user_birthday != None:
            user.user_birthday = user_birthday
        if user_school != None:
            user.user_school = user_school
        if user_phone != None:
            user.user_phone = user_phone
        if user_email != None:
            user.user_email = user_email
        if user_sex != None:
            user.user_sex = user_sex
        user.save()
        customer = Customer.objects.filter(customer_id=user_id).first()
        if user_pwd != None:
            customer.customer_password = user_pwd
        if user_name != None:
            customer.customer_name = user_name
        customer.save()
        request.session['is_login'] = True
        request.session['user_id'] = user_id
        request.session['user_name'] = user_name
        request.session['user_avatar'] = user_avatar
        request.session['user_role'] = user_role
        request.session['user_describe'] = user_describe
        request.session['user_birthday'] = user_birthday
        request.session['user_school'] = user_school
        request.session['user_phone'] = user_phone
        request.session['user_email'] = user_email
        request.session['user_pwd'] = user_pwd

        # return render(request, 'personal_center/customer_info.html', locals())

        # # 返回成功响应
        return JsonResponse({"message": "信息提交成功"})

