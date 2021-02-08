import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="copper-sdk",
    version="1.0.1",
    author="Claimer Tech Ltd",
    author_email="dev@claimer.com",
    description="Unofficial Copper CRM SDK written in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ClaimerApp/copper-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
