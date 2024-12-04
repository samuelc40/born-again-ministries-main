from django.shortcuts import render, redirect
from . forms import UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from . models import *

# Create your views here.

def index(request):
    return render(request, 'index.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST or None)

#         if form.is_valid():
#             new_user = form.save()
#             username = form.cleaned_data['username']
#             messages.success(request, f" Hey {username}, Your account has been created successfully.")
#             new_user = authenticate(username=form.cleaned_data['email'],
#                                     password=form.cleaned_data['password1'])
            
#             login(request, new_user)
#             return redirect('index')
    
#     else:
#         print("Something went wrong!!!")
#         form = UserRegistrationForm()

#     context = {
#         'form': form,
#     }

#     return render(request, 'register.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            # Create and save the user
            user = form.save()
            username = form.cleaned_data['username']

            messages.success(request, f"Hey {username}, Your account has been created successfully.")
            return redirect('signin')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    
    return render(request, 'register.html', context)

def login_view(request):

    context = {}
    
    if request.user.is_authenticated:
        messages.success(request, f"You are already logged in")
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"You are logged in {email}")
                return redirect('index')
            
            else:
                messages.warning(request, "User does not exist, Created an account!")
                error_msg = "Invalid credentials !"
                context['error_msg'] = error_msg
                
        except:
            messages.warning(request, "Invalid credentials !")
            error_msg = "Invalid credentials !"
            context['error_msg'] = error_msg
                
            

    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('signin')

def events(request):
    return render(request, 'events.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # If the request method is POST, it means the form is being submitted
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print("Name:", name)
        print("Phone:", phone)
        print("Message:", message)

        if name and phone and message:
            # Create a new Messages object and save it to the database
            contact_message = Messages(name=name, phone=phone, message=message)
            contact_message.save()

            return redirect('contact')  # Replace 'contact' with the URL or name of your contact page

    return render(request, 'contact.html')

def notice_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        # date = request.POST.get('date')
        # time = request.POST.get('time')
        desc = request.POST.get('desc')

        print("Name:", name)
        print("title:", title)
        # print("date:", date)
        # print("time:", time)
        print("desc:", desc)

        notice_form = Notices(name=name, title=title, desc=desc)
        notice_form.save()

        return redirect('notices')

    return render(request, 'notice_form.html')

def notices(request):
    notice = Notices.objects.all()
    context = {'notice': notice}
    return render(request, 'notices.html', context)

def notice_details(request, pk):
    notice = Notices.objects.get(id=pk)
    context = {'notice': notice}
    return render(request, 'notice_detail.html', context)

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         contacts = Messages(name=name, phone=phone, message=message)
#         contacts.save()
#         print('Message created successfully')
#     return render(request, 'contact.html')

# def news(request):
#     return render(request, 'news.html')

def create_superuser(request):
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin",
            email="adminalbin@gmail.com",
            password="adminalbin@123"
        )
        return HttpResponse("Superuser created!")
    return HttpResponse("Superuser already exists.")
