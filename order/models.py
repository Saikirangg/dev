from django.db import models
from django.utils import timezone
from Customers.models import Customers


class store(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.store_name


class StoreShopify(models.Model):
    store_id = models.ForeignKey(store, on_delete=models.CASCADE)
    Key = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Secret = models.CharField(max_length=100)

    def __str__(self):
        return self.store_id


class ShopifyApi(models.Model):
    AccountId = models.ForeignKey(store, on_delete=models.CASCADE)
    Api = models.TextField()
    Accesstoken = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.AccountId


class ShopifyApiPrivate(models.Model):
    store_id = models.ForeignKey(store, on_delete=models.CASCADE)
    Key = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    Secret = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.store_id


class ShopifyEvent(models.Model):
    id = models.AutoField(primary_key=True)
    eventId = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    eventurl = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    accountId = models.CharField(max_length=100)

    def __str__(self):
        return self.store_id


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    store_id = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    body_html = models.TextField()
    vendor = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    handle = models.DateTimeField(default=timezone.now)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    published_at = models.DateField(auto_now_add=True)
    template_sufix = models.TextField()
    published_score = models.TextField()
    tags = models.TextField()
    admin_graphql_api_id = models.TextField()
    sync_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class ProductsImage(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    position = models.DecimalField(max_digits=9, decimal_places=2)
    alt = models.TextField()
    width = models.DecimalField(max_digits=9, decimal_places=2)
    height = models.DecimalField(max_digits=9, decimal_places=2)
    src = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    variant_ids = models.TextField()
    admin_graphql_api_id = models.TextField()
    main = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.title


class ProductOption(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    position = models.DecimalField(max_digits=9, decimal_places=2)
    value = models.TextField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    sku = models.TextField()
    inventory_policy = models.TextField()
    compare_at_price = models.TextField()
    fulfillment_service = models.TextField()
    inventory_management = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    taxable = models.DecimalField(max_digits=9, decimal_places=2)
    barcode = models.TextField()
    grams = models.DecimalField(max_digits=9, decimal_places=2)
    image_id = models.TextField()
    weight = models.DecimalField(max_digits=9, decimal_places=2)
    weight_unit = models.TextField()
    inventory_item_id = models.TextField()
    inventory_quantity = models.DecimalField(max_digits=9, decimal_places=2)
    old_inventory_quantity = models.DecimalField(max_digits=9, decimal_places=2)
    requires_shipping = models.TextField()
    admin_graphql_api_id = models.TextField()
    currency_code = models.TextField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)
    position = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.title


class order(models.Model):
    order_id = models.CharField(max_length=100)
    parent_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=100)
    customer_id = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    closed_on = models.DateField(auto_now_add=True)
    rationing_status = models.CharField(max_length=100)
    crating_status = models.CharField(max_length=100)
    packing_status = models.CharField(max_length=100)
    financial_status = models.CharField(max_length=100)
    fullfilment_status = models.CharField(max_length=100)
    delivery_status = models.CharField(max_length=100)
    order_type = models.CharField(max_length=100)
    delivery_date = models.DateField(auto_now_add=True)
    delivery_slot = models.CharField(max_length=100)
    shopify_delivery_dt = models.CharField(max_length=100)
    order_number = models.CharField(max_length=100)
    order_name = models.CharField(max_length=100)
    updated_on = models.DateField(auto_now_add=True)
    shopify_status = models.CharField(max_length=100)
    order_status = models.CharField(max_length=100)
    shopify_id = models.CharField(max_length=100)
    location_id = models.CharField(max_length=100)
    caller = models.CharField(max_length=100)
    express = models.CharField(max_length=100)
    confirm = models.CharField(max_length=100)
    expressready = models.CharField(max_length=100)
    conversation_status = models.CharField(max_length=100)
    conversation_note = models.CharField(max_length=100)
    conversation_dt = models.CharField(max_length=100)
    explocation = models.CharField(max_length=100)

    def __str__(self):
        return self.order_id


class OrderAddress(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    billing_first_name = models.CharField(max_length=100)
    billing_last_name = models.CharField(max_length=100)
    billing_phone = models.CharField(max_length=100)
    billing_email = models.CharField(max_length=100)
    billing_address1 = models.TextField()
    billing_address2 = models.TextField()
    billing_landmark = models.CharField(max_length=100)
    billing_city = models.CharField(max_length=100)
    billing_state = models.CharField(max_length=100)
    billing_country = models.CharField(max_length=100)
    billing_postcode = models.CharField(max_length=100)
    billing_latitude = models.CharField(max_length=100)
    billing_longitude = models.CharField(max_length=100)
    billing_province = models.CharField(max_length=100)
    shipping_first_name = models.CharField(max_length=100)
    shipping_last_name = models.CharField(max_length=100)
    shipping_phone = models.CharField(max_length=100)
    shipping_address1 = models.TextField()
    shipping_address2 = models.TextField()
    shipping_landmark = models.CharField(max_length=100)
    shipping_city = models.CharField(max_length=100)
    shipping_state = models.CharField(max_length=100)
    shipping_country = models.CharField(max_length=100)
    shipping_postcode = models.CharField(max_length=100)
    shipping_latitude = models.CharField(max_length=100)
    shipping_longitude = models.CharField(max_length=100)
    shipping_province = models.TextField()
    customer_note = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    location_id = models.CharField(max_length=100)

    def __str__(self):
        return self.order_id


class OrderAmount(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    currency = models.CharField(max_length=100)
    total_items = models.CharField(max_length=100)
    total_items_price = models.CharField(max_length=100)
    total_discount = models.CharField(max_length=100)
    total_subtotal_price = models.CharField(max_length=100)
    total_tax = models.CharField(max_length=100)
    total_price = models.CharField(max_length=100)
    total_tip_received = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.total_items


class OrderClientDetail(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    accept_language = models.CharField(max_length=100)
    browser_height = models.CharField(max_length=100)
    browser_ip = models.CharField(max_length=100)
    browser_width = models.CharField(max_length=100)
    session_hash = models.CharField(max_length=100)
    user_agent = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.order_id


class OrderConversation(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    calltype = models.CharField(max_length=100)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    by = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)
    note = models.TextField()
    customer_id = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.tags


class OrderDelivery(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    rider_name = models.CharField(max_length=100)
    rider_number = models.CharField(max_length=100)
    vehicleId = models.CharField(max_length=100)
    tracklink = models.CharField(max_length=100)
    delivery_status = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    carrierTeams = models.CharField(max_length=100)
    log = models.CharField(max_length=100)
    eta = models.CharField(max_length=100)

    def __str__(self):
        return self.total_price


class OrderDiscount(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    target_type = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    value_type = models.CharField(max_length=100)
    allocation_method = models.CharField(max_length=100)
    target_selection = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.total_price


class OrderEcovia(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    pickup_schedule_at = models.DateField(auto_now_add=True)
    picked_done_at = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.total_price


class OrderItem(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    sku = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    variant_title = models.CharField(max_length=100)
    total_discount = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    variant_id = models.CharField(max_length=100)
    line_items_id = models.CharField(max_length=100)
    deliveryMethod = models.CharField(max_length=100)
    deliveryTime = models.TimeField(auto_now_add=True)
    deliveryCharge = models.CharField(max_length=100)
    locationId = models.CharField(max_length=100)
    fullfilled = models.CharField(max_length=100)

    def __str__(self):
        return self.total_price


class OrderLog(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    event = models.CharField(max_length=100)
    log = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    orderId = models.ForeignKey(order, on_delete=models.CASCADE)

    def __str__(self):
        return self.total_price


class OrderSource(models.Model):
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    source = models.CharField(max_length=100)
    landing_site = models.CharField(max_length=100)
    utm_campaign = models.CharField(max_length=100)
    utm_source = models.CharField(max_length=100)

    def __str__(self):
        return self.total_price


class orderTicket(models.Model):
    id =  models.AutoField(primary_key=True)
    ticket_id = models.CharField(max_length=100)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    issue = models.TextField()
    issue_type = models.TextField()
    sub_type = models.CharField(max_length=100)
    comment = models.TextField()
    image = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)

    def __str__(self):
        return self.order_id


class settingsPincode(models.Model):
    id = models.AutoField(primary_key=True)
    pincode = models.CharField(max_length=100)
    status = models.IntegerField()
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    monday = models.IntegerField()
    tuesday = models.IntegerField()
    wednesday = models.IntegerField()
    thursday = models.IntegerField()
    friday = models.IntegerField()
    saturday = models.IntegerField()
    sunday = models.IntegerField()

    def __str__(self):
        return self.pincode
