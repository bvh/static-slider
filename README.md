# Static Slider

HTML/CSS gallery and slider widget, built with minimal JavaScript.

## Usage

### Setup Source Images and Gallery Config

1. Copy all of the images you wish to display into the `images/` folder in the
source root.
2. Create a `gallery.json` file using the template below. and place it into the
`images/` folder as well.

### Generate the Gallery

Use `uv` to run the Python3 script:
```
uv run generate.py
```

### Verify

You should be able to view the gallery locally by opening `public/index.html`
in your browser of choice:
```
open public/index.html
```

## Gallery Config File

Example gallery configuration file.
```
{
    "site": {
        "title": "My Site",
        "gallery": {
            "title": "My Gallery",
            "images": [
                {
                    "id": "photo1",
                    "filename": "photo1.jpg",
                    "title": "Cool Sunset",
                    "description": "A cool sunset on a winter day.",
                    "artist": "John Doe",
                    "number": 1,
                    "date": "2026-01-30",
                    "month": "January",
                    "year": "2026"
                    "camera": "NIKON Z 8",
                    "lens": "NIKKOR Z 100-400mm f/4.5-5.6 VR S",
                    "focallength": "100mm",
                    "focallength35": "100mm",
                    "aperture": "f/8",
                    "shutterspeed": "1/320",
                    "iso": "64",
                },
                {
                    "id": "photo2",
                    "filename": "photo2.jpg",
                    "title": "Summer Barn",
                    "description": "A weathered barn stands among late summer wheat.",
                    "artist": "Jane Doe",
                    "number": 2,
                    "date": "2025-08-17",
                    "camera": "NIKON Z 7",
                    "lens": "NIKKOR Z 24-200mm f/4-6.3 VR",
                    "focallength": "39mm",
                    "focallength35": "39mm",
                    "aperture": "f/11",
                    "shutterspeed": "1/40",
                    "iso": 220,
                    "month": "August",
                    "year": "2025"
                }
            ]
        }
    }
}
```