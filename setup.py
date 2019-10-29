import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smsedge_api_python-SMSEdge", # Replace with your own username
    version="1.0.0",
    author="Mimon Copitman",
    author_email="mimon@smsedge.io",
    description="SMSEdge API package for Python development",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SMSEdge/API-Python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License, Version 1.1 (Apache-1.1)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)