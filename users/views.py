from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView
from .models import UserProfile
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404



class ProfileView(LoginRequiredMixin, UpdateView):
      model = UserProfile
      fields = '__all__'
      template_name = 'profile_update.html'
      context_object_name = 'profiles'
      success_url = reverse_lazy('core:home')

      def get(self, request, *args, **kwargs)
            
            user_pk = self.kwargs.get('pk')
            user_profile = UserProfile.objects.get(user__pk=user_pk)
            if self.request.user == user_profile:
                  return super(ProfileView,self).get(request,*args,**kwargs)
            else:
                  raise Http404
      
      
      def post(self, request, *args, **kwargs):
            
            user_pk = self.kwargs.get('pk')
            user_profile = UserProfile.objects.get(user__pk=user_pk)
            if self.request.user == user_profile:
                  user = UserProfile.objects.filter(pk=pk)
                  items = request.POST.dict()
                  del items['csrfmiddlewaretoken']
                  user.update(**items)
                  return HttpResponseRedirect(reverse('core:profile', args=(pk,)))
      
            else:
                  raise Http404

      
    
