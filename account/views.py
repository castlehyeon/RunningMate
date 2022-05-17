from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from .models import Account
from .serializers import AccountSerializer
from rest_framework.views import APIView


class AccountView(APIView):
    @csrf_exempt
    def get(self, request, pk):
        account = Account.objects.get(pk=pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)


class AccountListView(APIView):
    @csrf_exempt
    def get(self, request):
        queryset = Account.objects.all()
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)
