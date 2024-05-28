from setuptools import setup, find_packages


setup(
    name="prediction_model",
    version="1.0.0",
    author="Prateek Kamboj",
    author_email="parteekkamboj112@gmail.com",
    description="A prediction model package",
    long_description_content_type="text/markdown",
    url="https://github.com/keetrap/Packaging_ml_models",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "joblib"

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
