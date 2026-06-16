#!/usr/bin/env python3
"""Generate responsive clean page background and carousel exports."""

from __future__ import annotations

import json
import math
import os
import re
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
SET_ID = os.environ.get("PAGE_BG_SET_ID", "pages-10-20260616")
ASSET_ROOT = ROOT / "assets/page-backgrounds" / SET_ID
STATIC_ROOT = ROOT / "static/page-backgrounds" / SET_ID
SOURCE_DIR = ASSET_ROOT / "source-clean"


FORMATS = [
    {
        "key": "background_desktop_16x9",
        "dir": "background/desktop-16x9-3840x2160",
        "suffix": "bg-desktop-16x9-3840x2160",
        "size": (3840, 2160),
        "dpi": 300,
        "quality": 92,
        "focus": (0.58, 0.50),
        "purpose": "HTML5 page background for desktop and large tablets",
    },
    {
        "key": "background_tablet_4x3",
        "dir": "background/tablet-4x3-2048x1536",
        "suffix": "bg-tablet-4x3-2048x1536",
        "size": (2048, 1536),
        "dpi": 300,
        "quality": 92,
        "focus": (0.60, 0.50),
        "purpose": "HTML5 page background for tablets",
    },
    {
        "key": "background_mobile_9x16",
        "dir": "background/mobile-9x16-1440x2560",
        "suffix": "bg-mobile-9x16-1440x2560",
        "size": (1440, 2560),
        "dpi": 300,
        "quality": 91,
        "focus": (0.64, 0.50),
        "purpose": "HTML5 page background for phones",
    },
    {
        "key": "background_mobile_9x16_2x",
        "dir": "background/mobile-9x16-2160x3840",
        "suffix": "bg-mobile-9x16-2160x3840",
        "size": (2160, 3840),
        "dpi": 300,
        "quality": 92,
        "focus": (0.64, 0.50),
        "purpose": "high-density mobile page background",
    },
    {
        "key": "carousel_wide_16x9",
        "dir": "carousel/wide-16x9-2560x1440",
        "suffix": "carousel-wide-16x9-2560x1440",
        "size": (2560, 1440),
        "dpi": 300,
        "quality": 92,
        "focus": (0.55, 0.50),
        "purpose": "landscape carousel slide",
    },
    {
        "key": "carousel_square_1x1",
        "dir": "carousel/square-1x1-1600x1600",
        "suffix": "carousel-square-1x1-1600x1600",
        "size": (1600, 1600),
        "dpi": 300,
        "quality": 91,
        "focus": (0.60, 0.50),
        "purpose": "square carousel and social cards",
    },
    {
        "key": "carousel_portrait_4x5",
        "dir": "carousel/portrait-4x5-1600x2000",
        "suffix": "carousel-portrait-4x5-1600x2000",
        "size": (1600, 2000),
        "dpi": 300,
        "quality": 91,
        "focus": (0.62, 0.50),
        "purpose": "portrait carousel slide",
    },
    {
        "key": "carousel_story_9x16",
        "dir": "carousel/story-9x16-1080x1920",
        "suffix": "carousel-story-9x16-1080x1920",
        "size": (1080, 1920),
        "dpi": 300,
        "quality": 90,
        "focus": (0.64, 0.50),
        "purpose": "mobile story carousel slide",
    },
]


TOPICS = [
    ("01-orbital-station-observation", "Orbital station observation deck", 0.58, 0.50),
    ("02-eva-spacewalk", "EVA outside orbital station", 0.66, 0.50),
    ("03-station-laboratory", "Microgravity laboratory on station", 0.58, 0.50),
    ("04-lunar-transfer", "Lunar transfer spacecraft", 0.64, 0.50),
    ("05-lunar-surface-excursion", "Lunar surface educational excursion", 0.58, 0.54),
    ("06-orbital-classroom", "Orbital station classroom", 0.64, 0.50),
    ("07-moon-return-docking", "Return docking after lunar mission", 0.66, 0.50),
    ("08-orbital-sunrise-corridor", "Orbital sunrise station corridor", 0.70, 0.50),
    ("09-eva-airlock-prep", "EVA airlock preparation", 0.60, 0.52),
    ("10-mission-control-classroom", "Mission control classroom connected to orbit", 0.66, 0.50),
]


def source_path(slug: str) -> Path:
    clean_slug = re.sub(r"^\d{2}-", "", slug)
    return SOURCE_DIR / f"astronautiste-page-bg-{slug}-source.png"


