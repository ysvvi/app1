from django.contrib import admin
from carts.admin import CartTabAdmin
#from orders.admin import OrderTabulareAdmin   , OrderTabulareAdmin

from users.models import User

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email",]
    search_fields = ["username", "email",]

    inlines = [CartTabAdmin,]
