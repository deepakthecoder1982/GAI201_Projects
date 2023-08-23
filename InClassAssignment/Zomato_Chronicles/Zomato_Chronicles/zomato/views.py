from django.shortcuts import render,redirect
from django.http import JsonResponse 
from .menu import get_menu
import json
# Create your views here.

    # return render(request,'zomato/menu.html',{'menu':menu})
def add_dish(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data);
            dish_name = data.get("dish_name")
            dish_price = data.get("dish_price")
            dish_available = data.get("dish_available") == "on"

            menu = get_menu()
            dish_id = 1
            if menu:
                dish_id = max(menu.keys()) + 1 
            new_dish = {
                'name': dish_name,
                'price': dish_price,
                'available': dish_available
            }
            menu[dish_id] = new_dish
            return JsonResponse({"menu": menu})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
    menu = get_menu()
    return render(request, 'menu.html', {'menu': menu})
def display_menu(request):
    menu = get_menu()
    return JsonResponse({"menu":menu})
def update_dish(request, dish_id):
    if request.method == 'POST':
        dish_name = request.POST.get("edit_dish_name")
        dish_price = request.POST.get("edit_dish_price")
        dish_available = request.POST.get("edit_dish_available") == 'on'

        menu = get_menu()
        if dish_id in menu:
            menu[dish_id]['name'] = dish_name
            menu[dish_id]['price'] = dish_price
            menu[dish_id]['available'] = dish_available
            return JsonResponse({"menu": menu})
    
    return JsonResponse({"error": "Invalid dish ID or data"}, status=400)

def display_page(request):
    menu = get_menu()
    return render(request,'menu.html',{'menu':menu})
