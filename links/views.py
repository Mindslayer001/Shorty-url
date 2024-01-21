from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from .models import Link
from .forms import LinkForm
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from io import BytesIO
from django.http import HttpResponse
import base64
import qrcode


def index(request):
    links = Link.objects.all()
    context = {
        "links": links,
    }

    return render(request, "links/index.html", context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()  # increments click
    return redirect(link.url)


def add_link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            # save the data and return user to homepage
            form.save()
            return redirect(reverse("home"))

    else:
        form = LinkForm()

    context = {
        "form": form,
    }
    return render(request, "links/form.html", context)


def delete_link(request, link_slug):
    link_deleter = get_object_or_404(Link, slug=link_slug, isdeletable=1)
    link_deleter.delete()
    return redirect(reverse("home"))


class UpdateLink(UpdateView):
    model = Link
    template_name = "links/link_update.html"
    fields = ["name", "url", "slug"]
    success_url = reverse_lazy("home")


class QRCodeView(TemplateView):
    template_name = "links/qrcode.html"

    def get(self, request, *args, **kwargs):
        link_slug = self.kwargs.get("link_slug")
        link = get_object_or_404(Link, slug=link_slug)

        # Generate QR code
        img = qrcode.make(f"https://shorty-iaog.onrender.com/link/{link_slug}")

        # Create an in-memory image
        img_bytes = BytesIO()
        img.save(img_bytes)
        img_bytes.seek(0)

        # Convert the image to a data URI
        data_uri = (
            f"data:image/png;base64,{base64.b64encode(img_bytes.read()).decode()}"
        )

        # Pass the data URI to the template
        context = self.get_context_data(qrcode_data=data_uri)
        return self.render_to_response(context)
