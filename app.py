import os
import logging
from flask import Flask, render_template

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

@app.route('/')
def index():
    """Render the main page of the Love Calculator application."""
    return render_template('index.html')

# Additional routes can be added here if needed for future extensions
