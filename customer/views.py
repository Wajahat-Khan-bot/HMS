from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer
from client.models import Client

def customer_list (request):

    print("GET: ", request.GET)
    
    page = int(request.GET.get('page', 1))
    per_page = 3
    start = (page-1)*per_page
    end = start + per_page

    customers = Customer.objects.select_related('client').order_by('id')
    clients = Client.objects.all()
    total_customers = customers.count()
    total_pages = (total_customers + per_page - 1) // per_page
    customers =customers[start:end]

    # print(customers)
    if request.headers.get('X-Requested-With') =='XMLHttpRequest':
        print('ajax')
        customers_data = [
            {
                'id': customer.id,
                'name': customer.name,
                'email': customer.email,
                'address': customer.address,
                'client': customer.client.name
            }
            for customer in customers
        ]
        print(total_pages)
        return JsonResponse({'total_pages': total_pages, 'customers_data':customers_data, 'current_page': page})
    
    return render(request, "customer_app/customer_list.html", {"customers": customers, "clients": clients})

def customer_create(request): 
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        client_id = request.POST.get('client')

        client = Client.objects.get(id=int(client_id))
    
        customer= Customer.objects.create(
            name=name,
            email=email,
            address=address,
            client=client
        )
        return JsonResponse({"message":" Customer successfully created"})
    return JsonResponse({"message": "Invalid request"})
