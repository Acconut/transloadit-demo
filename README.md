# Transloadit Demo

This project is an example for how to integrate Transloadit into an application. The backend is powered by Flask using Python 3. On the front-end Bootstrap and Uppy.js is used.

## Installation

```
pip install -r requirements.txt
```

## Usage

1. Sign up for a Transloadit account.
2. Create a new Transloadit template with following content:
```json
{
  "steps": {
    "scan": {
      "use": ":original",
      "robot": "/file/virusscan"
    },
    "image": {
      "use": "scan",
      "robot": "/file/filter",
      "accepts": [
        [
          "${file.type}",
          "=",
          "image"
        ]
      ]
    },
    "video": {
      "use": "scan",
      "robot": "/file/filter",
      "accepts": [
        [
          "${file.type}",
          "=",
          "video"
        ]
      ]
    },
    "pdf": {
      "use": "scan",
      "robot": "/file/filter",
      "accepts": [
        [
          "${file.type}",
          "=",
          "pdf"
        ]
      ]
    },
    "image-thumbnail": {
      "use": "image",
      "robot": "/image/resize",
      "format": "png",
      "imagemagick_stack": "v2.0.7"
    },
    "video-thumbnail": {
      "use": "video",
      "robot": "/video/thumbs",
      "count": 1,
      "ffmpeg_stack": "v3.3.3"
    },
    "pdf-thumbnail": {
      "use": "pdf",
      "robot": "/document/thumbs",
      "page": 1,
      "imagemagick_stack": "v2.0.7"
    },
    "thumbnail": {
      "use": [
        "image-thumbnail",
        "video-thumbnail",
        "pdf-thumbnail"
      ],
      "robot": "/image/resize",
      "width": 500,
      "height": 500,
      "resize_strategy": "fit",
      "imagemagick_stack": "v2.0.7"
    }
  }
}
```
3. Replace YOUR_AUTH_KEY and YOUR_TEMPLATE_ID in `static/app.js` with your values.
4. Start the server using `FLASK_APP=server.py FLASK_ENV=development flask run`
