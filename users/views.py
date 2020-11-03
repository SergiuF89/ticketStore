from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView
from .models import UserProfile
from core.models import OrderItem, Order
from django.http import HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin
from core.forms import EditProfileForm

class ProfileView(LoginRequiredMixin, UpdateView):
      model = UserProfile
      form_class = EditProfileForm
      template_name = 'profile_update.html'
      context_object_name = 'profile'


      def get_success_url(self):
            user_id = self.kwargs['pk']
            return reverse_lazy('core:profile-view', kwargs={'pk':user_id})

      def get(self, request, *args, **kwargs):
            user_id = request.user.pk
            profile_id = kwargs['pk']
            if user_id != profile_id:
                  return HttpResponseForbidden()
            else:
                  return super(ProfileView, self).get(request, *args, **kwargs)


class UserProfileView(DetailView):
      model = UserProfile
      template_name = 'profile.html'
      context_object_name = 'user_profile'

      def get_context_data(self, *, object_list=None, **kwargs):
            context = super(UserProfileView, self).get_context_data(**kwargs)
            context['orders'] = Order.objects.all()
            context['order_item'] = OrderItem.objects.all()
            return context
      
      def get(self, request, *args, **kwargs):
            user_id = request.user.pk
            profile_id = kwargs['pk']
            if user_id != profile_id:
                  return HttpResponseForbidden()
            else:
                  return super(UserProfileView, self).get(request, *args, *kwargs)



