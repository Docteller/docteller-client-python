import setuptools


packagename = "docteller"
version = "1.0.0"
description = "Docteller Client in Python"

with open("requirements.txt") as f:
    required = f.read().splitlines()

setuptools.setup(
    name=packagename,
    version=version,
    description=description,
    long_description=open("README.md").read(),
    packages=setuptools.find_packages(),
    install_requires=required,
    include_package_data=True,
    zip_safe=False,
)
