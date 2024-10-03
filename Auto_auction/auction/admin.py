from django.contrib import admin
from .models import Bidder, Auction_User, Status, Product, Aucted_Product, Payment, Participant, Send_Feedback

@admin.register(Bidder)
class BidderAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'address', 'contact', 'image')
    search_fields = ('user__username', 'contact')

@admin.register(Auction_User)
class AuctionUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'address', 'contact', 'image')
    search_fields = ('user__username', 'contact')

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('status',)
    search_fields = ('status',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'min_price', 'status', 'auction_date', 'auction_time')
    list_filter = ('category', 'status')
    search_fields = ('name', 'category')

@admin.register(Aucted_Product)
class AuctedProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'winner')
    search_fields = ('user__user__username', 'product__name')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('pay',)
    search_fields = ('pay',)



@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'aucted_product', 'new_price', 'result', 'payment', 'product')
    search_fields = ('user__user__username', 'aucted_product__product__name')

@admin.register(Send_Feedback)
class SendFeedbackAdmin(admin.ModelAdmin):
    list_display = ('profile', 'message1', 'date')
    search_fields = ('profile__username', 'message1', 'date')
