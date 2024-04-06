from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
from .models import Catagory,Course,Customer,Contact,About,Comment
from .form import Order
from django.views.generic import UpdateView,CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
from django.db.models import F, Sum,ExpressionWrapper,Sum
from django.db.models import IntegerField
from django.http import JsonResponse


# Create your views here.

def Home(request):
    course = Course.objects.all()
    about  = About.objects.get(id=1)
    contax = {
        'course':course,
        'about':about,
        
    }
    return render(request,'website/index.html',contax)

def Courses(request):
    course = Course.objects.all()
    contax = {
        'course':course
    }
    return render(request,'website/courses.html',contax)



def Website(request):
    
   
    catagorey = Catagory.objects.all()
    course = Course.objects.all()[:8]
    customer = Customer.objects.all()
    about  = About.objects.get(id=1)
    if request.method == 'POST':
        form = Order(request.POST)
        if form.is_valid():
            coursee = form.cleaned_data['course']
            customers = Customer.objects.create(Course=coursee,user=request.user)
            customers.save()
        redirect('web:website') 



    form = Order()
    contax = {

        'catagorey':catagorey,
        'course':course,
        'form':form,
        'about':about,
        'customer':customer
        
    }
    return render(request,'website/website/index.html',contax)

def detail_Catagorey(request,id):
    course = Course.objects.filter(catagorey__id=id)
    about = About.objects.get(id=1)
    customer = Customer.objects.all()
    contax = {
        'course':course,
        'about':about,
        'customer':customer
    }
    return render(request,'website/website/courses.html',contax)
@login_required(login_url='/accounts/login/')
def detail_Course(request,id):

    


    about = About.objects.get(id=1)
    detail = Course.objects.filter(id=id)
    comment = Comment.objects.filter(Course__id=id)
    cust = Customer.objects.filter(Course__id=id,user=request.user)
    d = Course.objects.get(id=id)
    if not cust:
        Cust = Customer.objects.create(user=request.user,Course=d,pro=False)
        Cust.save()
    m=False
    for j in cust:
        m = j.pro

    
    
    if request.method == 'POST':
        

        det = Course.objects.get(id=id)
        comt = request.POST.get('comment')
        commente = Comment.objects.create(user=request.user,Course=det,comment=comt)
        commente.save()
        img = commente.user.Image.url
        use = commente.Course.user.username
        ids = commente.id 
        return JsonResponse({'img':img , 'use':use,'ids':ids})
  
    contax = {
        'detail':detail,
        'm':m,
        'about':about,
        'comment':comment
        
    }
    return render(request,'website/website/single-course.html',contax)

def course(request):
    course = Course.objects.all()
    about = About.objects.get(id=1)
    customer = Customer.objects.all()
    contax = {
        'course':course,
        'about':about,
        'customer':customer
    }
    return render(request,'website/website/courses.html',contax)


def customer(request):
    first_name = request.POST.get('first_name')
    if request.method == 'POST':
        order = Order(request.POST)
        course = order.cleaned_data['course']
        customers = Customer.objects.create(first_name=first_name,Course=course,user=request.user)
        customers.save()
    redirect('web:website') 
        

class contact(CreateView):
    model = Contact
    template_name = 'website/website/contact.html'
    fields = '__all__'
    def get_form(self, form_class=None):
        form = super(contact, self).get_form(form_class)
        form['Name'].field.widget.attrs.update({'class' : 'form-control','placeholder':'Your Name'})
        form['Email'].field.widget.attrs.update({'class' : 'form-control','placeholder':'Your E-mail'})
        form['Sunjects'].field.widget.attrs.update({'class' : 'form-control','placeholder':'Your Subjects'})
        form['Message'].field.widget.attrs.update({'class' : 'form-control','placeholder':'Your Message'})
        form['active'].field.widget.attrs.update({'class' : 'form-control'})
        return form
    success_url = reverse_lazy('accounts:dashboard')
    
def Search_Course(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        course = Course.objects.filter(title__icontains=search)
        if course:
            return render(request,'website/website/courses.html',{'course':course,})
    return HttpResponse(search,'dont in Course')


def delete_Comments(request,id):
    if request.method == 'POST':
        comment = Comment.objects.filter(id=id)
        comment.delete()
        return JsonResponse({'status':'ok'})
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def About_us(request):
    detai_about = About.objects.get(id=1)
    catagorey = Catagory.objects.all()
    return render(request,'website/website/blog.html',{'detail_about':detai_about,'catagorey':catagorey})