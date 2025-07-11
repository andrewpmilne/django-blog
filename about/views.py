from django.shortcuts import render
from .models import AboutSection
from .forms import CollaborateForm

# Create your views here.
def get_about(request):
    """
    Display the about page.

    **Template:**

    :template:`about/about.html`
    """
    about = AboutSection.objects.first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form},
    )