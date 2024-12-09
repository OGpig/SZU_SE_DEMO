from django.shortcuts import render
from django.http import JsonResponse
from .models import Contactus
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
        contactus_id = request.POST.get('phone')  # contactus_id 对应 phone 字段
        date_str = request.POST.get('position')  # date 对应 position 字段
        email = request.POST.get('email')  # email 对应 email 字段

        # 解析日期字段，确保日期格式为 'YYYY-MM-DD'
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()  # 转换为 date 对象
        except ValueError:
            return JsonResponse({"message": "日期格式不正确，必须为 'YYYY-MM-DD'"}, status=400)

        # 创建新的 Contactus 实例并保存到数据库
        new_contact = Contactus(
            contactus_id=contactus_id,
            date=date,
            email=email
        )
        new_contact.save()

        # 返回成功响应
        return JsonResponse({"message": "信息提交成功"})

    # 如果请求方式不是 POST，返回错误信息
    return JsonResponse({"message": "请求方式错误，请使用 POST 请求"}, status=400)
