from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Coupon, Refund, BillingAddress, Category, Slide


# # Register your models here.


# def make_refund_accepted(modeladmin, request, queryset):
#     queryset.update(refund_requested=False, refund_granted=True)


# make_refund_accepted.short_description = 'Update orders to refund granted'


# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['user',
#                     'ordered',
#                     'being_delivered',
#                     'received',
#                     'refund_requested',
#                     'refund_granted',
#                     'shipping_address',
#                     'billing_address',
#                     'payment',
#                     'coupon'
#                     ]
#     list_display_links = [
#         'user',
#         'shipping_address',
#         'billing_address',
#         'payment',
#         'coupon'
#     ]
#     list_filter = ['user',
#                    'ordered',
#                    'being_delivered',
#                    'received',
#                    'refund_requested',
#                    'refund_granted']
#     search_fields = [
#         'user__username',
#         'ref_code'
#     ]
#     actions = [make_refund_accepted]


# class AddressAdmin(admin.ModelAdmin):
#     list_display = [
#         'user',
#         'street_address',
#         'apartment_address',
#         'country',
#         'zip',
#         'address_type',
#         'default'
#     ]
#     list_filter = ['default', 'address_type', 'country']
#     search_fields = ['user', 'street_address', 'apartment_address', 'zip']


# def copy_items(modeladmin, request, queryset):
#     for object in queryset:
#         object.id = None
#         object.save()


# copy_items.short_description = 'Copy Items'


# class ItemAdmin(admin.ModelAdmin):
#     list_display = [
#         'title',
#         'category',
#     ]
#     list_filter = ['title', 'category']
#     search_fields = ['title', 'category']
#     prepopulated_fields = {"slug": ("title",)}
#     actions = [copy_items]

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = [
#         'title',
#         'is_active'
#     ]
#     list_filter = ['title', 'is_active']
#     search_fields = ['title', 'is_active']
#     prepopulated_fields = {"slug": ("title",)}
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'slug', 'is_active']
    list_filter = ['is_active', 'parent']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    fields = ['title', 'slug', 'description', 'image', 'is_active', 'parent']
    autocomplete_fields = ['parent']  # Optional: for better UX when selecting parent

    # Optional: Enable autocomplete for parent field
    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        queryset |= self.model.objects.filter(title__icontains=search_term)
        return queryset, use_distinct

admin.site.register(Item)
admin.site.register(Slide)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(BillingAddress)
