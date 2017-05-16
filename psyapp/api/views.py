from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

from .models import Subscriber

# Create your views here.
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
