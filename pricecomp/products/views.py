from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from products.models import *
from products.serializers import *
import json
from django.db import connection


class ProductModelView(viewsets.ModelViewSet):
    queryset = Productsndh.objects.all()
    serializer_class = ProductNDHSerializer


class ScrapeAPIView(APIView):
    def get(self, request):
        scrapes = Scrape.objects.all()
        serializer = ScrapePostSerializer(scrapes, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, id=None):
        data = request.data
        print(data)
        serializer = ScrapeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class ScrapeDetailAPIView(APIView):
    def get_object(self, id=None):
        try:
            return Productsndh.objects.get(id=id)
        except Productsndh.DoesNotExist:
            return Response({"Error": "Productdata does't exit"}, status=404)

    def get(self, request, id=None):
        scrape = self.get_object(id=id)
        serializer = ScrapeSerializer(scrape)
        return Response(serializer.data, status=200)

    def post(self, request, id=None):
        data = request.data
        scrapes = data.pop('scrapes')
        scrapes_data = []
        for scrape in scrapes:
            print(scrape, id)
            if not Productsndh.objects.get(id=id):
                return Response({"Error": "Product data does't exit"}, status=404)
        #     print('id',id)
            scrape["product"] = id
            print(scrape)
            serializer = ScrapePostSerializer(data=scrape)
            if serializer.is_valid():
                serializer.save()
                scrapes_data.append(serializer.data)
            else:
                return Response(serializer.errors, status=404)
        return Response(scrapes_data, status=201)
