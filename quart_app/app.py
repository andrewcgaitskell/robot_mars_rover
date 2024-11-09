import random
import asyncio
from quart import Quart, render_template, jsonify
from quart_app.blueprints.line_following import line_following_bp

app = Quart(__name__, templates_folder="templates")

# Register the sensor blueprint
app.register_blueprint(line_following_bp, url_prefix='/line')

# Endpoint to provide random data
@app.route('/data')
async def data():
    # Generate random data
    random_value = random.randint(0, 100)
    return jsonify({"value": random_value})

# Main route to render the Jinja2 template
@app.route('/')
async def index():
    return await render_template('index.html')

# Run the Quart app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
