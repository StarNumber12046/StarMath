import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="StarMath-StarNumber12046", # Replace with your own username
    version="0.0.1",
    author="StarNumber12046",
    author_email="starnumber12046.vivaldi.net",
    description="A math package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="github.com/starnumber12046/StarMath",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
