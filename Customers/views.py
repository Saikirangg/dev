from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

from rest_framework.parsers import JSONParser
from rest_framework import status
from Customers.serializers import CustomerSerializer
from Customers.models import Customers

# from CRM.helper.BaseResponse import BaseResponse
# from GG_Crm.CRM.helper import BaseResponse
from CRM.helper.BaseResponse import BaseResponse


@csrf_exempt
def customers(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Customers.objects.all()
        serializer = CustomerSerializer(snippets, many=True)
        return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data, "message": "success"},
                            status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return JsonResponse({"status code": status.HTTP_200_OK, "data": serializer.data, "message": "success"},
                                status=status.HTTP_200_OK)
        # return JsonResponse(serializer.errors, status=400)
        return JsonResponse({"status code": status.HTTP_400_BAD_REQUEST, "data": serializer.errors, "message": "error"},
                            status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def dnd_list(request):
    if request.method == 'GET':
        try:
            snippets = Customers.objects.filter(dnd=1)
            serializer = CustomerSerializer(snippets, many=True)
            base = BaseResponse(data=serializer.data, exception=None, code=status.HTTP_200_OK)
            return JsonResponse(base.to_dict(), status=status.HTTP_200_OK)
        except Customers.DoesNotExist:
            return JsonResponse(
                {"status code": status.HTTP_404_NOT_FOUND, "data": "No Dnd data found", "message": "Not Found"},
                status=status.HTTP_400_BAD_REQUEST)


def dnd(request, key):
    if request.method == 'GET':
        try:
            snippet = Customers.objects.get(email__exact=key)
            snippet.dnd = 1
            snippet.save()
            base = BaseResponse(data="Updated Successfully !!", exception=None, code=status.HTTP_200_OK)
            return JsonResponse(base.to_dict(),
                                status=status.HTTP_200_OK)

        except Customers.DoesNotExist:
            return JsonResponse(
                {"status code": status.HTTP_404_NOT_FOUND, "data": "no data found", "message": "Not Found"},
                status=status.HTTP_400_BAD_REQUEST)
