from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Client
from django.contrib import messages


def client_create(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        address = request.POST.get('address')

        if not name or not phone_num:
            messages.error(request, 'Name and phone number is required!')
            return redirect(client_create)
        
        Client.objects.create(
            name=name,
            phone_num=phone_num,
            address=address
        )
        messages.success(request,'Created Successfuly!')
        return JsonResponse({"message": "Client updated successfully!"})
    return JsonResponse({"error": "Invalid request"}, status=400)


def client_list(request):

    page = int(request.GET.get('page', 1))
    per_page = 5
    start = (page - 1)*per_page
    end = start + per_page

    clients = Client.objects.all()
    total_clients = clients.count()
    total_pages = (total_clients + per_page - 1) // per_page
    clients = clients[start:end]
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        clients = (list(clients.values()))
        return JsonResponse({'clients': clients, 'total_pages':total_pages, 'current_page': page})
    
    return render(request, 'client_app/client_list.html')

def client_list_in_json(request):
    clients = Client.objects.all().values("id", "name", "phone_num", "address")
    print(f"clients = {clients}")
    data = {
      "clients": list(clients)
    }
    return JsonResponse(data, safe=False)

def client_update(request):
    print(request.POST)
    if request.method == 'POST':

        client_id =int(request.POST.get("client_id"))
        name = request.POST.get("name")
        phone_num = request.POST.get("phone_num")
        address = request.POST.get("address")

        client = Client.objects.get(id=client_id)

        client.name = request.POST.get('name')
        client.phone_num = request.POST.get('phone_num')
        client.address = request.POST.get('address')
        client.save()
        return JsonResponse({"message": "Client updated successfully!"})
    return JsonResponse({"error": "Invalid request"}, status=400)

def client_delete(request):

    if request.method =="POST":
        client_id = int(request.POST.get("client_id"))

        client= Client.objects.get(id=client_id)
        client.delete()
        return JsonResponse({"message": "Client deleted successfully!"})
    return JsonResponse({"error": "Invalid request"}, status=400)

def client_copy(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        address = request.POST.get('address')
        
        new_client = Client.objects.create(
            name=name,
            phone_num=phone_num ,
            address=address
        )
        return JsonResponse({"message": "Client updated successfully!"})
    return JsonResponse({"error": "Invalid request"}, status=400)

