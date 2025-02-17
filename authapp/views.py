from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from authapp.models import Contact,MembershipPlan,Trainer,Enrollment,Attendance
# Create your views here.
def Home(request):
    return render(request,"index.html")

def signup(request):
    if request.method=="POST":
        username = request.POST.get('usernumber')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Check if the username is exactly 10 characters long
        if len(username) != 10:
            messages.info(request, "Phone Number must be 10 digits")
            return redirect('signup')

        # Check if passwords match
        if pass1 != pass2:
            messages.info(request, "Passwords do not match")
            return redirect('signup')

        # Check if the username (phone number) already exists
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Phone number is already taken")
            return redirect('signup')

        # Check if the email is already taken
        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email is already taken")
            return redirect('signup')

        # Create the new user
        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.save()
        messages.success(request, "User created successfully! Please log in.")
        return redirect('login')

    return render(request, "signup.html")


def handlelogin(request):
    if request.method == "POST":
        username = request.POST.get('usernumber')
        pass1 = request.POST.get('pass1')

        # Check if the username or password fields are empty
        if not username or not pass1:
            messages.error(request, "Please fill in both fields.")
            return redirect('login')

        # Authenticate the user
        myuser = authenticate(username=username, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful")
            return redirect('/')  # Redirect to the homepage or desired page after login
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')

    return render(request, "handlelogin.html")



def handleLogout(request):
            logout(request)
            messages.success(request, "Logout successful")
            return redirect('login')  # Redirect to the login page after logout

def about(request):
            return render(request,"about.html")

def services(request):
            return render(request,"services.html")

def trainer(request):
            return render(request,"trainer.html")

def attendance(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please LogIn and Try Again")
        return redirect('/login')

    SelectTrainer = Trainer.objects.all()
    context = {"SelectTrainer": SelectTrainer}

    if request.method == "POST":
        PhoneNumber = request.POST.get('PhoneNumber')
        Login = request.POST.get('loginTime')
        Logout = request.POST.get('logoutTime')
        SelectWorkout = request.POST.get('workout')
        TrainedBy = request.POST.get('trainer')

        query = Attendance(PhoneNumber=PhoneNumber, Login=Login, Logout=Logout, SelectWorkout=SelectWorkout, TrainedBy=TrainedBy)
        query.save()
        messages.warning(request, "Attendance Applied")
        return redirect('/attendance')
        
    return render(request, "attendance.html", context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        number = request.POST.get('num')
        desc = request.POST.get('desc')

        myquery = Contact(name=name, email=email, phonenumber=number, description=desc)
        myquery.save()

        messages.info(request, "Thanks For Contacting Us, We Will Get Back To You Soon")
        return redirect('/contact')
    
    return render(request, "contact.html")


def enroll(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please LogIn and Try Again")
        return redirect('/login')

    Membership = MembershipPlan.objects.all()
    SelectTrainer = Trainer.objects.all()
    context = {"Membership": Membership, "SelectTrainer": SelectTrainer}

    if request.method == "POST":
        FullName = request.POST.get('FullName')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        PhoneNumber = request.POST.get('PhoneNumber')
        DOB = request.POST.get('DOB')
        member = request.POST.get('member')
        trainer = request.POST.get('trainer')
        address = request.POST.get('address')

        query = Enrollment(FullName=FullName, Email=email, Gender=gender, PhoneNumber=PhoneNumber, DOB=DOB, 
                           SelectMembershipPlane=member, SelectTrainer=trainer, Address=address)
        query.save()
        messages.success(request, "Thanks For The Enrollment")
        return redirect('/join')

    return render(request, "enroll.html", context)
