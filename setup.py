# -*- coding: utf-8 -*-

"""The setup script."""

import sys
from setuptools import setup, find_packages

with open("README.md") as f:
    description = f.read()

setup(
    name="connio",
    author="Jose Tiago Macara Coutinho",
    author_email="coutinhotiago@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Concurrency agnostic socket API",
    license="GPLv3+",
    long_description=description,
    long_description_content_type="text/markdown",
    keywords="socket, tcp, ser2net, serial, rs232, rfc2217, asyncio",
    packages=find_packages(),
    install_requires=["serialio>=2.2", "sockio>=0.11"],
    url="https://tiagocoutinho.github.io/connio/",
    project_urls={
        "Documentation": "https://tiagocoutinho.github.io/connio/",
        "Source": "https://github.com/tiagocoutinho/connio/",
    },
    version="0.1.0",
    python_requires=">=3.5",
    zip_safe=True,
)
