from django.shortcuts import render
from .models import AboutSection

# Create your views here.
def get_about(request):
    """
    Display the about page.

    **Template:**

    :template:`about/about.html`
    """
    about = AboutSection.objects.first()

    return render(
        request,
        "about/about.html",
        {"about": about}
    )