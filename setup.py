from setuptools import setup, find_packages

setup(
    name="shield-auth",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "bcrypt",
    ],
    author="angyedz",
    description="Библиотека для безопасного хеширования паролей",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
)