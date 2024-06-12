from django.shortcuts import render, get_object_or_404
from .models import Panorama, Marker
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .forms import SubscriptionForm


@csrf_exempt
def subscribe(request):
    if request.method == "POST":
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscriber = form.save(commit=False)
            subscriber.ip_address = request.META.get("REMOTE_ADDR")
            subscriber.save()
            return JsonResponse(
                {"message": "You have successfully subscribed!"}, status=200
            )
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        form = SubscriptionForm()
        return render(request, "walk_app/subscription.html", {"form": form})


def panorama_detail(request, pk):
    panorama = get_object_or_404(Panorama, pk=pk)
    markers = Marker.objects.filter(panorama=panorama)
    markers_json = json.dumps(
        [
            {
                "id": marker.id,
                "x_coordinate": marker.x_coordinate,
                "y_coordinate": marker.y_coordinate,
                "tooltip_text": marker.tooltip_text,
                "linked_panorama_url": (
                    marker.linked_panorama.get_absolute_url()
                    if marker.linked_panorama
                    else None
                ),
            }
            for marker in markers
        ]
    )
    return render(
        request,
        "walk_app/base.html",
        {"panorama": panorama, "markers_json": markers_json},
    )
