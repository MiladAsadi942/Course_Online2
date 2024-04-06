from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from web.models import Catagory,Course,Customer,Contact,About,Comment
from .models import User
from django.urls import reverse_lazy,reverse
from django.views.generic import UpdateView,CreateView
from django.contrib.auth import login,logout
from accounts.form import LoginForm,register
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from .mixens import FieldsMixin,Website_mixin,Mixin_Customer,Contact_Mixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            
            return redirect('accounts:dashboard')
    form = register()
    return render(request,'register/index.html',{'form':form})



def Login(request):
    if request.method == 'POST':
        redirect_to = request.GET.get('next', 'accounts:dashboard')
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect(redirect_to)
        else:
            return HttpResponse('data is Note Valid')
    form = LoginForm()
    return render(request,'login/index.html',{'form':form})



def Logout_user(request):
    logout(request)
    return redirect('web:website')



@login_required(login_url='/accounts/login/')
def Dashboard(request):
    count_users = User.objects.all().count()
    count_course = Course.objects.all().count()
    count_contact = Contact.objects.all().count()
    count_customer = Customer.objects.all().count()
    cont = Contact.objects.filter(active=False).count()
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.Techer:


            course = Customer.objects.all()
            contax = {
            'course':course,
            'count_users':count_users,
            'count_course':count_course,
            'count_contact':count_contact,
            'count_customer':count_customer
            }
            return render(request,'dashboard/index.html',contax)
    
    course = Customer.objects.filter(user=request.user)
    contax = {
            'course':course,
            'cont':cont
            }
    return render(request,'dashboard/index.html',contax)
    


class Update_User(LoginRequiredMixin,UpdateView):
    model = User
    template_name = 'dashboard/Update_user.html'
    fields = ['phone','address','Image','Techer','username']
    def get_form(self, form_class=None):
        form = super(Update_User, self).get_form(form_class)
        form['phone'].field.widget.attrs.update({'class' : 'form-control'})
        form['address'].field.widget.attrs.update({'class' : 'form-control'})
        form['Image'].field.widget.attrs.update({'class' : 'form-control'})
        form['Techer'].field.widget.attrs.update({'class' : 'form-control'})
        form['username'].field.widget.attrs.update({'class' : 'form-control'})
        return form
    success_url = reverse_lazy('accounts:dashboard')
@login_required(login_url='/accounts/login/')    
def Delete_course(request,id):
    delete_course = Course.objects.filter(id=id)
    delete_course.delete()
    return redirect('accounts:dashboard')
def List_Course(request):
    if request.user.is_authenticated:
        if request.user.is_superuser or request.user.Techer:
            course = Course.objects.all()
            contax = {
                'course':course }
            return render(request,'dashboard/list_Course.html',contax)
    
    return HttpResponse('You Dont Access The Page')
class Update_Course(LoginRequiredMixin,FieldsMixin,UpdateView):
    model = Course
    template_name = 'dashboard/Update_course.html'
    fields = '__all__'
    def get_form(self, form_class=None):
        form = super(Update_Course, self).get_form(form_class)
        form['title'].field.widget.attrs.update({'class' : 'form-control'})
        form['video'].field.widget.attrs.update({'class' : 'form-control'})
        form['image'].field.widget.attrs.update({'class' : 'form-control'})
        form['about'].field.widget.attrs.update({'class' : 'form-control','id':'summernote'})
        form['grammer'].field.widget.attrs.update({'class' : 'form-control'})
        form['catagorey'].field.widget.attrs.update({'class' : 'form-control'})
        form['user'].field.widget.attrs.update({'class' : 'form-control'})
       
        
        return form
    success_url = reverse_lazy('accounts:list_course')


class Create_Course(LoginRequiredMixin,FieldsMixin,CreateView):
    model = Course
    template_name = 'dashboard/Update_course.html'
    fields = '__all__'
    def get_form(self, form_class=None):
        form = super(Create_Course, self).get_form(form_class)
        form['title'].field.widget.attrs.update({'class' : 'form-control'})
        form['video'].field.widget.attrs.update({'class' : 'form-control'})
        form['image'].field.widget.attrs.update({'class' : 'form-control'})
        form['about'].field.widget.attrs.update({'class' : 'form-control','id':'summernote'})
        form['grammer'].field.widget.attrs.update({'class' : 'form-control'})
        form['catagorey'].field.widget.attrs.update({'class' : 'form-control'})
        form['user'].field.widget.attrs.update({'class' : 'form-control'})
        return form
    def get_initial(self,*args,**kwargs):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['milad'] = 'Create Course'
        return context
    success_url = reverse_lazy('accounts:dashboard')

class Add_Catagorey(LoginRequiredMixin,CreateView):
    model = Catagory
    template_name = 'dashboard/Add_catagorey.html'
    fields = '__all__'
    def get_form(self, form_class=None):
        form = super(Add_Catagorey, self).get_form(form_class)
        form['name'].field.widget.attrs.update({'class' : 'form-control'})
        form['image'].field.widget.attrs.update({'class' : 'form-control'})
        return form
    success_url = reverse_lazy('accounts:dashboard')

@login_required(login_url='/accounts/login/')
def List_Catagorey(request):
    catagorey = Catagory.objects.all()
    contax = {
        'catagorey':catagorey
    }
    return render(request,'dashboard/List_catagorey.html',contax)
@login_required(login_url='/accounts/login/')
def Delete_catagorey(request,id):
    delete_catagorey = Catagory.objects.filter(id=id)
    delete_catagorey.delete()
    return redirect('accounts:list_catagorey')

