# Wine Quality Prediction API

This project is a FastAPI-based machine learning model API for predicting the quality of wine. It uses a Ridge regression model to make predictions based on the chemical properties of the wine.

## Features

- **FastAPI** for serving the API
- **scikit-learn** for training the Ridge regression model
- **Pydantic** for input validation
- **Heroku Deployment**: You can access the live API documentation on Heroku [here](https://wine-quality-fastapi-bdadb8c33eb6.herokuapp.com/docs).

## API Endpoints

### 1. `/predict/` (POST)

This endpoint takes various chemical properties of wine as input and returns the predicted wine quality.

- **Request Body** (example):
    ```json
    {
      "fixed_acidity": 7.4,
      "volatile_acidity": 0.7,
      "citric_acid": 0.0,
      "residual_sugar": 1.9,
      "chlorides": 0.076,
      "free_sulfur_dioxide": 11.0,
      "total_sulfur_dioxide": 34.0,
      "density": 0.9978,
      "pH": 3.51,
      "sulphates": 0.56,
      "alcohol": 9.4
    }
    ```

- **Response** (example):
    ```json
    {
      "predicted_quality": 5.0
    }
    ```

## Live API Documentation

The live API is hosted on Heroku, and you can interact with the API through the automatically generated Swagger UI documentation.

Visit: [Wine Quality Prediction API Documentation](https://wine-quality-fastapi-bdadb8c33eb6.herokuapp.com/docs)

## Getting Started

### Prerequisites

- Python 3.10 or higher
- `pip` for managing Python packages

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/wine_quality_fastapi.git
    ```

2. Navigate to the project directory:

    ```bash
    cd wine_quality_fastapi
    ```

3. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Train the machine learning model (if needed):

    ```bash
    python train_model.py
    ```

6. Start the FastAPI server:

    ```bash
    python -m uvicorn app:app --reload
    ```

7. Open your browser and visit `http://127.0.0.1:8000/docs` to interact with the API using the Swagger UI.
