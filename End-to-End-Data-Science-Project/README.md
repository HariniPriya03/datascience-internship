# END-TO-END-DATA-SCIENCE-PROJECT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: G. HARINI PRIYA

*INTERN ID*: CT04DN652

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## Project Overview

In this project, I created a simple yet effective machine learning web application that predicts a student’s exam score based on the number of hours they studied. By training a linear regression model on a small dataset containing study hours and corresponding scores, the app learns the underlying relationship and provides real-time predictions. This project serves as a practical example of an end-to-end ML workflow—from data handling and model training to deploying a user-friendly web interface.

The goal was to build an accessible app where users can input their study hours and immediately see an estimated exam score, demonstrating how machine learning models can be integrated into everyday applications.

## How the Project Works

### Training the Model

I started by using pandas to load a CSV file containing historical data of hours studied and scores achieved. Next, I trained a Linear Regression model using scikit-learn, which fits a simple line to predict scores based on study hours. After training, I saved the model as model.pkl using joblib, allowing the Flask app to reuse it without retraining every time it runs.

### Building the Web App

Using Flask, a lightweight Python web framework, I developed a small web application that presents a clean and intuitive form to users. They enter the number of hours they studied and submit the form. The app then loads the saved model, uses it to predict the score, and displays the result dynamically on the webpage—all without needing to refresh the site.

### Integration

The training script and the Flask app script are placed in the same project directory for simplicity. The web app loads the pre-trained model file during runtime, making the response time very fast and efficient. This separation ensures the model is trained only once unless updated data requires retraining.

## Project Structure
StudentScorePredictor
  - train_model.py
  - app.py
  - model.pkl
  - data.csv
  - templates
     - index.html     

## How to Run This Project
1.	Open the project folder in VSCode or your preferred code editor.
2.	Create and activate a Python virtual environment to manage dependencies cleanly.
3.	Install all required packages by running:
   `pip install pandas scikit-learn flask joblib`
4.	Run the training script to build and save the model:
   `python train_model.py`
5.	Launch the Flask web app:
   `python app.py`
6.	Open your browser and go to:
   `http://127.0.0.1:5000`
7.	Enter the number of hours studied and submit to see your predicted exam score instantly.

## Results

The web app provides immediate feedback by predicting scores based on the input study hours using the trained linear regression model. The simple interface is designed for ease of use, focusing solely on functionality to demonstrate how machine learning can be quickly deployed to end users. Although the model is basic, it effectively illustrates the power of data-driven predictions and how models can be served through web applications.

## Conclusion

This project highlights a complete cycle of machine learning application development: data loading, model training, model persistence, and web deployment. It shows how even a simple model like linear regression can be made interactive and accessible through a web app. This hands-on experience lays a solid foundation for building more complex predictive models and deploying them for real-world use cases.

By using Python libraries like pandas, scikit-learn, Flask, and joblib, and leveraging Visual Studio Code as a development environment, I was able to build, test, and run this project efficiently. This approach is highly scalable and can be adapted for many other ML-powered applications.

# Output
![Image](https://github.com/user-attachments/assets/acba9d07-2cc6-4fb3-8356-b9f32953fa04)



