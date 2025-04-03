from django.shortcuts import render
from django.http import JsonResponse
from .models import Asset
from sitee.models import Sitee
from customer.models import Customer
from client.models import Client

def asset_list(request):
    print("GET")
    print(request.GET)
    search_query = request.GET.get('search', '')
    page = int(request.GET.get('page', 1))
    per_page = 3
    start = (page - 1)*per_page
    end = start + per_page


    #Filter perameters
    client_id = request.GET.get('client')
    customer_id = request.GET.get('customer')
    sitee_id = request.GET.get('sitee')

    assets = Asset.objects.select_related('sitee__customer__client').all()
    if client_id:
        assets = assets.filter(sitee__customer__client__id = client_id)
    if customer_id:
        assets = assets.filter(sitee__customer__id=customer_id)
    if sitee_id:
        assets = assets.filter(sitee__id= sitee_id)
    if search_query:
        assets = assets.filter(name__icontains = search_query)
    
    total_assets = assets.count()
    total_pages = (total_assets + per_page - 1) // per_page

    filtered_assets = assets[start:end]

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        assets_data = list(filtered_assets.values(
            'id', 'name', 'phone_num', 'address',
            'sitee__name', 'sitee__customer__name', 'sitee__customer__client__name'
        ))
        return JsonResponse({'assets': assets_data, 'total_pages': total_pages, 'current_page': page })

    sitees = Sitee.objects.all()
    customers = Customer.objects.all()
    clients = Client.objects.all()
    
    return render(request, 'asset/asset_list.html', {
        'assets': filtered_assets,
        'current_page': page,
        'total_pages':  total_pages,
        'clients' : clients,
        'sitees':sitees,
        'customers':customers,
        })

def asset_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        address = request.POST.get('address')
        sitee_id = request.POST.get('sitee')

        sitee = Sitee.objects.get(id = sitee_id)

        Asset.objects.create(
            name= name,
            phone_num=phone_num,
            address=address,
            sitee=sitee
        )
        return JsonResponse({'message': 'Successfully added new asset'})
    return JsonResponse({'message': 'Invalid request'})


