import os

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="naivenlp",
    version="0.0.3",
    description="NLP toolkit, including tokenization, sequence tagging, etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luozhouyang/naivenlp",
    author="ZhouYang Luo",
    author_email="zhouyang.luo@gmail.com",
    packages=setuptools.find_packages(),
    # include_package_data=True,
    package_data={

    },
    install_requires=[
        "jieba",
        "numpy",
        "pycorrector",
        "strsimpy",
    ],
    dependency_links=[
        "git+https://github.com/kpu/kenlm.git"
    ],
    extras_require={

    },
    license="Apache Software License",
    classifiers=(
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    )
)
