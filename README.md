# Particle Orb — Deep Space

A high-performance, interactive particle morphing system powered by **WebGL (Three.js)** and **Flask**. This project features a 80,000-particle engine that can dynamically transition between complex 3D shapes and custom text, all while maintaining a smooth, cinematic aesthetic.

![Particle Orb Showcase](https://raw.githubusercontent.com/vicky/particle-python/main/preview.gif) *(Note: Add a real preview image/gif here later)*

## ✨ Key Features

-   **High-Density Engine**: Renders 80,000 particles simultaneously using custom GLSL shaders.
-   **Dynamic Morphing**: Seamlessly transition between predefined shapes (Heart, Cube, Star, Sphere, Flower) or any custom text typed by the user.
-   **Cinematic Visuals**: 
    -   **Glassmorphic UI**: Sleek, transparent control panels with backdrop filters.
    -   **Post-Processing**: Unreal Bloom for that "nebula" glow and Afterimage for smooth motion trails.
    -   **Procedural Starfield**: A natural-looking cosmic background with twinkling stars.
-   **Interactive Physics**: Particles react to mouse movement with adjustable attraction/repulsion forces.
-   **Live Tuning**: Integrated GUI (`lil-gui`) to modify bloom, particle size, physics, and exposure in real-time.
-   **Flask Backend**: Serves the application and provides API endpoints for configuration and metadata.

## 🚀 Tech Stack

### Frontend
-   **[Three.js](https://threejs.org/)**: The core 3D engine for scene management and rendering.
-   **GLSL (Web Graphics Library Shading Language)**: Custom Vertex and Fragment shaders for high-performance particle animation and coloring.
-   **CSS3**: Modern styling with glassmorphism and responsive design.
-   **Vanilla JavaScript (ES6+)**: Modular code with `importmap` for dependency management.

### Backend
-   **[Python](https://www.python.org/)**: Core logic for the host server.
-   **[Flask](https://flask.palletsprojects.com/)**: A lightweight WSGI web application framework to serve the frontend and handle REST API requests.

## 📂 Project Structure

```bash
particle-python/
├── server.py           # Flask backend server
├── index.html          # Main WebGL frontend (350+ lines of optimized code)
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
└── API_WALKTHROUGH.md  # Detailed API documentation
```

## 🛠️ Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/vicky/particle-python.git
    cd particle-python
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the server**:
    ```bash
    python server.py
    ```

4.  **Open in Browser**:
    Navigate to [http://localhost:5000](http://localhost:5000) to experience the Particle Orb.

## 🕹️ Controls

-   **Morph**: Type any word in the input box and press "Morph" or "Enter".
-   **Rotate**: Left-click and drag to rotate the orb.
-   **Zoom**: Scroll to zoom in/out.
-   **Pan**: Right-click and drag to move the camera.
-   **GUI**: Use the control panel on the top-right to tweak visuals.

## 📡 API Endpoints

The Flask server provides the following endpoints:
-   `GET /api/metadata`: Returns project version and author info.
-   `GET /api/shapes`: Returns a list of supported symbolic shapes.
-   `GET /api/settings`: Returns current particle system settings.

---

Built with ❤️ by **VICKY**
