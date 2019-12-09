from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Profile, Position, Council, OfficersTerm
from django.contrib import messages
from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, OfficersTermForm


class OfficersTerm(CreateView):
    model = OfficersTerm
    form_class = OfficersTermForm

    success_url = reverse_lazy('officers_term')

    def form_valid(self, form):
        return super().form_valid(form)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'council/register.html', {'form': form})


class ProfileList(ListView): 
    model = Profile

class ProfileDetail(DetailView): 
    model = Profile
    template_name = 'council/profile_detail.html'

class ProfileDetail13774(DetailView): 
    model = Profile
    template_name = 'council/profile_detail_13774.html'

class ProfileDetail15167(DetailView): 
    model = Profile
    template_name = 'council/profile_detail_15167.html'

class ProfileDetail15311(DetailView): 
    model = Profile
    template_name = 'council/profile_detail_15311.html'

class ProfileDetail16314(DetailView): 
    model = Profile
    template_name = 'council/profile_detail_16314.html'

class ProfileList13774(ListView): 
    model = Profile
    template_name = 'council/profile_list_13774.html'
    context_object_name = 'profiles'

class ProfileList15167(ListView): 
    model = Profile
    template_name = 'council/profile_list_15167.html'
    context_object_name = 'profiles'

class ProfileList15311(ListView): 
    model = Profile
    template_name = 'council/profile_list_15311.html'
    context_object_name = 'profiles'

class ProfileList16314(ListView): 
    model = Profile
    template_name = 'council/profile_list_16314.html'
    context_object_name = 'profiles'

class ProfileCreate(CreateView): 
    model = Profile
    fields = ['membership_number', 'council_number', 'council_name', 'first_name', 'middle_name', 'last_name', 'street_address', 'City_state_zip', 'first_degree_date', 'second_degree_date', 'third_degree_date', 
    'assembly_number', 'birth_date', 'reentry_date', 'membership_type', 'membership_class',  'email', 'phone', 'image']
    success_url = '/'

#update profile
class ProfileUpdate(UpdateView): 
    model = Profile
    fields = ['membership_number', 'council_number', 'council_name', 'first_name', 'middle_name', 'last_name', 'street_address', 'City_state_zip', 'first_degree_date', 'second_degree_date', 'third_degree_date', 
    'assembly_number', 'birth_date', 'reentry_date', 'membership_type', 'membership_class', 'email', 'phone', 'image']
    template_name = 'council/update_profile_form.html'
    success_url = '/'

class ProfileUpdate13774(UpdateView): 
    model = Profile
    fields = ['membership_number', 'council_number', 'council_name', 'first_name', 'middle_name', 'last_name', 'street_address', 'City_state_zip', 'first_degree_date', 'second_degree_date', 'third_degree_date', 
    'assembly_number', 'birth_date', 'reentry_date', 'membership_type', 'membership_class', 'email', 'phone', 'image']
    template_name = 'council/update_profile_form_13774.html'
    success_url = '/profile_list_13774'

class ProfileUpdate15167(UpdateView): 
    model = Profile
    fields = ['membership_number', 'council_number', 'council_name', 'first_name', 'middle_name', 'last_name', 'street_address', 'City_state_zip', 'first_degree_date', 'second_degree_date', 'third_degree_date', 
    'assembly_number', 'birth_date', 'reentry_date', 'membership_type', 'membership_class', 'email', 'phone', 'image']
    template_name = 'council/update_profile_form_15167.html'
    success_url = '/profile_list_15167'

class ProfileUpdate15311(UpdateView): 
    model = Profile
    fields = ['membership_number', 'council_number', 'council_name', 'first_name', 'middle_name', 'last_name', 'street_address', 'City_state_zip', 'first_degree_date', 'second_degree_date', 'third_degree_date', 
    'assembly_number', 'birth_date', 'reentry_date', 'membership_type', 'membership_class', 'email', 'phone', 'image']
    template_name = 'council/update_profile_form_15311.html'
    success_url = '/profile_list_15311'

class ProfileUpdate16314(UpdateView): 
    model = Profile
    fields = ['membership_number', 'council_number', 'council_name', 'first_name', 'middle_name', 'last_name', 'street_address', 'City_state_zip', 'first_degree_date', 'second_degree_date', 'third_degree_date', 
    'assembly_number', 'birth_date', 'reentry_date', 'membership_type', 'membership_class', 'email', 'phone', 'image']
    template_name = 'council/update_profile_form_16314.html'
    success_url = '/rofile_list_16314'

def load_council(request):
    council_id = request.GET.get('council')
    council_desc = Council.objects.filter(council_id=council_id).order_by('council')
    return render(request, 'council/desc_dropdown_list_options.html', {'council_desc': council_desc})

class ProfileDelete(DeleteView): 
    model = Profile
    success_url = '/'

def OfficersGuide(request):
    return render(request, 'council/OfficersGuide.html', {'title': "Kofc District N32"})

def LeadershipResource(request):
    return render(request, 'council/LeadershipResource.html', {'title': "Kofc District N32"})

def LeadershipProgramming(request):
    return render(request, 'council/LeadershipProgramming.html', {'title': "Kofc District N32"})

def LeadershipRecruitment(request):
    return render(request, 'council/LeadershipRecruitment.html', {'title': "Kofc District N32"})

def form(request):
    return render(request, 'council/form.html', {'title': "Kofc District N32"})

def family(request):
    return render(request, 'council/family.html', {'title': "Kofc District N32"})

def life(request):
    return render(request, 'council/life.html', {'title': "Kofc District N32"})

def faith(request):
    return render(request, 'council/faith.html', {'title': "Kofc District N32"})

def faiths(request):
    return render(request, 'council/faiths.html', {'title': "Kofc District N32"})

def community(request):
    return render(request, 'council/community.html', {'title': "Kofc District N32"})

def CommunityDisasterPreparation(request):
    return render(request, 'council/CommunityDisasterPreparation.html', {'title': "Kofc District N32"})

def CommunityRespondent(request):
    return render(request, 'council/CommunityRespondent.html', {'title': "Kofc District N32"})

def CommunityResources(request):
    return render(request, 'council/CommunityResources.html', {'title': "Kofc District N32"})

def CommunityIndividualResponse(request):
    return render(request, 'council/CommunityIndividualResponse.html', {'title': "Kofc District N32"})

class Coucil(ListView):
    model = Council
    template_name = 'council/base.html'
    context_object_name = 'councils'

