from django.shortcuts import render
import json

# Create your views here.
from django.http import JsonResponse
from django.views import View
from products.models import Owner, Dog 

class ProductsView(View):
    def post(self, request):
        data = json.loads(request.body)
        owner = Owner.objects.create(
            name=data['owner'], 
            email=data['owner'], 
            age=data['owner']
        )
        dog = Dog.objects.create(
            name = data['dog'],
            owner = owner,
            age = data['dog']
        )
              

        return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)