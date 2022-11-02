from ast import Delete
from django.shortcuts import render
from order.models import store, orderTicket, settingsPincode

from order.serializers import StoreSerializer, TicketSerializer, SettingsPincodeSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# serializer = StoreSerializer(Store.objects.all(), many=True)
# serializer.data
import json

from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from CRM.helper.BaseResponse import BaseResponse


@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = store.objects.all()
        serializer = StoreSerializer(snippets, many=True)
        return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data, "message": "success"},
                            status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(data=data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data, "message": "success"},
                                status=status.HTTP_200_OK)
        # return JsonResponse(serializer.errors, status=400)
        return JsonResponse({"status code": status.HTTP_400_BAD_REQUEST, "data": serializer.errors, "message": "error"},
                            status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def tickets_list(request):
    if request.method == 'GET':
        snippets = orderTicket.objects.all()
        serializer = TicketSerializer(snippets, many=True)
        base = BaseResponse(data=serializer.data, exception=None, code=status.HTTP_200_OK)
        # return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data, "message": "success"},
        #                     status=status.HTTP_200_OK)
        return JsonResponse(base.to_dict(),status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TicketSerializer(data=data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data, "message": "success"},
                                status=status.HTTP_200_OK)
        return JsonResponse({"status code": status.HTTP_400_BAD_REQUEST, "data": serializer.errors, "message": "error"},
                            status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def ticket(request, id):
    try:
        snippet = store.objects.get(pk=id)
    except store.DoesNotExist:
        return JsonResponse({"status code": status.HTTP_404_NOT_FOUND, "data": "no data found", "message": "Not Found"},
                            status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = TicketSerializer(snippet, many=True)
        base = BaseResponse(data=serializer.data, exception=None, code=status.HTTP_200_OK)
        return JsonResponse(base.to_dict())

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TicketSerializer(snippet, data=data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            base = BaseResponse(data=serializer.data, exception=None, code=status.HTTP_200_OK)
            return JsonResponse(base.to_dict(),
                                status=status.HTTP_200_OK)
        return JsonResponse({"status code": status.HTTP_400_BAD_REQUEST, "data": serializer.errors, "message": "error"},
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return JsonResponse({"status code": "200", "message": "success", "data": "Item Deleted"})


@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = store.objects.get(pk=pk)
    except store.DoesNotExist:
        return JsonResponse({"status code": status.HTTP_404_NOT_FOUND, "data": "no data found", "message": "Not Found"},
                            status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = StoreSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"status code": status.HTTP_200_OK, "data": serializer.data, "message": "Data updated successfully"},
                status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return JsonResponse({"status code": "200", "message": "success", "data": "Item Deleted"})


@csrf_exempt
def delivery_pincode(request):
    if request.method == 'GET':
        snippets = settingsPincode.objects.all()
        serializer = SettingsPincodeSerializer(snippets, many=True)
        base = BaseResponse(data=serializer.data, exception=None, code=status.HTTP_200_OK)
        return JsonResponse(base.to_dict(), status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['status'] = 1
        serializer = SettingsPincodeSerializer(data=data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            base = BaseResponse(data=serializer.data, exception=None, code=status.HTTP_200_OK)
            return JsonResponse(base.to_dict(), status=status.HTTP_200_OK)
        # return JsonResponse(serializer.errors, status=400)
        return JsonResponse({"status code": status.HTTP_400_BAD_REQUEST, "data": serializer.errors, "message": "error"},
                            status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def pincode_delivery(request, pk):
    try:
        snippet = settingsPincode.objects.get(pk=pk)
    except store.DoesNotExist:
        base = BaseResponse(data="no data found", exception=None, code=status.HTTP_404_NOT_FOUND)
        return JsonResponse(base.to_dict(), status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = SettingsPincodeSerializer(snippet)
        base = BaseResponse(data=serializer.data, exception=None, code=status.HTTP_200_OK)
        return JsonResponse(base.to_dict(), status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SettingsPincodeSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"status code": status.HTTP_200_OK, "data": serializer.data, "message": "Data updated successfully"},
                status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return JsonResponse({"status code": "200", "message": "success", "data": "Item Deleted"})
