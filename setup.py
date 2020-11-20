import setuptools
from uminifier import __version__, __author__, __email__

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as rf:
    requirements = rf.readlines()

setuptools.setup(
    name="uminifier",
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yeyeto2788/uminifier",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
    entry_points={"console_scripts": ["uminifier=uminifier:main"]}
)
