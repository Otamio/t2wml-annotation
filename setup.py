import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    install_requires = list()
    for line in f:
        re = line.strip()
        if re:
            install_requires.append(re)


setuptools.setup(
    name="t2wml-annotation",
    version="0.0.3",
    author="Amandeep Singh",
    author_email="amandeep.s.saggu@gmail.com",
    description="T2WML lite: annotation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usc-isi-i2/t2wml-annotation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    include_package_data=True,
    install_requires=install_requires,
    package_data={'datamart': ['resources/*.json','resources/*.csv', 'resources/*.xlsx', 'resources/*.yaml', 'resources/*.tsv']}
)
