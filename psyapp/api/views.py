from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

from .models import Subscriber

from engine.drivers.feedapi import fetch_price_list

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def subscriber_view(request):
    if request.method == 'POST':
        try:
            s = Subscriber.objects.get(subscriber=request.data['email'])
            return Response(status=302)
        except:
            s = Subscriber.objects.create(subscriber=request.data['email'])
            return Response(status=200)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def fetch_view(request):
    """
    It will return an array of price.
    Url: /api/fetch/?key=hexagon
    Input:
        {
    	"sid": "INE069A01017",
    	"from": "2014-09-25",
    	"to": "2017-01-10",
    	"frequency": "daily"
        }
    return: [
          "1661.55",
          "1754.25",
          "1784.55",
          "1709.8"
        ]
    """
    # import pdb; pdb.set_trace()
    if request.method == 'POST' and request.query_params['key']=='hexagon':
        secId=request.data['sid']
        datefrom=request.data['from']
        dateto=request.data['to']
        frequency=request.data['frequency']
        try:
            fetched_data = fetch_price_list(secId, datefrom, dateto, frequency)
            return Response(status=200, data=fetched_data)
        except Exception as e:
            return Response(status=404)
    else:
        return Response(status=404, data='Not available')
