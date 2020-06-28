import setuptools
import subprocess
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hanzi2reading",
    version="0.1.1",
    author="Brandon Liu",
    author_email="bdon@bdon.org",
    description="Convert Mandarin text to Hanyu Pinyin, Zhuyin, and more, using swappable dictionary backends.",
    license="BSD-2-Clause",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bdon/hanzi2reading",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    scripts=['bin/hanzi2reading'],
    requires_python='>=3.0',
    package_data={'hanzi2reading':['data/*.h2r']}
)