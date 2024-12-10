from setuptools import setup, find_packages

setup(
    name="Indices_Calculator",
    version="0.1.0",
    author="Your Name",
    description="A library for calculating satellite indices (NDVI, NDWI, NDBI).",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "rasterio",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)