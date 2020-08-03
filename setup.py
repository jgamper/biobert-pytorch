from setuptools import setup, find_packages

setup(
    name="biobert-pytorch",
    version="0.9",
    description="Ready to use BioBert pytorch weights for HuggingFace pytorch BertModel.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Jevgenij Gamper",
    author_email="jevgenij.gamper5@gmail.com",
    url="https://github.com/jgamper/biobert-pytorch",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3.6"
    ],
)
