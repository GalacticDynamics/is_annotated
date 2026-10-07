# /// script
# requires-python = ">=3.11"
# dependencies = ["resvg-py"]
# ///
"""Copyright (c) 2024 Nathaniel Starkman. All rights reserved.

Draw the is_annotated logo: ``Annotated[T, metadata]``, checked.

Square brackets around a type, as a teal block, and its metadata, as a purple
flag: the shape of ``Annotated[T, x]``. A yellow badge with a tick asks the
question this package answers. The shapes are vector, so the logo is written as
an SVG, sharp at any size; for a bitmap, name a .png and give its size::

    uv run docs/_static/make_logo.py                     # favicon.svg
    uv run docs/_static/make_logo.py --size 2048 big.png
"""

import argparse
from pathlib import Path

NAVY, TEAL, PURPLE = "#030a23", "#66a19a", "#7738eb"  # GalacticDynamics' colours
YELLOW = "#ffd43b"

# In a 64-unit square: the brackets' left and right x, top and bottom.
BRACKETS = (8, 50, 14, 50)
TYPE = (16, 24, 12, 16)  # the type block: x, y, width, height
FLAG = (33, 22, 42)  # the flag's pole: x, top, bottom
BADGE = (50, 48, 10)  # centre x, y, radius

SVG = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="512" height="512">
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="{brackets}" stroke="{navy}" stroke-width="4"/>
    <path d="M{fx:g} {ftop:g}V{fbottom:g}" stroke="{purple}" stroke-width="3"/>
  </g>
  <rect x="{tx:g}" y="{ty:g}" width="{tw:g}" height="{th:g}" rx="3" fill="{teal}"/>
  <path d="{flag}" fill="{purple}"/>
  <circle cx="{bx:g}" cy="{by:g}" r="{br:g}" fill="{yellow}"
    stroke="{navy}" stroke-width="2.2"/>
  <path d="{tick}" fill="none" stroke="{navy}" stroke-width="2.5"
    stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""


def brackets() -> str:
    """Return the square brackets as an SVG path, each 5 units deep."""
    left, right, top, bottom = BRACKETS
    return (
        f"M{left + 5:g} {top:g}H{left:g}V{bottom:g}H{left + 5:g}"
        f"M{right - 5:g} {top:g}H{right:g}V{bottom:g}H{right - 5:g}"
    )


def flag() -> str:
    """Return the flag's cloth as an SVG path, swallow-tailed at its free end."""
    x, top, _ = FLAG
    end, notch = x + 10, x + 7  # the cloth's free end, and its tail's notch
    return f"M{x:g} {top:g}H{end:g}L{notch:g} {top + 5:g}L{end:g} {top + 10:g}H{x:g}Z"


def tick() -> str:
    """Return the badge's tick as an SVG path."""
    x, y, r = BADGE
    s = 0.42 * r
    return f"M{x - s:g} {y:g}l{0.75 * s:g} {0.75 * s:g}l{1.4 * s:g} {-1.5 * s:g}"


def svg() -> str:
    """Return the logo as SVG text."""
    fx, ftop, fbottom = FLAG
    tx, ty, tw, th = TYPE
    bx, by, br = BADGE
    return SVG.format(
        brackets=brackets(),
        flag=flag(),
        tick=tick(),
        navy=NAVY,
        teal=TEAL,
        purple=PURPLE,
        yellow=YELLOW,
        fx=fx,
        ftop=ftop,
        fbottom=fbottom,
        tx=tx,
        ty=ty,
        tw=tw,
        th=th,
        bx=bx,
        by=by,
        br=br,
    )


def main() -> None:
    """Parse the command line and save the logo."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "out",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("favicon.svg"),
        help="output file, SVG or PNG by its extension (default: favicon.svg)",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=512,
        help="pixels per side, for a PNG",
    )
    args = parser.parse_args()

    if args.out.suffix == ".svg":
        args.out.write_text(svg())
    else:
        import resvg_py  # noqa: PLC0415  # only a PNG needs a renderer

        png = resvg_py.svg_to_bytes(svg_string=svg(), width=args.size)
        args.out.write_bytes(bytes(png))


if __name__ == "__main__":
    main()
