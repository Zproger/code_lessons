from django.shortcuts import render
from .handlers.info import get_info_by_ip


# TODO: Выводим index.html и результат POST запроса
def index(request):
    if request.method == 'POST':
        ip_address = request.POST.get('ipAddress')
        ip_info = get_info_by_ip(ip_address)
        return render(request, 'ip_app/index.html', {'ip_address': ip_info})
    else:
        return render(request, 'ip_app/index.html')

