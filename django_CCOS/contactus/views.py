from django.shortcuts import render
from django.http import JsonResponse
from .models import Contactus
from .models import Consult
from .models import Feedbackform
from .models import Volunteerrecruitment
from datetime import datetime

# Create your views here.
def show_contactus(request):
    return render(request,'contactus/contactus.html')

from django.http import JsonResponse
from .models import Contactus
from datetime import datetime

def submit_contact_form(request):
    if request.method == 'POST':
        # 从请求中获取表单数据
        contactus_id = request.POST.get('contactus_id')  
        date_str = request.POST.get('date') 
        email = request.POST.get('email')  

        sponsorshipform = request.POST.get('sponsorshipform')
        cooperationform = request.POST.get('cooperationform')
        competitionform = request.POST.get('competitionform')
        feedbackform = request.POST.get('feedbackform')
        volunteerapplicationform = request.POST.get('volunteerapplicationform')
        # 检查 contactus_id 是否为 10 位整数
        try:
            contactus_id = int(contactus_id)  # 转换为整数
            if len(str(contactus_id)) != 10:
                return JsonResponse({"message": "填表编号必须是 10 位整数"}, status=400)
        except ValueError:
            return JsonResponse({"message": "填表编号必须是有效的整数"}, status=400)
        
        # 解析日期字段，确保日期格式为 'YYYY-MM-DD'
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()  # 转换为 date 对象
        except ValueError:
            return JsonResponse({"message": "日期格式不正确，必须为 'YYYY-MM-DD'"}, status=400)
        
        # 检查邮箱长度是否小于 30 位
        if email and len(email) >= 30:
            return JsonResponse({"message": "邮箱长度不能超过 30 个字符"}, status=400)

        # 创建新的 Contactus 实例并保存到数据库
        new_contact = Contactus(
            contactus_id=contactus_id,
            date=date,
            email=email
        )
        new_contact.save()

        #创建新的 Consult 实例并保存到数据库
        new_consult = Consult(
            contactus_id=contactus_id,
            date=date,
            sponsor_consultation=sponsorshipform,
            cooperation_consultation=cooperationform,
            competition_consultation=competitionform
        )
        new_consult.save()
        #创建新的 Feedbackform 实例并保存到数据库
        new_feedbackform = Feedbackform(
            contactus_id=contactus_id,
            date=date,
            feedbackinformation=feedbackform 
        )
        new_feedbackform.save()
        #创建新的 Volunteerrecruitment 实例并保存到数据库
        new_volunteerrecruitment = Volunteerrecruitment(
            contactus_id=contactus_id,
            date=date,
            recruitmentrequirements=volunteerapplicationform
        )
        new_volunteerrecruitment.save()
        # 返回成功响应
        return JsonResponse({"message": "信息提交成功"})

    # 如果请求方式不是 POST，返回错误信息
    return JsonResponse({"message": "请求方式错误，请使用 POST 请求"}, status=400)
