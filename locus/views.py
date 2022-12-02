import io
import datetime
from click import File
import requests
from .models import Patient
from datetime import datetime as dtt
from datetime import date as dat
from .serializers import (
    PatientSerializer,
    FileSerializer
)
from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)
import pandas as pd
import json
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class FileUploadView(APIView):
    """Represents file upload view class.
    API endpoint that allows users to be upload a csv file.
    POST: upload file
    """

    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        uploaded = []
        failed = []
        """Upload the CSV file.
        Then reads it and saves csv data to database.
        Endpoint: /api/patients/file_upload/
        """
        request.data['owner'] = request.user.id
        file_serializer = FileSerializer(data=request.data)
        # Commented code is for debugging only
        # import pdb; pdb.set_trace()
        # print(to_dict['_name'])
        _dict_file_obj = request.data['file'].__dict__
        kkd = request.data['file']

        _csv = _dict_file_obj['_name'].endswith('.csv')

        _excel = _dict_file_obj['_name'].endswith('.xlsx')

        if request.data['file'] is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_400_BAD_REQUEST)

        if file_serializer.is_valid():
            data = self.request.data.get('file')

            if _csv is True:
                data_set = data.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                io_string = io.StringIO(data_set)

                csv_file = pd.read_csv(io_string, low_memory=False)
                for i in range(len(csv_file)):
                    order_id = str(csv_file['Order ID'][i])
                    types = (str(csv_file['Type'][i])).upper()
                    team_id = str(csv_file['Team ID'][i])
                    homebase_id = str(csv_file['Homebase ID'][i])
                    category = str(csv_file['Category'][i])
                    customer_address = str(csv_file['Customer Address'][i])
                    customer_zipcode = str(csv_file['Customer Zipcode'][i])
                    customer_city = str(csv_file['Customer City'][i])
                    customer_state = str(csv_file['Customer State'][i])
                    customer_country = str(csv_file['Customer Country'][i])
                    contact_name = str(csv_file['Contact Name'][i])
                    contact_number = str(csv_file['Contact Number'][i])

                    transaction_duration = int(csv_file['Customer Transaction Duration (minutes)'][i])
                    volume = str(csv_file['Volume'][i])
                    volume_unit = str(csv_file['Volume Unit'][i])
                    quantity = str(csv_file['Quantity'][i])
                    quantity_unit = str(csv_file['Quantity Unit'][i])
                    # customer_notes = csv_file['customer_notes'][i]
                    payment_type = (str(csv_file['Payment Type'][i])).upper()
                    amount = float(csv_file['Amount'][i])
                    currency = str(csv_file['Currency'][i])
                    what3words = str(csv_file['what3words'][i])
                    date = str(datetime.datetime.strptime(str(csv_file['Customer Execution Date'][i]), "%d-%m-%Y").strftime("%Y-%m-%d"))
                    order_date = str(datetime.datetime.strptime(str(csv_file['Order Date'][i]), "%d-%m-%Y").strftime("%Y-%m-%d"))
                    # customer_slot_start = order_date+'T'+str(dtt.strptime(str(csv_file['Customer Slot Start'][i]), '%I:%M %p').strftime('%H:%M:%S'))+'.000+0000'
                    # customer_slot_end = order_date+'T'+str(dtt.strptime(str(csv_file['Customer Slot End'][i]), '%I:%M %p').strftime('%H:%M:%S'))+'.000+0000'
                    customer_slot_start = str(dat.today())+'T'+str(dtt.strptime(str(csv_file['Customer Slot Start'][i]), '%I:%M %p').strftime('%H:%M:%S'))+'.000+0000'
                    customer_slot_end = str(dat.today())+'T'+str(dtt.strptime(str(csv_file['Customer Slot End'][i]), '%I:%M %p').strftime('%H:%M:%S'))+'.000+0000'
                    
                    print(customer_slot_start)
                    print(customer_slot_end)
                    print(team_id)




                    # url = "https://api.locus.sh/v1/orders"
                    url = "https://oms.locus-api.com/v1/client/gourmetgarden-oiq/order/"+str(order_id)
                    payload = json.dumps({
                        "clientId": "gourmetgarden-oiq",
                        "id": order_id,
                        "type": types,
                        "teamId": team_id,
                        "homebaseId": homebase_id,
                        "category": category,
                                "lineItems": [
                            {
                            "id": "Product",
                            "name": "Product",
                            "quantity": quantity,
                            "quantityUnit": quantity_unit
                            }
                        ],
                        "locationAddress": {
                            "placeName": "Locus Office",
                            "formattedAddress": customer_address,
                            "pincode": customer_zipcode,
                            "city": customer_city,
                            "state": customer_state,
                            "countryCode": customer_country
                        },
                        "contactPoint": {
                            "name": contact_name,
                            "number": contact_number
                        },
                        "slot": {
                            "start": customer_slot_start,
                            "end": customer_slot_end
                        },
                        "amountTransaction": {
                        "amount": {
                        "amount": amount,
                        "currency": currency
                        },
                        "exchangeType": payment_type
                        },
                        "transactionDuration": transaction_duration,
                        "volume": {
                            "value": volume,
                            "unit": volume_unit
                        },
                        "quantity": {
                            "value": quantity,
                            "unit": quantity_unit
                        },
                            "date": date,
                            "orderDate": order_date,
                            "what3words": what3words
                    })
                
                    headers = {
                    'Authorization': 'Basic Z291cm1ldGdhcmRlbi1vaXE6Nzk4YmU5NDEtMzYzMS00ZjI1LTg2MjEtOTVkMmIyZjExOTEx',
                    'Content-Type': 'application/json'
                    }


                    
                    response = requests.request("PUT", url, headers=headers, data=payload)
                    if response.status_code == 200:
                        uploaded.append(order_id)
                    else:
                        failed.append(order_id)

                    print(response.text)
                columns = list(csv_file.columns.values)
                # print(columns)

                first_name, last_name, email = columns[0], columns[1],\
                    columns[2]

                instances = [
                    Patient(
                        firstname=row[first_name],
                        lastname=row[last_name],
                        email=row[email]
                    )

                    for index, row in csv_file.iterrows()
                ]

                Patient.objects.bulk_create(instances)

            elif _excel is True:
                xl = pd.read_excel(data)
                columns = list(xl.columns.values)
                first_name, last_name, email = columns[0], columns[1],\
                    columns[2]

                instances = [
                    Patient(
                        firstname=row[first_name],
                        lastname=row[last_name],
                        email=row[email]
                    )

                    for index, row in xl.iterrows()
                ]

                Patient.objects.bulk_create(instances)

            else:
                return Response(data={"err": "Must be *.xlsx or *.csv File."},
                                status=status.HTTP_400_BAD_REQUEST
                                )

            file_serializer.save()
            return Response(
                {"message": "Upload Successfull",
                    "uploaded": uploaded,
                    "failed": failed,
                 "data": file_serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(file_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

        

class PatientListAPIView(generics.ListAPIView):
    """Class represents Patient API View.
    endpoint: /api/patients/list/
    GET: show list of patients.
    POST: create a patient.
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer