from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def analyze_code(code):
    if "for" in code and "for" in code.split("for", 1)[1]:
        return {
            "bottlenecks": ["Nested loops detected, consider optimizing!"],
            "suggestions": ["Use vectorized operations or algorithms with lower complexity."]
        }
    else:
        return {
            "bottlenecks": [],
            "suggestions": ["Code looks optimized."]
        }

@app.route('/')
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Code Analysis Tool</title>
    </head>
    <body>
        <h1>Welcome to the Code Analysis Tool</h1>
        <p>Use the frontend to analyze your code. Make sure the frontend connects to this server!</p>
    </body>
    </html>
    """)

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'code' not in request.form:
        return jsonify({"error": "Code not provided"}), 400

    code = request.form['code']
    result = analyze_code(code)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
