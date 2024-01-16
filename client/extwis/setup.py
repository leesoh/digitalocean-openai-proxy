from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="extwis",
    version="0.1.0",
    author="someone",
    author_email="you@there.com",
    description="Extract wisdom",
    url="https://github.com/leesoh/digitalocean-openai-proxy",
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    entry_points={"console_scripts": ["extwis=extwis.main:main"]},
)

