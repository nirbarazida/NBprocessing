from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='NBprocessing',
    version='0.0.18832',
    author="Nir Barazida",
    author_email="nirbarazida@gmail.com",
    description="Pre-processing database using pre-written functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nirbarazida/NBprocessing",
    packages=find_packages(exclude=['*test*', 'main*','ignore_files*']),
    install_requires=['pandas', 'numpy', 'matplotlib', 'seaborn'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

