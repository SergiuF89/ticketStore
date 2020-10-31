from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DetailView
from .models import UserProfile
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404



class ProfileView(LoginRequiredMixin, UpdateView):
      model = UserProfile
      fields = ['first_name', 'last_name', 'gender', 'birth_date']
      template_name = 'profile_update.html'
      context_object_name = 'profile'
      success_url = reverse_lazy('core:home')

      def get_context_data(self, *, object_list=None, **kwargs):
            context = super(ProfileView, self).get_context_data(**kwargs)
            context['users'] = UserProfile.objects.all()
            return context

      def get(self, request, *args, **kwargs):
            user_id = request.user.pk
            profile_id = kwargs['pk']
            if user_id != profile_id:
                  return HttpResponseForbidden()
            else:
                  return super(ProfileView, self).get(request, *args, **kwargs)

      def post(self, request, pk):
            user = UserProfile.objects.filter(pk=pk)
            if user.filter(pk=request.user.pk):
                  items = request.POST.dict()
                  del items['csrfmiddlewaretoken']
                  user.update(**items)
                  return HttpResponseRedirect(reverse('core:profile-view', args=(pk,)))
            else:
                  return HttpResponse('You are not authoried to make this change!', status=401)

      # def form_valid(self, form):
      #       form.instance.manager = self.request.user
      #       return super().form_valid(form)


class UserProfileView(DetailView):
      model = UserProfile
      template_name = 'profile.html'
      context_object_name = 'user_profile'
      
      def get(self, request, *args, **kwargs):
            user_id = request.user.pk
            profile_id = kwargs['pk']
            if user_id != profile_id:
                  return HttpResponseForbidden()
            else:
                  return super(UserProfileView, self).get(request, *args, *kwargs)


