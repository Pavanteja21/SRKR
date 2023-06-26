from django.shortcuts import render

from django.contrib.auth.decorators import login_required 

from IT.models import Student

# Create your views here.
def Home(request):
    name="Revanth"
    names =['pavan','teja','venkata','kiran']
    student = Student.objects.all()
    Context={'name_1':name, 'names':names, 'student':student}
    return render(request,'home.html', Context)

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contacts.html')

def Product(request):
    return render(request,'product.html')

def Service(request):
    return render(request,'service.html')





from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from IT.models import(Student)

class StudentReg(CreateView):
    model=Student
    fields='__all__'
    template_name='CBV/studentreg.html'
    success_url="/"

class StudentList(ListView):
    model=Student
    template_name='CBV/studentlist.html'

class StudentDetail(DetailView):
    model=Student
    template_name='CBV/studentdetail.html'

class StudentUpdate(UpdateView):
    model=Student
    fields='__all__'
    template_name='CBV/studentupdate.html'
    success_url="/"

class StudentDelete(DeleteView):
    model=Student
    fields='__all__'
    template_name='CBV/studentdelete.html'
    success_url="/"

from django.shortcuts import render, redirect, get_object_or_404

from .models import Student
from .forms import StudentForm

def student(request):
    stu = Student.objects.all()
    context = {'stu': stu}
    return render(request, 'student.html', context)


def detail(request, id):
	data = Student.objects.get(id = id)	
	context = {'data':data}
	return render(request,'detail.html', context)


def update(request, id):
	obj = get_object_or_404(Student, id =id)
	form = StudentForm(request.POST or None, instance = obj)
	data = Student.objects.get(id = id)
	if form.is_valid():
		form.save()
		return redirect('student')

	context = {'form':form, 'data':data}
	return render(request,'update.html', context )


def delete(request, id):
	data = Student.objects.get(id = id)
	context = {'data':data}
	if request.method =='POST':
		data.delete()
		return redirect('form')
	return render(request,'delete.html', context )


def form(request):
    stu = Student.objects.all() 

    form = StudentForm
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student')  

    context = {'stu': stu, 'form': form}
    return render(request, 'form.html', context)

def rit(request):
	return render(request,'rit.html')

def get1(request):
	a = int(request.GET['num1'])
	b = int(request.GET['num2'])
	c = a+b
	context = {'c': c }
	return render(request,'get.html',context)

def post1(request):
	a = int(request.POST['num1'])
	b = int(request.POST['num2'])
	c = a+b
	context = {'c': c }
	return render(request,'post.html',context)

def index(request):
      return render(request, 'IT\index.html')

def about(request):
      return render(request, 'IT/about.html')

def blog(request):
      return render(request, 'IT/blog.html')

@login_required(login_url = 'IT:login')
def contact(request):
      return render(request, 'IT/contact.html')

def portfolio(request):
      return render(request, 'IT/portfolio.html')

def blog_single(request):
      return render(request, 'IT/blog-single.html')

from django.shortcuts import render, redirect
from .forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
#from django.contrib import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 


def register(request):
	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('IT:login')


	context = { 'form': form }
	return render (request, 'register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('IT:index')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('IT:login')