from setuptools import setup, find_packages
import os

# Read version from VERSION file
with open("../VERSION") as f:
    version = f.read().strip().rsplit("-", 1)[0]
    # Get only the first part (without develop suffix)

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open("../README.md", encoding="utf-8") as f:
        long_description = f.read()
except Exception:
    long_description = ""

setup(
    # Name of the package
    name="qbit_manage_mod",
    # Start with a small number and increase it with
    # every change you make https://semver.org
    version=version,
    # Packages to include into the distribution
    packages=find_packages(),
    py_modules=["qbit_manage"],
    python_requires=">=3.9",
    install_requires= [
    "argon2-cffi==25.1.0",
    "bencodepy==0.9.5",
    "croniter==6.0.0",
    "fastapi==0.122.0",
    "GitPython==3.1.45",
    "humanize==4.13.0",
    "pytimeparse2==1.7.1",
    "qbittorrent-api==2025.11.1",
    "requests==2.32.5",
    "retrying==1.4.2",
    "ruamel.yaml==0.18.16",
    "slowapi==0.1.9",
    "uvicorn==0.38.0",
    "pre-commit==4.3.0",
    "ruff==0.14.6",
],
    # Chose a license from here: https: //
    # help.github.com / articles / licensing - a -
    # repository. For example: MIT
    license="MIT",
    # Short description of your library
    description=(
        "This tool will help manage tedious tasks in qBittorrent and automate them. "
        "Tag, categorize, remove Orphaned data, remove unregistered torrents and much much more."
    ),
    # Long description of your library
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Your name
    author="Th3_DoC",
    # Either the link to your github or to your website
    url="https://github.com/Th3-DoC/qbit_manage_mod",
)
