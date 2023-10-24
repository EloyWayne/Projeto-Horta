from django.shortcuts import render

def register_view(request):
    render(request, 'LoginUser/pages/register_view.html')