class Update_Catagorey(LoginRequiredMixin,UpdateView):
    model = Catagory
    template_name = 'dashboard/Add_catagorey.html'
    fields = '__all__'
    def get_form(self, form_class=None):
        form = super(Update_Catagorey, self).get_form(form_class)
        form['name'].field.widget.attrs.update({'class' : 'form-control'})
        form['image'].field.widget.attrs.update({'class' : 'form-control'})
        return form
    success_url = reverse_lazy('accounts:list_catagorey')

@login_required(login_url='/accounts/login/')
def List_contact(request):
    if request.user.is_superuser or request.user.Techer:

        contact = Contact.objects.all()
        cont = Contact.objects.filter(active=False).count()
        contact_false = Contact.objects.all().update(active=True)
        contax = {
        'contact':contact,
        'cont':cont
        }
        return render(request,'dashboard/contact_list.html',contax)
    else:
        return HttpResponse('You Dont Access The Page')

@login_required(login_url='/accounts/login/')
def delete_contact(request,id):
    delete_c = Contact.objects.get(id=id)
    delete_c.delete()
    return redirect('accounts:list_contact')

class Update_contact(LoginRequiredMixin,Contact_Mixin,UpdateView):
    model = Contact
    template_name = 'dashboard/Update_contact.html'
    fields = '__all__'
    def get_form(self, form_class=None):
        form = super(Update_contact, self).get_form(form_class)
        form['Name'].field.widget.attrs.update({'class' : 'form-control','placeholder':'Your Name'})
        form['Email'].field.widget.attrs.update({'class' : 'form-control','placeholder':'Your E-mail'})
        form['Sunjects'].field.widget.attrs.update({'class' : 'form-control','placeholder':'Your Subjects'})
        form['Message'].field.widget.attrs.update({'class' : 'form-control','placeholder':'Your Message','id':'summernote'})
        form['active'].field.widget.attrs.update({'class' : 'form-control'})
        return form
    success_url = reverse_lazy('accounts:list_contact')


@login_required(login_url='/accounts/login/')
def List_user(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            users = Customer.objects.all()
            queryset = Customer.objects.filter().select_related('user').values('user__username','user__id','user__Image','user__email','user__phone','user__address').distinct()
            
            for item in queryset:
                print(item['user__Image'])
                

        else:
            return HttpResponse('You Dont Acceese The Page')
    contax = {
        'users':users,
        'queryset':queryset
        
    }
    return render(request,'dashboard/parvalege_user.html',contax)
@login_required(login_url='/accounts/login/')
def Parvelege(request,id):
    Users = User.objects.filter(id=id)
    Users.update(Techer=False)
    return redirect('accounts:list_user')
@login_required(login_url='/accounts/login/')
def detail_customer(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            use = Customer.objects.filter(user__id=id)
        else:
            return HttpResponse('You Dont Access The Page')
    
    contax = {
        "use":use,
        
    }
    return render(request,'dashboard/detail_customer_p.html',contax)
@login_required(login_url='/accounts/login/')
def True_customer(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            tru = Customer.objects.filter(id=id).update(pro=True)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else : 
            return HttpResponse('you dont Access The Page')
@login_required(login_url='/accounts/login/')
def False_customer(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            fal = Customer.objects.filter(id=id).update(pro=False)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponse('You Dont Access The Page')




def Par_Create_User(request):
    if request.method == 'POST':
        check = request.POST.getlist('check[]')
        for j in check:
            if j:
                users = User.objects.filter(id=j)
                users.update(Techer=True)
                print(j)
            else:
                users = User.objects.filter(id=j)
                users.update(Techer=False)
                print(j)


def access_user(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            users = User.objects.filter(id=id)
            users.update(Techer=True)
    
    return redirect('accounts:access')

def access_user_False(request,id):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            users = User.objects.filter(id=id)
            users.update(Techer=False)
    
    return redirect('accounts:access')

def Accessorey(request):
    user = User.objects.all()

    contax = {
        'users':user
    }
    return render(request,'dashboard/Accessorey.html',contax)    


class Update_Customer(Mixin_Customer,UpdateView):
    model = Customer
    template_name = 'dashboard/update_customer.html'
    fields = '__all__'
    def get_form(self, form_class=None):
        form = super(Update_Customer, self).get_form(form_class)
        form['user'].field.widget.attrs.update({'class' : 'form-control'})
        form['Course'].field.widget.attrs.update({'class' : 'form-control'})    
        return form
    success_url = reverse_lazy('accounts:dashboard')

class Update_Website_specifications(Website_mixin,UpdateView):
    model = About
    template_name = 'dashboard/Update_About_web.html'
    fields  = '__all__'
    def get_form(self, form_class=None):
        form = super(Update_Website_specifications, self).get_form(form_class)
        form['Title'].field.widget.attrs.update({'class' : 'form-control'})
        form['bio'].field.widget.attrs.update({'class' : 'form-control'})
        form['logo'].field.widget.attrs.update({'class' : 'form-control'})
        form['email'].field.widget.attrs.update({'class' : 'form-control'})
        form['phone'].field.widget.attrs.update({'class' : 'form-control'})
        form['address'].field.widget.attrs.update({'class' : 'form-control'})    
        return form
    success_url = reverse_lazy('accounts:dashboard')


def Check_Comments(request):
    course = Course.objects.all()
    lis = []
    comment = Comment.objects.all()
    contax = {
        'course':course,
        'comment':comment
        }
    return render(request,'dashboard/check_comments.html',contax)
