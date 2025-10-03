from django.shortcuts import render
from django.http import JsonResponse
import requests
def home(request):
    return render(request, 'home.html')

# core/views.py



def user_panel(request):
    if request.method == "POST":
        message = request.POST.get("message")

        # Aquí llamamos a la API de n8n para enviar el mensaje
        api_url = "https://n8n.agenciabuffalo.es/webhook/recibir-ia-mensaje"
        payload = {
            "message": message,
            # Puedes agregar más campos si tu API los requiere
        }
        try:
            response = requests.post(api_url, json=payload)
            response_data = response.json()
            return JsonResponse({"status": "success", "data": response_data})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return render(request, "user_panel.html")

