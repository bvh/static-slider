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
