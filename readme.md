# BJJ Position Classifier AI

An artificial intelligence system for automatic classification of Brazilian Jiu-Jitsu positions and techniques using computer vision and machine learning.

## Overview

This scientific research project develops a system that uses computer vision models to:

1. Detect fighters in Jiu-Jitsu images/videos
2. Extract keypoints from the athletes' bodies
3. Classify the current technical position (e.g., mount, closed guard, etc.)

The system achieves over 90% accuracy in classifying 10 fundamental BJJ positions.

## Technologies Used

- **Pose Detection**: ViTPose (Vision Transformer for Human Pose Estimation)
- **Classification**: TensorFlow/Keras
- **Backend/API**: FastAPI
- **Image Processing**: OpenCV, PIL
- **Others**: NumPy, Pandas

## Dataset

The project uses the public Jiu-Jitsu dataset available at:
<https://vicos.si/resources/jiujitsu/>

## Project Structure

```
bjj_ia/
├── api/                # FastAPI API to serve the model
├── assets/             # Static resources
├── core/               # Core detection and classification logic
├── dataset/            # Training data
├── models/             # Trained models
├── pipelines/          # Different versions of training pipelines
│   ├── v1/             # Initial version with one person
│   ├── v2/             # Training with all people + COCO dataset
│   ├── v3/             # Training with x,y coordinates without score
│   ├── v4/             # Duplication of keypoints with inverted positions
│   └── v5/             # Augmentation in keypoint preprocessing
├── scrapper/           # Data collection tools
├── utils/              # Helper functions
└── demo.ipynb          # Notebook for system demonstration
```

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/bjj_ia.git
cd bjj_ia
```

2. Install dependencies:

```
# For GPU (recommended for better performance)
pip install -r requirements_gpu.txt

# For CPU only
pip install -r requirements.txt
```

3. Download pre-trained models:
Models are downloaded automatically on first execution.

## How to Use

### Interactive Demo

Run the `demo.ipynb` notebook to test the system with your own images:

```
jupyter notebook demo.ipynb
```

### REST API

Start the FastAPI server:

```
cd api
uvicorn main:app --reload
```

Available endpoints:

- `POST /analyze/`: Analyzes a single image
- `WebSocket /ws/analyze/`: Real-time connection for image analysis

## Classified Positions

The system classifies the following positions:

- Standing
- Takedown
- Open Guard
- Half Guard
- Closed Guard
- 50/50 Guard
- Side Control
- Mount
- Back
- Turtle

## Project Evolution

- **v1**: Initial version with training using only one person in the images
- **v2**: Training using all people in the image and COCO dataset
- **v3**: Attempt to train with only x and y values, without the score
- **v4**: Duplicating keypoints from the initial dataset using inverted positions for both fighters
- **v5**: Adding augmentation to keypoint preprocessing

## Running with Docker

```
docker build -t bjj_ia .
docker run -p 8000:8000 bjj_ia
```

## Contributions

Contributions are welcome! See `todo.md` for planned upcoming tasks.
