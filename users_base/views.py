# -*- coding: utf-8 -*-
from django.shortcuts import \
    render_to_response, RequestContext, HttpResponseRedirect, HttpResponse
from users_base.models import User, UserForm
import random
import csv


def home(request):
    users = User.objects.all()
    return render_to_response('index.html', {'data': users})


def add(request):
    if request.method == "POST":
        form_user = UserForm(request.POST)
        form_user.is_valid()
        data = form_user.cleaned_data
        if form_user.is_valid() == True:
            obj = User(
                first_name=data['first_name'],
                last_name=data['last_name'],
                birthday=data['birthday'],
                random_number=random.randint(1, 100),
                )
            obj.save()
        return HttpResponseRedirect("/")
    return render_to_response(
        'add.html', {'form': UserForm},
        context_instance=RequestContext(request))


def remove(request):
    if request.method == "GET":
        print request.GET.get('id')
        User.objects.get(id=request.GET.get('id')).delete()
    return HttpResponseRedirect('/')


def generate_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['First name', 'Last name', 'Birthday'])
    for obj in User.objects.all():
        writer.writerow([
            obj.first_name.encode("utf-8"),
            obj.last_name.encode("utf-8"),
            obj.birthday])

    return response


def edit(request):
    if request.method == "GET":
        user_for_id = User.objects.get(id=request.GET.get('id'))
        UserFormEdit = UserForm(
            {'first_name': user_for_id.first_name,
             'last_name': user_for_id.last_name,
             'birthday': user_for_id.birthday}
             )
        return render_to_response(
            'edit.html', {'form': UserFormEdit},
            context_instance=RequestContext(request))
    if request.method == "POST":
        user_for_id = User.objects.get(id=request.GET.get('id'))
        print user_for_id
        form_user = UserForm(request.POST)
        form_user.is_valid()
        data = form_user.cleaned_data
        if form_user.is_valid() == True:
            user_for_id.first_name = data['first_name']
            user_for_id.last_name = data['last_name']
            user_for_id.birthday = data['birthday']
            user_for_id.save()
        return HttpResponseRedirect('/')
