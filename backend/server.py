from flask import Flask, send_from_directory, jsonify, request
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')

# Mock database for demonstration
PROJECT_CONFIG = {
    "name": "Particle Orb — Deep Space",
    "version": "1.2.0",
    "author": "Naini Vivekanand",
    "particle_count": 150000,
    "theme": "nebula",
    "settings": {
        "bloom_strength": 0.45,
        "bloom_radius": 0.9,
        "trail_persistence": 0.92,
        "interaction_strength": -0.5
    }
}

MORPH_SHAPES = [
    {"id": "love", "label": "Heart", "icon": "❤️"},
    {"id": "cube", "label": "Cube", "icon": "🧊"},
    {"id": "star", "label": "Star", "icon": "⭐"},
    {"id": "circle", "label": "Sphere", "icon": "🔵"},
    {"id": "flower", "label": "Flower", "icon": "🌸"}
]

# --- Frontend Routes ---

@app.route('/')
def index():
    """Serve the main particle system experience."""
    return app.send_static_file('index.html')

# --- API Routes ---

@app.route('/api/metadata', methods=['GET'])
def get_metadata():
    """Return project information and current configuration."""
    return jsonify(PROJECT_CONFIG)

@app.route('/api/shapes', methods=['GET'])
def get_shapes():
    """Return the list of available morph targets."""
    return jsonify(MORPH_SHAPES)

@app.route('/api/settings', methods=['GET', 'POST'])
def handle_settings():
    """Get or update particle system settings."""
    if request.method == 'POST':
        new_settings = request.json
        PROJECT_CONFIG['settings'].update(new_settings)
        return jsonify({"status": "success", "message": "Settings updated", "current": PROJECT_CONFIG['settings']})
    
    return jsonify(PROJECT_CONFIG['settings'])

if __name__ == '__main__':
    print("--- Particle Morphing Server is running! ---")
    print("URL: http://localhost:5001")
    print("API Endpoints available at /api/metadata, /api/shapes, /api/settings")
    app.run(host='0.0.0.0', port=5001, debug=True)
