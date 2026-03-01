from .forms import StayUpdateForm

def stayupdate_form(request):
    return {'stayupdate_form': StayUpdateForm()}