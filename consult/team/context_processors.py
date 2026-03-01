from .models import TeamMember

def team_members(request):
    return {
        'team_members': TeamMember.objects.all()
    }