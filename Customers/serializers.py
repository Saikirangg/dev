from order.models import order
from rest_framework import serializers
from Customers.models import Customers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = ['id',
                  'customer_id',
                  'store_id',
                  'first_name',
                  'last_name',
                  'name',
                  'phone',
                  'email',
                  'phone_verify',
                  'email_verify',
                  'accepts_marketing',
                  'last_login',
                  'group_id',
                  'created_at',
                  'updated_at',
                  'password',
                  'password_hash',
                  'tags',
                  'login_ip',
                  'shopify_id',
                  'order_count',
                  'total_spent',
                  'first_order_date',
                  'last_order',
                  'note',
                  'fromapi',
                  'onclevertap',
                  'city',
                  'state',
                  'pincode',
                  'caller',
                  'dnd',
                  'conversation_status',
                  'conversation_note',
                  'conversation_dt',
                  'experience_caller',
                  'welcome_conid',
                  'winback_conid',
                  'experience_conid']
