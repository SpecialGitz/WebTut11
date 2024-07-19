console.log("hello world!");

const videoElement = document.getElementById('videoElement');
const canvasElement = document.getElementById('canvasElement');
const photoElement = document.getElementById('photoElement');
const startVideo = document.getElementById('startVideo');
const stopVideo = document.getElementById('stopVideo');
const capturePhoto = document.getElementById('capturePhoto');

const uploadForm = document.getElementById('uploadForm');


let stream;

async function startWebcam() {
    try {
        stream = await navigator.mediaDevices.getUserMedia({ video: true });
        videoElement.srcObject = stream;
        startVideo.disabled = true;
        stopVideo.disabled = false;
        capturePhoto.disabled = false;
    } catch (error) {
        console.error('Error accessing webcam:', error);
    }
}

startVideo.addEventListener('click', startWebcam);

function capture_photo() {
    canvasElement.width = videoElement.videoWidth;
    canvasElement.height = videoElement.videoHeight;
    canvasElement.getContext('2d').drawImage(videoElement, 0, 0);
    photoDataUrl = canvasElement.toDataURL('image/png'); // PNG format

    console.log(photoDataUrl);

    document.getElementById('imageDataInput').value = photoDataUrl;
}

capturePhoto.addEventListener('click', capture_photo);

async function stopWebcam() {
    stream.getVideoTracks()[0].stop();
    videoElement.srcObject = null;
    startVideo.disabled = false;
    stopVideo.disabled = true;
    photoElement.style.display = 'none';
}

stopVideo.addEventListener('click', stopWebcam);


uploadForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const formData = new FormData(uploadForm);
    console.log('Uploading photo:', formData);

    fetch('/save_camera_image/', {
        method: 'POST',
        body: formData,

    }).then(response => {
        if (response.ok) {
            console.log('Photo saved successfully');
            alert('Photo saved successfully');
        } else {
            console.error('Error saving photo');
        }
    }).catch(error => {
        console.error('Error:', error);
    });
});