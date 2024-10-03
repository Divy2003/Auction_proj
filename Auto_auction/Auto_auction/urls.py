
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from auction.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="home"),
    path('login_user',Login_User,name="login_user"),
    path('login_admin',Login_Admin,name="login_admin"),
    path('signup', Signup_User,name="signup"),
    path('logout', Logout, name="logout"),
    # path('trainer_home',Auction_User,name="trainer_home"),
   # path('contact',Contact,name="conRtact"),
    path('about',About,name="about"),
    path('contact',Contact,name="contact"),
    path('edit_profile1',Edit_Profile1,name="edit_profile1"),
    path('change_password1',Change_Password1,name="change_password1"),
   # path('admin_home', Admin_Home,name="admin_home"),
    path('feedback', Feedback,name="feedback"),
   #path('user_home',Bidder_Home,name="user_home"),
    path('profile1', Profile1, name='profile1'),
    path('add_product', Add_Product,name="add_product"),
    path('all_product', All_product, name='all_product'),
    path('bidding_status', Bidding_Status, name='bidding_status'),
    path('bidding_status2', Bidding_Status2, name='bidding_status2'),
    path('view_auction(<int:pid>)', view_auction, name='view_auction'),
    path('product_detail(<int:pid>)', product_detail, name='product_detail'),
    path('winner1(<int:pid>)', Winner1,name='winner1'),
    path('start_auction(<int:pid>)', Start_Auction, name='start_auction'),
    path('winner2(<int:pid>)', Winner2,name='winner2'),
    path('view_popup', view_popup,name="view_popup"),
    path('particpated_user(<int:pid>)', Participated_user, name='particpated_user'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
