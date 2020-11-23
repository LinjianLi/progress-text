import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="progress-text-llj", # Replace with your own package name and username
    version="0.0.1",
    author="Linjian Li",
    author_email="author@example.com",
    description="Python script for printing progress in text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LinjianLi/progress-text",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License Version 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
