# Wildfire Risk Intelligence

Advanced predictive analytics for wildfire risk assessment and prevention using machine learning and environmental data.

## Features

- **Environmental Risk Assessment**: Analyze weather conditions, fire weather indices, and time parameters
- **AI-Powered Predictions**: Machine learning models trained on historical wildfire data
- **Real-time Analysis**: Get fire probability and potential burned area predictions
- **Interactive Visualizations**: Plotly-powered graphs for impact visualization
- **Web Interface**: User-friendly Flask-based web application

## Technologies Used

- **Backend**: Python Flask
- **Machine Learning**: TensorFlow/Keras, Scikit-learn
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Priyanka959/forestfireprediction.git
   cd forestfireprediction
   ```

2. Install dependencies:
   ```bash
   pip install flask pandas numpy tensorflow scikit-learn plotly
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Fill in the environmental parameters:
   - Weather conditions (temperature, humidity, wind speed, rainfall)
   - Fire weather indices (FFMC, DMC, DC, ISI)
   - Time parameters (month, day of week)

2. Click "Analyze Fire Risk" to get predictions

3. View results including:
   - Fire probability percentage
   - Risk level assessment
   - Potential burned area
   - Interactive visualizations

## Screenshots

<img width="940" height="1268" alt="image" src="https://github.com/user-attachments/assets/070ead42-75d8-40b4-b31b-92c1418133a5" />
<img width="940" height="1161" alt="image" src="https://github.com/user-attachments/assets/ac5f6be4-fa24-4c9d-a967-3d7f38b08e4e" />


## Model Information

The application uses two trained models:
- **Classification Model**: Predicts fire occurrence probability
- **Regression Model**: Predicts burned area (log-transformed)

Models are trained on historical wildfire data and environmental factors.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions or feedback, please open an issue on GitHub.
