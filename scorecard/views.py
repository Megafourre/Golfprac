from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Scorecard

# Create your views here.
def scorecard_list(request):
    scorecards=Scorecard.objects.filter(published_date__lte=timezone.now()).order_by('played_date')
    return render(request, 'scorecard/scorecard_list.html', {'scorecards':scorecards})

def scorecard_detail(request,pk):
    scorecard=get_object_or_404(Scorecard,pk=pk)
    return render(request, 'scorecard/scorecard_detail.html', {'scorecard':scorecard})
