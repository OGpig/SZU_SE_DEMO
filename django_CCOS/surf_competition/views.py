from django.shortcuts import render
from .models import Competition
from django.http import JsonResponse

# Create your views here.
def show_competition(request):
    return render(request, 'surf_competition/surf_competition_base.html')
#详情页
def search_competition(request):
    category = request.GET.get('category', 'all')
    search_keyword = request.GET.get('search', '').strip()

    # 固定类别列表
    valid_categories = ['泰迪杯挑战赛', '泰迪杯技能赛', '湾区金融数模', '华中杯', '技能兴鲁', '大学生科技节']

    if search_keyword:
        if search_keyword in valid_categories:
            competitions = Competition.objects.filter(competition_category=search_keyword)
        else:
            competitions = []  # 其他值返回空
    elif category == 'all':
        competitions = Competition.objects.all()  # 显示全部
    else:
        competitions = Competition.objects.filter(competition_category=category)

    # 将结果转换为 JSON 格式
    data = [
        {
            "name": comp.competition_name,
            "category": comp.competition_category,
            "bonus": comp.competition_prize if comp.competition_prize else 0,
            "brand": comp.competition_brand or "无",
            "organization": comp.competition_organization or "无",
            "time": f"{comp.competition_begintime} ~ {comp.competition_endtime}" if comp.competition_begintime and comp.competition_endtime else "时间待定",
            "image_url": comp.image_url if hasattr(comp, 'image_url') else "/static/images/default.png",
        }
        for comp in competitions
    ]
    return JsonResponse(data, safe=False)
def show_competition_detail(request):
    competition_id = request.GET.get('id')  # 获取传递的竞赛 ID
    competition = Competition.objects.get(competition_id=competition_id)

    context = {
        "id": competition.competition_id,
        "name": competition.competition_name,
        "category": competition.competition_category,
        "brand": competition.competition_brand,
        "organization": competition.competition_organization,
        "bonus": str(competition.competition_prize),
        "team_count": competition.competition_teams,

        "time": f"{competition.competition_begintime} ~ {competition.competition_endtime}",
    }
    return render(request, 'surf_competition/competition_list.html', context)

def filter_competition(request):
    category = request.GET.get('category', 'all')
    if category == 'all':
        competitions = Competition.objects.all()
    else:
        competitions = Competition.objects.filter(competition_category=category)

    data = [
        {
            "id": comp.competition_id,
            "name": comp.competition_name,
            "category": comp.competition_category,
            "bonus": comp.competition_prize if comp.competition_prize else 0,
            "brand": comp.competition_brand or "无",
            "team_count":comp.competition_teams if comp.competition_teams else 0,
            "organization": comp.competition_organization or "无",
            "time": f"{comp.competition_begintime} ~ {comp.competition_endtime}" if comp.competition_begintime and comp.competition_endtime else "时间待定",
        }
        for comp in competitions
    ]
    return JsonResponse(data, safe=False)
