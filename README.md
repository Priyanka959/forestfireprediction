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

Add screenshots of your application here. To add screenshots:

1. Take screenshots of your running application
2. Save them in a `screenshots/` folder in your repository
3. Add them to this README using Markdown image syntax:

   ```markdown
   ![Home Page](screenshots/homepage.png)
   ![Prediction Results](screenshots/results.png)
   ```

   Example:
   - Screenshot of the main prediction form
   - Screenshot of the risk assessment results
   - Screenshot of the impact visualization

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