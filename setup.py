# Copyright (c) 2022 Microsoft
# Licensed under The MIT License [see LICENSE for details]

from io import open

from setuptools import find_packages, setup

setup(
    name="torchscale-gml",
    version="0.2.3",
    author="TorchScale Team",
    author_email="Shuming.Ma@microsoft.com",
    description="Transformers at any scale",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="Transformers at any scale",
    license="MIT",
    url="https://github.com/microsoft/torchscale",
    package_dir = {"torchscale": "torchscale"},
    install_requires=["torch>=1.8", "fairscale~=0.4.0", "timm", "einops"],
    python_requires=">=3.8.0",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)
