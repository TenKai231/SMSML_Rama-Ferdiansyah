# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commonly Used Commands

- **Train standard model:** `python modelling.py [n_estimators] [max_depth]`
  - Example: `python modelling.py 100 10`
  - Runs a single Random Forest training pass and logs to MLflow.
- **Run hyperparameter optimization:** `python modellingopt.py`
  - Performs a basic Grid Search over `n_estimators` and `max_depth` and logs the best model.
- **View MLflow Experiments:** `mlflow ui`
  - Access the UI in a browser at `http://127.0.0.1:5000`.
- **Install Dependencies:** 
  - Using pip: `pip install -r requirements.txt`
  - Using Conda: `conda env create -f environment.yml` (environment name is `credit_scoring`)

## High-Level Architecture

- **Domain:** Credit Scoring Classification using a Random Forest model (`scikit-learn`).
- **Data:** Relies on pre-processed datasets (`train_pca.csv`, `test_pca.csv`) implying that Principal Component Analysis (PCA) feature extraction has already been completed in an earlier pipeline step.
- **Experiment Tracking:** Uses `MLflow` for logging metrics (accuracy), parameters, and artifacts (saved models). By default, tracking URIs are configured to write to a local `mlruns/` directory rather than a central server.
- **Key Scripts:**
  - `modelling.py`: Responsible for training a single model run. Automatically logs via `mlflow.autolog()` and explicitly logs the `RandomForestClassifier` model.
  - `modellingopt.py`: Responsible for hyperparameter tuning. It loops over predefined ranges for estimators and tree depth, logs each run, and explicitly saves the best model based on accuracy.
