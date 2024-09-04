from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306275052',
        'name': 'Daniel Ferdiansyah',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
