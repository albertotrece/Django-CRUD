# -*- coding: utf-8 -*-

from crud.forms import UsuarioForm
from crud.models import Usuario
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView


class UserListView(ListView):
    model = Usuario
    template_name = 'users/index.html'
    context_object_name = 'userList'
    
    def get(self, request, *args, **kwargs):
        return ListView.get(self, request, *args, **kwargs)


class UserCreateView(CreateView):
    template_name = 'users/createUser.html'
    form_class = UsuarioForm
    
    def post(self, request, *args, **kwargs):        
        form = UsuarioForm(request.POST)
        if(form.is_valid()):
            form.save()      
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponse("O formulário é inválido. Por favor, insira corretamnete os dados.")
        
    def get(self, request, *args, **kwargs):
        return CreateView.get(self, request, *args, **kwargs)
    
    def get_success_url(self):
        return reverse('user_list')
    

class UserUpdateView(UpdateView):
    model = Usuario
    template_name = 'users/updateUser.html'
    form_class = UsuarioForm
    
    def get(self, request, *args, **kwargs):
        self.object = Usuario.objects.get(userId=self.kwargs['userId'])
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = get_object_or_404(Usuario, userId=self.kwargs['userId'])
        return obj

    def get_success_url(self):
        return reverse('user_list')
    
        
class UserDeleteView(DeleteView):
    model = Usuario
    template_name = 'users/deleteUser.html'
    
    def get_object(self, queryset=None):
        obj = get_object_or_404(Usuario, userId=self.kwargs['userId'])
        return obj
    
    def get_success_url(self):
        return reverse('user_list')