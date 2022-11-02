# from .models import order
from rest_framework import serializers
from .models import callStatus, calls


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


class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = calls
        fields = ['call_id', 'call_tag', 'created_at', 'updated_at', 'is_active']


class CallStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = callStatus
        fields = ['call_status_id', 'type', 'title', 'created_at', 'updated_at','is_active','additional_tag_required']