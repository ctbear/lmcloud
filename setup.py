import setuptools

with open("README.md", "r") as f:
    readme = f.read()

setuptools.setup(
    name="lmcloud",
    version="0.4.5",
    description="A Python implementation of the new La Marzocco API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/zweckj/lmcloud",
    author="Josef Zweck",
    author_email="24647999+zweckj@users.noreply.github.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        "httpx>=0.16.1",
        "authlib>=0.15.5",
        "websockets>=11.0.2",
        "bleak>=0.20.2",
        "aiohttp>=3.8.0",
    ],
    package_data={
        "lmcloud": ["py.typed"],
    },
)
