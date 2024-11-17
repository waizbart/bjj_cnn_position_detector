const videoElement = document.getElementById('videoElement');
const uploadedVideo = document.getElementById('uploadedVideo');
const canvas = document.getElementById('canvas');
const outputImage = document.getElementById('outputImage');
const startWebcamBtn = document.getElementById('startWebcamBtn');
const videoUploadInput = document.getElementById('videoUploadInput');

let socket;
let streaming = false;

function startWebSocket() {
    socket = new WebSocket("ws://localhost:8000/ws/analyze/");

    socket.onopen = () => {
        console.log("Conexão WebSocket estabelecida.");
    };

    socket.onmessage = event => {
        const data = JSON.parse(event.data);
        if (data.error) {
            console.error("Erro do servidor:", data.error);
        } else {
            console.log("Posição detectada:", data.position_detected);
       
            outputImage.src = 'data:image/jpeg;base64,' + data.image_with_keypoints;
        }
    };

    socket.onclose = () => {
        console.log("Conexão WebSocket encerrada.");
    };
}

function captureAndSendFrames(video) {
    const ctx = canvas.getContext('2d');

    function sendFrame() {
        if (!streaming) return;

        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        canvas.toBlob(blob => {
            const reader = new FileReader();
            reader.onloadend = () => {
                const base64data = reader.result.split(',')[1]; 
        
                socket.send(base64data);
            };
            reader.readAsDataURL(blob);
        }, 'image/jpeg', 0.7); 

        setTimeout(sendFrame, 100); 
    }

    sendFrame();
}

startWebcamBtn.addEventListener('click', () => {
    if (streaming) return;

    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            videoElement.srcObject = stream;
            videoElement.style.display = 'block';
            uploadedVideo.style.display = 'none';
            outputImage.style.display = 'block';
            streaming = true;
            startWebSocket();
            captureAndSendFrames(videoElement);
        })
        .catch(error => {
            console.error('Erro ao acessar a webcam:', error);
        });
});

videoUploadInput.addEventListener('change', event => {
    const file = event.target.files[0];
    if (!file) return;

    if (streaming) return;

    const url = URL.createObjectURL(file);
    uploadedVideo.src = url;
    uploadedVideo.style.display = 'block';
    videoElement.style.display = 'none';
    outputImage.style.display = 'block';
    streaming = true;
    startWebSocket();

    uploadedVideo.onloadedmetadata = () => {
        uploadedVideo.play();
        captureAndSendFrames(uploadedVideo);
    };

    uploadedVideo.onended = () => {
        streaming = false;
        socket.close();
        console.log("Reprodução do vídeo finalizada.");
    };
});
