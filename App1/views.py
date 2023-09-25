from django.shortcuts import render
from django.http import HttpResponse

def display1App1(request):
    return HttpResponse("<h1 style=\"color:red;\">ESTO ES LA APP1 (Pagina_1)</h1><h2 style=\"color:red;\">ESTO ES LA APP1</h2><h3 style=\"color:red;\">ESTO ES LA APP1</h3><h4 style=\"color:red;\">ESTO ES LA APP1</h4>")
def display2App1(request):
    return HttpResponse("<h1 style=\"color:blue;\">ESTO ES LA APP1 (Pagina_2)</h1><h2 style=\"color:blue;\">ESTO ES LA APP1</h2><h3 style=\"color:blue;\">ESTO ES LA APP1</h3><h4 style=\"color:blue;\">ESTO ES LA APP1</h4>")