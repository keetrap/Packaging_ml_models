import os

# Define the directory structure
directories = [
    "prediction_model/config",
    "prediction_model/datasets",
    "prediction_model/processing",
    "prediction_model/trained_models",
    "tests"
]

# Define the files to be created
files = [
    "MANIFEST.in",
    "prediction_model/config/config.py",
    "prediction_model/config/__init__.py",
    "prediction_model/datasets/__init__.py",
    "prediction_model/datasets/test.csv",
    "prediction_model/datasets/train.csv",
    "prediction_model/__init__.py",
    "prediction_model/pipeline.py",
    "prediction_model/predict.py",
    "prediction_model/processing/data_handling.py",
    "prediction_model/processing/__init__.py",
    "prediction_model/processing/preprocessing.py",
    "prediction_model/trained_models/classification.pkl",
    "prediction_model/trained_models/__init__.py",
    "prediction_model/training_pipeline.py",
    "prediction_model/VERSION",
    #    "README.md",
    "requirements.txt",
    "setup.py",
    "tests/pytest.ini",
    "tests/test_prediction.py"
]

# Create the directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create the files
for file in files:
    with open(file, 'w') as f:
        pass

print("File structure created successfully.")

