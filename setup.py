import setuptools

with open("README.md", "r") as fh:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "disease_classification"
AUTHOR_USER_NAME = "Aryan Tomar"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "aryantomar01.at@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    }
)