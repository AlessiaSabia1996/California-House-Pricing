# setup.py

from setuptools import setup, find_packages

setup(
    name="MlOps-project",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "scikit-learn",
        "pandas",
        "joblib",
        "click",
        "flask"
    ],
    entry_points={
        "console_scripts": [
            "predict-price=mlopsapp.predict:predict"
        ]
    }
)
