import { Viewer } from '@photo-sphere-viewer/core';
import { MarkersPlugin } from '@photo-sphere-viewer/markers-plugin';

const panoramas = [
    '/static/images/hotel.jpeg',
    '/static/images/room1.jpg',
    '/static/images/room2.jpg',
    '/static/images/room3.jpg',
];
let currentPanoramaIndex = 0;

const viewer = new Viewer({
    container: 'viewer',
    panorama: panoramas[currentPanoramaIndex],
    caption: 'Parc national du Mercantour <b>&copy; Damien Sorel</b>',
    loadingImg: '/static/images/1474.gif', 
    touchmoveTwoFingers: true,
    mousewheelCtrlKey: true,

    plugins: [
        [MarkersPlugin, {
            markers: [
                {
                    id: 'image',
                    position: { yaw: 2, pitch: -0.1 },
                    image: '/static/images/pin-blue.png', 
                    size: { width: 32, height: 32 },
                    anchor: 'bottom center',
                    tooltip: 'A image marker. <b>Click here!</b>',
                    data: { nextPanorama: panoramas[currentPanoramaIndex + 1], prevPanorama: panoramas[currentPanoramaIndex - 1] }
                }
            ],
        }],
    ],
});

const markersPlugin = viewer.getPlugin(MarkersPlugin);

markersPlugin.addEventListener('select-marker', ({ marker }) => {
    if (marker.data) {
        if (marker.data.nextPanorama) {
            currentPanoramaIndex++;
            if (currentPanoramaIndex >= panoramas.length) {
                currentPanoramaIndex = 0; 
            }
            viewer.setPanorama(panoramas[currentPanoramaIndex]);
        } else if (marker.data.prevPanorama) {
            currentPanoramaIndex--;
            if (currentPanoramaIndex < 0) {
                currentPanoramaIndex = panoramas.length - 1; 
            }
            viewer.setPanorama(panoramas[currentPanoramaIndex]);
        }
    }
});
