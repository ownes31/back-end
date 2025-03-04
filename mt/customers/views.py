from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Customer
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def customer_list(request):
    if request.method == "GET":
        customers = list(Customer.objects.values())
        return JsonResponse(customers, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        customer = Customer.objects.create(name=data["name"], phone=data["phone"])
        return JsonResponse({"id": customer.id, "name": customer.name, "phone": customer.phone})

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return JsonResponse({"id": customer.id, "name": customer.name, "phone": customer.phone})
