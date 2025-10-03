from django.shortcuts import render
from django.http import JsonResponse
import requests
def home(request):
    return render(request, 'home.html')

# core/views.py



def user_panel(request):
    if request.method == "POST":
        message = request.POST.get("message")

        api_url = "https://n8n.agenciabuffalo.es/webhook/recibir-ia-mensaje"
        payload = {"message": message}
        try:
            response = requests.post(api_url, json=payload)
            response_data = response.json()
            return JsonResponse({"status": "success", "data": response_data})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    # 👇 en GET muestra el HTML, en POST inválido devuelve error
    if request.method == "GET":
        return render(request, "user_panel.html")
    return JsonResponse({"status": "error", "message": "Método no permitido"}, status=405)
