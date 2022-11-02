from order.models import store
from order.models import ProductsImage, Product, store, order, StoreShopify, orderTicket, settingsPincode
from django.contrib import admin

admin.site.register(Product)
admin.site.register(ProductsImage)
admin.site.register(store)
admin.site.register(order)
admin.site.register(orderTicket)
admin.site.register(StoreShopify)
admin.site.register(settingsPincode)
