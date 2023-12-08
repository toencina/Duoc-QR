from django.shortcuts import render
from django.views import View
from device_detector import DeviceDetector

class UserView(View):
    def get(self, request):
        user_agent = request.META.get('HTTP_USER_AGENT', 'Desconocido')
        device_detector = DeviceDetector(user_agent)
        device = device_detector.parse()

        # Verificar si es un dispositivo móvil
        is_mobile = device.is_mobile()

        if is_mobile:
            device_type = 'Móvil'
        else:
            device_type = 'Escritorio/Notebook'

        return device_type

def index(request):
    user_agent = UserView.as_view()(request)
    print("Device Type:", user_agent)
    return render(request, 'index.html', {'user_agent': user_agent})
