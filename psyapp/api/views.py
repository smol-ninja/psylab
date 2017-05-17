from django.shortcuts import render

from engine.drivers.feedapi import fetch_price_list
# Create your views here.


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def test_view(request):
    if request.method == 'GET' and request.query_params=='hexagon':
        secId=request.data['sid']
        datefrom=request.data['from']
        dateto=request.data['to']
        frequency=request.data['frequency']
        fetched_data = fetch_price_list(secId, datefrom, dateto, frequency)
        ts = TickerSerializer(ticker_lists, many=True)
        return Response(status=200, data=fetched_data)
    else:
        return Response(status=404, data='Not available')
