from django.shortcuts import render

# Create your views here.
def layers_list(request):
    return render(request, 'layers/layers.html')