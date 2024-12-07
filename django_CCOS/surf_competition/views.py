from django.shortcuts import render
from .models import Competition
from django.http import JsonResponse

# Create your views here.
def show_competition(request):
    return render(request, 'surf_competition/surf_competition_base.html')

def filter_competition(request):
    category = request.GET.get('category', 'all')
    print(f"Requested category: {category}")  # 输出请求的分类，便于调试
    if category == 'all':
        competitions = Competition.objects.all()
    else:
        competitions = Competition.objects.filter(competition_category=category)

    data = [
        {
            "name": comp.competition_name,
            "category": comp.competition_category,
            "bonus": comp.competition_prize if comp.competition_prize else 0,
            "brand": comp.competition_brand or "无",
            "organization": comp.competition_organization or "无",
            "time": f"{comp.competition_begintime} ~ {comp.competition_endtime}" if comp.competition_begintime and comp.competition_endtime else "时间待定",
        }
        for comp in competitions
    ]
    return JsonResponse(data, safe=False)
