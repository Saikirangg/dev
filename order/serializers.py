from order.models import order
from rest_framework import serializers
from order.models import store, orderTicket, settingsPincode


# class StoreSerializer(serializers.Serializer):
#     store_id = serializers.CharField(read_only=True)
#     store_name = serializers.CharField(read_only=True)
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#     status = serializers.CharField(read_only=True)

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return order.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.store_id = validated_data.get('store_id', instance.store_id)
#         instance.store_name = validated_data.get('store_name', instance.store_name)
#         instance.created_at = validated_data.get('created_at', instance.created_at)
#         instance.updated_at = validated_data.get('updated_at', instance.updated_at)
#         instance.status = validated_data.get('status', instance.status)
#         instance.save()
#         return instance


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = store
        fields = ['store_id', 'store_name', 'created_at', 'updated_at', 'status']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderTicket
        fields = ['ticket_id', 'order_id', 'product_id', 'issue', 'issue_type', 'sub_type', 'comment', 'image', 'issue',
                  'customer_id']


class SettingsPincodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = settingsPincode
        fields = ['id', 'pincode', 'status', 'created_on', 'updated_on', 'monday', 'tuesday', 'wednesday', 'thursday',
                  'friday', 'saturday', 'sunday']
