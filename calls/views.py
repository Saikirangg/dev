import imp
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from .models import calls
from .models import callStatus

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from calls.serializers import CallSerializer
from calls.serializers import CallStatusSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = calls.objects.all()
        serializer = CallSerializer(snippets, many=True)
        return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data,"message":"success"}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CallSerializer(data=data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data,"message":"success"}, status=status.HTTP_200_OK)
        # return JsonResponse(serializer.errors, status=400)
        return JsonResponse({"status code": status.HTTP_400_BAD_REQUEST, "data": serializer.errors,"message":"error"}, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = calls.objects.get(pk=pk)
    except calls.DoesNotExist:
        return JsonResponse({"status code": status.HTTP_404_NOT_FOUND, "data": "no data found","message":"Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CallSerializer(snippet)
        return JsonResponse(serializer.data)
        # return JsonResponse({"status code": status.HTTP_404_NOT_FOUND, "data": serializer.errors,"message":"Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CallSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data,"message":"Data updated successfully"}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return JsonResponse({"status code": "200","message":"success", "data": "Item Deleted"})


#Call Status Serializer

@csrf_exempt
def call_status_snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = callStatus.objects.all()
        serializer = CallStatusSerializer(snippets, many=True)
        return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data,"message":"success"}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CallStatusSerializer(data=data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data,"message":"success"}, status=status.HTTP_200_OK)
        # return JsonResponse(serializer.errors, status=400)
        return JsonResponse({"status code": status.HTTP_400_BAD_REQUEST, "data": serializer.errors,"message":"error"}, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
def call_status_snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = callStatus.objects.get(pk=pk)
    except callStatus.DoesNotExist:
        return JsonResponse({"status code": status.HTTP_404_NOT_FOUND, "data": "no data found","message":"Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = CallStatusSerializer(snippet)
        return JsonResponse(serializer.data)
        # return JsonResponse({"status code": status.HTTP_404_NOT_FOUND, "data": serializer.errors,"message":"Not Found"}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CallStatusSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data,"message":"Data updated successfully"}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return JsonResponse({"status code": "200","message":"success", "data": "Item Deleted"})

