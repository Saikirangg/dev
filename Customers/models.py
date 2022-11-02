from django.db import models
from django.utils import timezone


class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.CharField(max_length=100)
    store_id = models.CharField(max_length=100)
    first_name = models.TextField()
    last_name = models.TextField()
    name = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_verify = models.CharField(max_length=100)
    email_verify = models.CharField(max_length=100)
    accepts_marketing = models.CharField(max_length=100)
    last_login = models.CharField(max_length=100)
    group_id = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    password = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=100)
    tags = models.TextField()
    login_ip = models.CharField(max_length=100)
    shopify_id = models.CharField(max_length=100)
    order_count = models.CharField(max_length=100)
    total_spent = models.CharField(max_length=100)
    first_order_date = models.DateField(auto_now_add=True)
    last_order = models.DateField(auto_now_add=True)
    note = models.TextField()
    fromapi = models.CharField(max_length=100)
    onclevertap = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    caller = models.CharField(max_length=100)
    dnd = models.CharField(max_length=100)
    conversation_status = models.CharField(max_length=100)
    conversation_note = models.TextField()
    conversation_dt = models.CharField(max_length=100)
    experience_caller = models.CharField(max_length=100)
    welcome_conid = models.CharField(max_length=100)
    winback_conid = models.CharField(max_length=100)
    experience_conid = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CustomerAddress(models.Model):
    address_id = models.DateField(auto_now_add=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    address1 = models.TextField()
    address2 = models.TextField()
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    default = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    shopify_address_id = models.TextField()
    fromapi = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_id


class CustomerFcm(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    email_id = models.CharField(max_length=100)
    fcm_id = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    device_id = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_id


class CustomerLog(models.Model):
    log_id = models.CharField(max_length=100)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    log = models.TextField()
    log_type = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_id


class CustomerRewards(models.Model):
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    shopify_id = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    points_balance = models.CharField(max_length=100)
    referral = models.TextField()
    state = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now_add=True)
    smile_id = models.CharField(max_length=100)
    last_sync = models.CharField(max_length=100)
    syncstatus = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_id
