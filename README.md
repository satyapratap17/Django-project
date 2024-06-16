# Django Data Analysis Project

This project allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

## Setup Instructions

1. **Clone the repository**

    ```sh
    git clone <repository_url>
    cd data_analysis_project
    ```

2. **Create a virtual environment and activate it**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the migrations**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Run the development server**

    ```sh
    python manage.py runserver
    ```

6. **Open your browser and go to**

    ```
    http://127.0.0.1:8000
    ```

## Sample CSV File

A sample CSV file `sample.csv` is included for testing purposes.
