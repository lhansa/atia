# setup.py
from setuptools import setup, find_packages

setup(
    name="atia",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'psutil', 'python-xlib'
    ],
    entry_points={
        'console_scripts': [
            'atia=atia.cli:main',
        ],
    },
    author="Leonardo Hansa Torres",
    author_email="hola@leonardohansa.com",
    description="Una aplicación para medir tiempo de uso de programas en Linux",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lhansa/atia",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.10",
)