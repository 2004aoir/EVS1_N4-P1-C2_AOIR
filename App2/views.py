from django.shortcuts import render
from django.http import HttpResponse

def display1App2(request):
    return HttpResponse("<h1 style=\"color:green;\">ESTO ES LA APP2 (Pagina_1)</h1><h2 style=\"color:green;\">ESTO ES LA APP2</h2><h3 style=\"color:green;\">ESTO ES LA APP2</h3><h4 style=\"color:green;\">ESTO ES LA APP2</h4>")
def display2App2(request):
    return HttpResponse("<h1 style=\"color:orange;\">ESTO ES LA APP2 (Pagina_2)</h1><h2 style=\"color:orange;\">ESTO ES LA APP2</h2><h3 style=\"color:orange;\">ESTO ES LA APP2</h3><h4 style=\"color:orange;\">ESTO ES LA APP2</h4>")