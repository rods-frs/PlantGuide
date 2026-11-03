"""Utility for resolving file paths to the resources folder."""

from pathlib import Path

# Project root directory (where this file lives)
BASE_DIR = Path(__file__).resolve().parent
# Path to the folder containing images and other assets
RESOURCES_PATH = BASE_DIR / "resources"