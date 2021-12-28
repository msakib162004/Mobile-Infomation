from django.contrib import admin
from .models import MobileInformation
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "password", "email")


class MobileInformationAdmin(admin.ModelAdmin):
    list_display = ("id", "Brand_Name", "Model", "Color", "JAN_Code", "Image")

#
# class ClosedAuctionAdmin(admin.ModelAdmin):
#     list_display = ("id", "close_a_id", "close_u_id")


# admin.site.register(User, UserAdmin)
# admin.site.register(AuctionList, AuctionAdmin)
admin.site.register(MobileInformation)
# admin.site.register(WatchList)
# admin.site.register(Bid)
# admin.site.register(ClosedAuction, ClosedAuctionAdmin)
