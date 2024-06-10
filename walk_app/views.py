from django.shortcuts import render, get_object_or_404
from .models import Panorama, Marker
import json

def panorama_detail(request, pk):
    panorama = get_object_or_404(Panorama, pk=pk)
    markers = Marker.objects.filter(panorama=panorama)
    markers_json = json.dumps([
        {
            'id': marker.id,
            'x_coordinate': marker.x_coordinate,
            'y_coordinate': marker.y_coordinate,
            'tooltip_text': marker.tooltip_text,
            'linked_panorama_url': marker.linked_panorama.get_absolute_url() if marker.linked_panorama else None
        } for marker in markers
    ])
    return render(request, 'walk_app/base.html', {
        'panorama': panorama,
        'markers_json': markers_json
    })

