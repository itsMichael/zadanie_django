from django.shortcuts import \
    render_to_response, RequestContext, HttpResponseRedirect
from users_base.models import User, UserForm


def home(request):
    users = User.objects.all()
    return render_to_response('index.html', {'data': users})


def add(request):
    if request.method == "POST":
        form_user = UserForm(request.POST)
        form_user.is_valid()
        data = form_user.cleaned_data
        if form_user.is_valid()==True:
            print data['first_name'], data['last_name'], data['birthday']
            obj = User(
                first_name=data['first_name'],
                last_name=data['last_name'],
                birthday=data['birthday'],
                random_number=1,
                )
            obj.save()
        return HttpResponseRedirect("/")
    return render_to_response(
        'add.html', {'form': UserForm},
        context_instance=RequestContext(request))
