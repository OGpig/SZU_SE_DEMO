from django.shortcuts import render
from .models import Competition
from django.http import JsonResponse

# Create your views here.
def show_competition(request):
    return render(request, 'surf_competition/surf_competition_base.html')
#详情页
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
