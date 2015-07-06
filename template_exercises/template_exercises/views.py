from django.shortcuts import render

# Yes, putting views in the main site seems pretty unorthodox, but I
# wanted to provide a simple view with some real HTML.
def welcome(request):
    return render(request, "template_exercises/welcome.html")