def cover_crop(img: Image.Image, size: tuple[int, int], focus_x: float, focus_y: float) -> Image.Image:
    src_w, src_h = img.size
    dst_w, dst_h = size
    scale = max(dst_w / src_w, dst_h / src_h)
    scaled_w = math.ceil(src_w * scale)
    scaled_h = math.ceil(src_h * scale)
    resized = img.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS)

    max_left = max(0, scaled_w - dst_w)
    max_top = max(0, scaled_h - dst_h)
    left = round(max_left * min(1, max(0, focus_x)))
    top = round(max_top * min(1, max(0, focus_y)))
    return resized.crop((left, top, left + dst_w, top + dst_h))


def polish(img: Image.Image) -> Image.Image:
    img = ImageEnhance.Color(img).enhance(0.96)
    img = ImageEnhance.Contrast(img).enhance(1.035)
    return img.filter(ImageFilter.UnsharpMask(radius=0.9, percent=52, threshold=3))


def make_contact_sheet(paths: list[Path], out: Path, cols: int, cell: tuple[int, int]) -> None:
    cell_w, cell_h = cell
    gap = 12
    rows = math.ceil(len(paths) / cols)
    sheet = Image.new("RGB", (cols * cell_w + (cols + 1) * gap, rows * cell_h + (rows + 1) * gap), "#0a0a0a")
    for i, path in enumerate(paths):
        img = Image.open(path).convert("RGB")
        img.thumbnail((cell_w, cell_h), Image.Resampling.LANCZOS)
        row, col = divmod(i, cols)
        x = gap + col * (cell_w + gap) + (cell_w - img.width) // 2
        y = gap + row * (cell_h + gap) + (cell_h - img.height) // 2
        sheet.paste(img, (x, y))
    sheet.save(out, quality=90, dpi=(144, 144), optimize=True)


def main() -> None:
    for fmt in FORMATS:
        (STATIC_ROOT / fmt["dir"]).mkdir(parents=True, exist_ok=True)

    topics = []
    contact_by_format: dict[str, list[Path]] = {fmt["key"]: [] for fmt in FORMATS}

    for idx, (slug, title, topic_focus_x, topic_focus_y) in enumerate(TOPICS, start=1):
        source = source_path(slug)
        if not source.exists():
            raise FileNotFoundError(source)
        src_img = Image.open(source).convert("RGB")
        urls = {}
        assets = {}

        for fmt in FORMATS:
            focus_x = (topic_focus_x + fmt["focus"][0]) / 2
            focus_y = (topic_focus_y + fmt["focus"][1]) / 2
            out_dir = STATIC_ROOT / fmt["dir"]
            out = out_dir / f"astronautiste-page-bg-{slug}-{fmt['suffix']}.jpg"
            crop = polish(cover_crop(src_img, fmt["size"], focus_x, focus_y))
            crop.save(out, quality=fmt["quality"], dpi=(fmt["dpi"], fmt["dpi"]), optimize=True, progressive=True)
            assets[fmt["key"]] = str(out.relative_to(ROOT))
            urls[fmt["key"]] = "/" + str(out.relative_to(ROOT / "static"))
            contact_by_format[fmt["key"]].append(out)

        topics.append({
            "index": idx,
            "slug": slug,
            "title": title,
            "source": str(source.relative_to(ROOT)),
            "source_size": list(src_img.size),
            "assets": assets,
            "urls": urls,
        })

    for fmt in FORMATS:
        contact_dir = STATIC_ROOT / "_contact-sheets"
        contact_dir.mkdir(parents=True, exist_ok=True)
        make_contact_sheet(
            contact_by_format[fmt["key"]],
            contact_dir / f"{fmt['key']}.jpg",
            cols=2 if fmt["size"][0] >= fmt["size"][1] else 5,
            cell=(480, 270) if fmt["size"][0] >= fmt["size"][1] else (216, 384),
        )

    manifest = {
        "version": "20260616",
        "set_id": SET_ID,
        "brand": "Astronautiste",
        "mode": "clean_no_text_responsive",
        "formats": {
            fmt["key"]: {
                "path": fmt["dir"],
                "size": list(fmt["size"]),
                "dpi": fmt["dpi"],
                "text": False,
                "purpose": fmt["purpose"],
            }
            for fmt in FORMATS
        },
        "topics": topics,
    }
    (ASSET_ROOT / "responsive-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (STATIC_ROOT / "responsive-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {len(TOPICS)} topics x {len(FORMATS)} responsive variants")
    print(STATIC_ROOT)


if __name__ == "__main__":
    main()
