# Adaptive-E-commerce-Recommendation-System-with-Feedback-Loop
Full MLOps pipeline for product recommendations. Integrates a Collaborative Filtering model with a real-time user feedback loop to enable continuous retraining and deployment via FastAPI and Docker. Demonstrates A/B testing readiness and CI/CD for model adaptation.

## 📂 Project Structure

This project adopts a standard MLOps directory structure to ensure scalability, clarity, and a clear separation of concerns between application code, data, and deployment artifacts.

| Directory | Purpose | Key Contents |
| :--- | :--- | :--- |
| **`src/`** | **Main Application Code & API Logic** | Contains all production Python code (FastAPI service, recommendation logic, helper classes). **This directory is containerized for deployment.** |
| **`data/`** | **Data Management & ETL Scripts** | Stores simulated input data, scripts for data generation (e.g., `generate_data.py`), schema definitions, and database files (e.g., `interactions.sqlite`). |
| **`notebooks/`** | **Exploration and Prototyping (PoC)** | Used exclusively for initial data analysis, rapid prototyping, and testing ideas. **Code from here is strictly non-production.** |
| **`models/`** | **Local Model Artifacts** | A temporary location for saving trained model files (e.g., via `pickle` or `joblib`) before they are formally registered and versioned by **MLflow**. |
| **`deployment/`** | **Infrastructure as Code (IaC)** | Stores all necessary configuration files for building and running the service in containers, including `Dockerfile`, `docker-compose.yml`, and CI/CD scripts. |

This structure ensures that the MLOps pipeline (CI/CD) targets only the necessary production code (`src/` and `deployment/`), keeping experiments (`notebooks/`) and raw artifacts isolated.
