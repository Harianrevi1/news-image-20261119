#!/usr/bin/env python3
"""Publish the finished front page for 19 November 2026.

The newspaper image is rendered ahead of time and shipped with this
repository as ``entry.png``.  This script does one small, predictable
job: it copies that picture byte-for-byte into the output directory the
harness points at, so the judging pipeline can pick it up as
``entry.png``.

Behaviour in one paragraph: the output folder comes from the
``MAKEFUN_OUTPUT_DIR`` environment variable and falls back to
``/output`` when the variable is absent; the source picture lives in
the same folder as this script; the destination file is created (along
with any missing parent folders) and overwritten if it already exists;
the script prints the destination path and the number of bytes written,
then exits zero.  It uses only the Python standard library, touches no
network, and writes nothing else, so running it twice over the same
input always yields identical output bytes.
"""

import os
import shutil
import sys
from pathlib import Path

SOURCE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def locate_source() -> Path:
    """Return the path of the bundled front-page image."""
    here = Path(__file__).resolve().parent
    return here / SOURCE_NAME


def resolve_output_dir() -> Path:
    """Return the output directory from the environment, or the default."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    chosen = raw.strip() or DEFAULT_OUTPUT_DIR
    return Path(chosen)


def publish(source: Path, output_dir: Path) -> Path:
    """Copy the source image into the output directory as entry.png."""
    if not source.is_file():
        raise FileNotFoundError(f"bundled image not found: {source}")
    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / SOURCE_NAME
    shutil.copyfile(source, destination)
    # Guard against a truncated write: the copy must be exactly as big
    # as the bundled picture, otherwise something went wrong mid-copy.
    if destination.stat().st_size != source.stat().st_size:
        raise OSError(f"copy incomplete: {destination}")
    return destination


def main() -> int:
    source = locate_source()
    output_dir = resolve_output_dir()
    try:
        destination = publish(source, output_dir)
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    size = destination.stat().st_size
    print(f"wrote {destination} ({size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
