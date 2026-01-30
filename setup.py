from setuptools import setup, find_packages

setup(
    name="shield_auth",
    version="1.0.3",
    description="Библиотека для безопасного хранения паролей в TXT",
    author="angyedz",
    packages=find_packages(),
    install_requires=[
        "passlib>=",
    ],
    python_requires='>=3.7',
)