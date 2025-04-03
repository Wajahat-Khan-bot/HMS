from django.shortcuts import render 
from django.http import JsonResponse
from .models import Sitee
from customer.models import Customer


def sitee_list(request):
    sitees = Sitee.objects.select_related("customer__client").all()
    customers = Customer.objects.all()
    print(sitees)
    return render(request , "sitee/sitee_list.html", {'sitees': sitees, "customers": customers})

def sitee_create(request):
    print("hello world")
    print(request.POST.get('customer'))
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        address = request.POST.get('address')
        customer_id = request.POST.get('customer')
        print(customer_id)

        customer = Customer.objects.get(id = customer_id)

        # if not name and phone_num and customer:
        #     return JsonResponse({ 'message': "Invalid Data" })
        
        new_site= Sitee.objects.create(
            name = name,
            phone_num=phone_num,
            address=address,
            customer = customer
        )
        return JsonResponse({'message': 'Added new sitee Successfully'})
    return JsonResponse({'message': 'Invalid request'})
