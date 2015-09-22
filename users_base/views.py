# -*- coding: utf-8 -*-
from django.shortcuts import \
    render_to_response, RequestContext, HttpResponseRedirect, HttpResponse, render
from users_base.models import User
import random
import csv
from forms import UserForm
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.messages import get_messages
from django.views.generic import View, DeleteView, UpdateView


def home(request):
    users = User.objects.all()
    storage = get_messages(request)
    for message in storage:
        print message
    return render_to_response(
        'index.html', {'data': users}, context_instance=RequestContext(request))


"""def add(request):
    if request.method == "POST":
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            data = form_user.cleaned_data
            form_user.save()
            messages.success(request, 'Profile added.')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Incorrect data.')
            return HttpResponseRedirect(reverse('add'))
    if request.method == "GET":
        return render_to_response(
            'add.html', {'form': UserForm},
            context_instance=RequestContext(request))"""


class AddUser(View):
    form_class = UserForm
    template_name = 'add.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile added.')
        else:
            messages.error(request, 'Incorrect data.')
        return render(request, self.template_name, {'form': form})


class DeleteUser(DeleteView):
    model = User
    template_name = "user_confirm_delete.html"
    success_url = "/"


"""def remove(request):
    if request.method == "GET":
        User.objects.get(id=request.GET.get('id')).delete()
        messages.success(request, 'Profile removed.')
    return HttpResponseRedirect(reverse('home'))"""


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


class UpdateUser(UpdateView):
    model = User
    template_name = "add.html"
    fields = ['first_name', 'last_name', 'birthday']
    success_url = "/"


"""def edit(request):
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
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            data = form_user.cleaned_data
            user_for_id.first_name = data['first_name']
            user_for_id.last_name = data['last_name']
            user_for_id.birthday = data['birthday']
            user_for_id.save()
            messages.success(request, 'Profile details updated.')
        else:
            messages.error(request, 'Incorrect data')
        return HttpResponseRedirect(reverse('home'))"""
