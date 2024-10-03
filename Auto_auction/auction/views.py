from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
import datetime
from django.db.models import Avg, Max, Min, Sum
from django.utils import timezone



# Create your views here.
def Home(request):
  
    return render(request,'carousel.html')

def Login_User(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        sign = ""
        if user:
            try:
                sign = Bidder.objects.get(user=user)
            except:
                pass
            if sign:
                login(request, user)  #create a session
                error = "pat"
            else:
                login(request, user)
                error = "pat1"
        else:
            error="not"
            
    d = {'error': error}
    return render(request, 'login.html', d)

def Login_Admin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = "yes"
        else:
            error = "not"

    d = {'error': error}
    return render(request, 'loginadmin.html', d)
 
def Signup_User(request):
    error = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        p = request.POST['pwd']
        con = request.POST['contact']
        add = request.POST['add']
        d2 = request.POST['dob']
        reg = request.POST['reg']
        i = request.FILES['image']
        user = User.objects.create_user(email=e, username=u, password=p, first_name=f,last_name=l)
        
        if reg == "Bidder":
            sign = Bidder.objects.create(user=user,contact=con,address=add,dob=d2,image=i)
        else:
            sign = Auction_User.objects.create(user=user,contact=con,address=add,dob=d2,image=i)
        error = True
    d = {'error':error}
    return render(request,'signup.html',d)

def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')
     
'''def new():
    status = Status.objects.get(status="pending")
    new_pro = Product.objects.filter(status=status)
    return new_pro'''
  

def Logout(request):
    logout(request)
    return redirect('home')



def Change_Password1(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error=""
    user = User.objects.get(id=request.user.id)
    pro=""
    try:
        pro = Bidder.objects.get(user=user)
        if pro:
            error = "pat"
    except:
        pro = Auction_User.objects.get(user=user)
        
    terror = ""
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            terror = "yes"
        else:
            terror = "not"
    d = {'terror':terror,'error': error}
    return render(request,'change_password1.html',d)

def Edit_Profile1(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error=""
    user1 = User.objects.get(id=request.user.id) #retrive id
    pro=""
    try:
        pro = Bidder.objects.get(user=user1) #retrive data of row using forain key -user
        if pro:
            error="pat"
    except:
        pro = Auction_User.objects.get(user=user1)
    
    terror = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        try:
            i = request.FILES['image']
            pro.image=i
            pro.save()
        except:
            pass
        ad = request.POST['address']
        e = request.POST['email']
        con = request.POST['contact']
        pro.address = ad
        pro.contact=con
        user1.first_name = f
        user1.last_name = l
        user1.email = e
        user1.save()
        pro.save()
        terror = True
    d = {'terror':terror,'pro':pro,'data':pro,'error': error}
    return render(request, 'edit_profile1.html',d)

def Profile1(request):
    error=""
    user = User.objects.get(id=request.user.id)
    pro=""
    try:
        pro = Bidder.objects.get(user=user)
        if pro:
            error = "pat"
    except:
        pro = Auction_User.objects.get(user=user)
        
    d = {'pro':pro,'error': error}
    return render(request,'profile1.html',d)


def Feedback(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error=""
    date1 = datetime.date.today()
    user = User.objects.get(id=request.user.id)
    pro = ""
    try:
        pro = Bidder.objects.get(user=user)
        if pro:
            error = "pat"
    except:
        pro = Auction_User.objects.get(user=user)
    
       
    terror = False
    if request.method == "POST":
        d = request.POST['date']
        u = request.POST['uname']
        e = request.POST['email']
        con = request.POST['contact']
        m = request.POST['desc']
        
      
        Send_Feedback.objects.create(profile=user, date=d, message1=m)
        terror = True
    d = {'pro': pro,'date1': date1,'terror':terror,'error': error}
    return render(request, 'feedback.html', d)

def Add_Product(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    user = User.objects.get(username=request.user.username)
    sell = Auction_User.objects.get(user=user)
    terror = False
    if request.method == "POST":
        c = request.POST['cat'] 
        p = request.POST['p_name']
        pr = request.POST['price']
        i = request.FILES['image']
        sett1 = request.POST['time']
        sed1 = request.POST['date']
        
        
        pro1=Product.objects.create(status="pending",auction_date=sed1,auction_time=sett1,category=c,name=p, min_price=pr, images=i)
        auc=Aucted_Product.objects.create(product=pro1,user=sell)
        terror = True
    d = {'terror':terror}
    return render(request, 'add_product.html',d)


def All_product(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        data = Bidder.objects.get(user=user)
        if data:
            error = "pat"
    except:
        data = Auction_User.objects.get(user=user)

    pro = Aucted_Product.objects.filter(user=data)
    d = {'pro':pro,'error':error}
    return render(request,'All_prodcut.html',d)
    
def Bidding_Status(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    data = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        data = Bidder.objects.get(user=user)
        if data:
            error = "pat"
    except:
        data = Auction_User.objects.get(user=user)
 
    pro = Participant.objects.filter(user=data)
    d = {'pro':pro,'error':error}
    return render(request,'bidding_status.html',d)

def Bidding_Status2(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    data = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        data = Bidder.objects.get(user=user)
        if data:
            error = "pat"
    except:
        data = Auction_User.objects.get(user=user)
    
    pro1 =  Aucted_Product.objects.filter(user=data)
    d = {'pro':pro1,'error':error}
    return render(request,'bidding_status2.html',d)    

def view_popup(request):
    if not request.user.is_authenticated:
        return redirect('login_user')
    error=True
    d = {'error':error}
    return render(request,'view_popup.html',d)


def view_auction(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_user')
    
    user = User.objects.get(username=request.user.username)
    error = ""
    
    try:
        data = Bidder.objects.get(user=user)
        error = "pat"
    except Bidder.DoesNotExist:
        data = Auction_User.objects.get(user=user)
    
    if request.method == "POST":
        pro1 = Product.objects.get(id=pid)
        auc = Aucted_Product.objects.get(product=pro1)
        Participant.objects.create(user=data, aucted_product=auc)
    
    # Get products with status "pending"
    pro = Product.objects.filter(status="pending")
    if not pro:
        message1 = "No Any Bidding Product"
    else:
        message1 = ""

    one_hour = datetime.timedelta(hours=1)
    today = datetime.date.today()
    now_datetime = datetime.datetime.now()
    now_time = now_datetime.time()

    print(f"Today: {today}")
    

    # Update the temp field based on the auction date and time
    for i in pro:
        if i.auction_date == today:
            if now_time < i.auction_time:
                i.temp = 1  # Auction is upcoming today
            elif now_time >= i.auction_time:
                i.temp = 2  # Auction is live
            else:
                i.temp = 0  # Auction already happened
        elif i.auction_date < today:
            i.temp = 3  # Auction is over
        else:
            i.temp = 0  # Auction is in the future
        i.save()
        

    context = {
        'pro': pro,
        'error': error,
        'message1': message1,
    }
    return render(request, 'view_auction.html', context)


from django.utils import timezone
import pytz
import datetime

def convert_to_ist(dt):
    """Convert naive or UTC datetime to IST timezone."""
    ist = pytz.timezone('Asia/Kolkata')
    if dt.tzinfo is None:
        dt = timezone.make_aware(dt, timezone.utc)
    return dt.astimezone(ist)

def Start_Auction(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_user')

    user = User.objects.get(username=request.user.username)
    error = ""
    terror = ""

    try:
        data = Bidder.objects.get(user=user)
        error = "pat"
    except Bidder.DoesNotExist:
        data = Auction_User.objects.get(user=user)

    # Fetch the product and related Aucted_Product
    pro4 = Product.objects.get(id=pid)
    c = Aucted_Product.objects.get(product=pro4)

    # Calculate the start and end times of the auction
    auction_start_time = datetime.datetime.combine(pro4.auction_date, pro4.auction_time)
    end_time = auction_start_time + datetime.timedelta(hours=1)
    end2 = end_time.time().strftime("%H:%M")

 

    # Fetch participant details
    pro1 = Participant.objects.filter(user=data, aucted_product=c).first()

    if not pro1:
        return redirect('view_popup')

    # Fetch all participants for this auction, ordered by the highest bid
    pro2 = Participant.objects.filter(aucted_product=c).order_by('-new_price')

    # Handle bid submission
    if request.method == "POST":
        new_price = request.POST.get("price")
        if new_price:
            pro1.new_price = new_price
            pro1.save()

    # Check auction timing to update the auction status
    current_datetime = timezone.now()
    current_datetime = convert_to_ist(current_datetime)  # Convert to IST
    current_time = current_datetime.time()

    if pro4.auction_date == current_datetime.date():
        if auction_start_time.time() <= current_time < end_time.time():
            pro4.temp = 2  # Auction is ongoing
        else:
            pro4.temp = 3  # Auction has ended        
            terror = "expire"
    elif pro4.auction_date < current_datetime.date():
        pro4.temp = 3  # Auction has ended
        terror = "expire"

    pro4.save()
    
    # Determine the winner if the auction has ended
    if pro4.temp == 3:
        if pro2.exists():
            win1 = pro2.first()
            c.winner = win1.user.user.username
            c.save()

        for participant in pro2:
            try:
                if participant.user.user.username == c.winner:
                    participant.result = "Winner"
                    participant.payment = "pending"
                else:
                    participant.result = "Defeat"
                    participant.payment = "reject"
                
                participant.save()
                participant.refresh_from_db()
            
            except Exception as e:
                print(f"Error saving participant {participant.user.user.username}: {e}")


            # Update product status
            pro4.status = "Done"
            pro4.save()
    
    context = {
        'pro': pro1,
        'pro2': pro2,
        'end2': end2,
        'error': error,
        'terror': terror,
    }
    return render(request, 'start_auction.html', context)

def product_detail(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_user')
    
    user = User.objects.get(username=request.user.username)
    error = ""
    
    try:
        data = Bidder.objects.get(user=user)
        error = "pat"
    except Bidder.DoesNotExist:
        data = Auction_User.objects.get(user=user)
  
    # Fetch the product based on the given id
    pro = Product.objects.get(id=pid)
    
    # Calculate the end time of the auction (1 hour after the start time)
    auction_start_time_ = pro.auction_time
    auction_start_time= (datetime.datetime.combine(datetime.date.today(), auction_start_time_) + datetime.timedelta(hours=12)).time()

    end_time_hour = (auction_start_time.hour + 1) % 24
    end_time = auction_start_time.replace(hour=end_time_hour)

    # Fetch the Aucted_Product instance related to this product
    pro1 = Aucted_Product.objects.get(product=pro)
    
    context = {
        'pro': pro,
        'pro1': pro1,
        'error': error,
        'end2': end_time.strftime("%H:%M"),
    }
    return render(request, 'product_detail.html', context)


def Winner1(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_user')

    user = User.objects.get(username=request.user.username)
    error = ""

    try:
        data = Bidder.objects.get(user=user)
        error = "pat"
    except Bidder.DoesNotExist:
        data = Auction_User.objects.get(user=user)
  

    pro2 = Product.objects.get(id=pid)


    try:
        au = Aucted_Product.objects.get(product=pro2)
        
    except Aucted_Product.DoesNotExist:
        au = None
        
    
    # Directly check for the "Winner" result in the Participant model
    if au:
        pro1 = Participant.objects.filter(aucted_product=au, result="Winner").first()
        
        if pro1:
            terror = False
        else:
            terror = True
    else:
        pro1 = None
        terror = True
    
    
    context = {
        'pro': pro1,
        'error': error,
        'terror': terror
    }
    return render(request, 'winner2.html', context)

def Winner2(request, pid):
    if not request.user.is_authenticated:
        return redirect('login_user')

    user = User.objects.get(username=request.user.username)
    error = ""
    
    try:
        data = Bidder.objects.get(user=user)
        error = "pat"
    except Bidder.DoesNotExist:
        data = Auction_User.objects.get(user=user)
        
    pro2 = Product.objects.get(id=pid)
    au = Aucted_Product.objects.get(product=pro2)

    # Directly filter the Participant based on the 'Winner' result string
    pro1 = Participant.objects.get(aucted_product=au, result="Winner")
    
    context = {
        'pro': pro1,
        'error': error
    }
    return render(request, 'winner2.html', context)
def All_product(request):
    if not request.user.is_authenticated:
        return redirect('login_user')

    data = None
    user = User.objects.get(username=request.user.username)
    error = ""
    
    try:
        data = Bidder.objects.get(user=user)
        print(f"Bidder data found: {data}")
        error = "pat"
    except Bidder.DoesNotExist:
        try:
            data = Auction_User.objects.get(user=user)
            print(f"Auction_User data found: {data}")
        except Auction_User.DoesNotExist:
            print("No Bidder or Auction_User data found.")
            data = None
    
    if data:
        pro = Aucted_Product.objects.filter(user=data)
        print(f"Aucted_Product queryset: {pro}")
    else:
        pro = None
        print("No user data found, pro is set to None.")
    
    d = {'pro': pro, 'error': error}
    return render(request, 'All_prodcut.html', d)

def Participated_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_user')
    data = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        data = Bidder.objects.get(user=user)
        if data:
            error = "pat"
    except:
        data = Auction_User.objects.get(user=user)
   
    auc = Aucted_Product.objects.get(id=pid)
    pro1 =  Participant.objects.filter(aucted_product=auc)
    message1=""
    if not pro1:
        message1 = "No Bidder"
    d = {'part':pro1,'error':error,'message1':message1}
    return render(request,'particpated_user.html',d)