from django.shortcuts import render
from .models import AboutSection
from .forms import CollaborateForm
from django.contrib import messages

# Create your views here.
def get_about(request):
    """
    Display the about page.

    **Template:**

    :template:`about/about.html`
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)  
        if collaborate_form.is_valid():                   
            collaborate_form.save()
            messages.success(request, "Your collaboration request has been submitted!")

    about = AboutSection.objects.first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about,
         "collaborate_form": collaborate_form},
    )