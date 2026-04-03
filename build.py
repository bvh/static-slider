import json
import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def main():
    root = Path(__file__).resolve().parent
    public_dir = root / "public"

    print("Cleaning public/ ...", file=sys.stderr)
    if public_dir.exists():
        shutil.rmtree(public_dir)
    public_dir.mkdir(exist_ok=True)

    print("Loading configuration ...", file=sys.stderr)
    context = load_config(root)

    jinja_env = Environment(loader=FileSystemLoader(str(root / "templates")))
    print("Building pages ...", file=sys.stderr)
    build_index(jinja_env, context, public_dir)
    build_image_pages(jinja_env, context, public_dir, root / "images")

    print("Copying static assets ...", file=sys.stderr)
    copy_static_assets(root, public_dir)

    print("Build complete.", file=sys.stderr)
    return 0


def load_config(root):
    """Read config.json and gallery.json, merge into template context."""
    with open(root / "config.json") as f:
        config = json.load(f)
    with open(root / "images" / "gallery.json") as f:
        gallery_data = json.load(f)

    # merge site-level keys from both files
    site = {**config["site"], **gallery_data["site"]}

    gallery = site.pop("gallery")
    images = gallery.pop("images")

    return {"site": site, "gallery": gallery, "images": images}


def build_index(env, context, public_dir):
    """Render index.html template to public/index.html."""
    template = env.get_template("index.html")
    html = template.render(**context)
    (public_dir / "index.html").write_text(html, encoding="utf-8")
    print(f"  Wrote index.html ({len(context['images'])} images)", file=sys.stderr)


def build_image_pages(env, context, public_dir, images_src):
    """Render per-image detail pages and copy source images."""
    template = env.get_template("image.html")
    for img in context["images"]:
        img_dir = public_dir / img["id"]
        img_dir.mkdir(exist_ok=True)

        # copy source image
        src = images_src / img["filename"]
        if src.exists():
            shutil.copy2(src, img_dir / img["filename"])
        else:
            print(f"*** WARNING: Source image not found: {src}", file=sys.stderr)

        # render detail page
        html = template.render(site=context["site"], gallery=context["gallery"], img=img)
        (img_dir / "index.html").write_text(html, encoding="utf-8")
        print(f"  Wrote {img['id']}/index.html", file=sys.stderr)


def copy_static_assets(root, public_dir):
    """Copy css/ and js/ directories into public/."""
    for dirname in ("css", "js"):
        src = root / dirname
        dst = public_dir / dirname
        if src.exists():
            shutil.copytree(src, dst)
            print(f"  Copied {dirname}/", file=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())
