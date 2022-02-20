from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class OrderView(generics.RetrieveAPIView):
    queryset = Order.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
