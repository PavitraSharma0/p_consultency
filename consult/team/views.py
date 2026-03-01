from django.shortcuts import render
from .models import TeamMember

# Create your views here.

def team_page(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team.html', {'team_members': team_members})
