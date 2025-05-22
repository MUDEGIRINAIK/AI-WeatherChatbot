from flask import Flask, render_template, request, jsonify # type: ignore
from weather import get_weather  # Ensure this function exists

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')  # Ensure 'index.html' is inside 'templates' folder

# API Route to get weather data
@app.route('/get_weather', methods=['POST'])
def fetch_weather():
    try:
        # Try fetching 'city' from form data or JSON
        city = request.form.get('city') or request.json.get('city')
        
        if not city:
            return jsonify({"error": "City name is missing"}), 400  # Handle missing input
        
        weather_data = get_weather(city)  # Call your function to get weather data
        return jsonify(weather_data)  # Return JSON response

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle any errors

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
