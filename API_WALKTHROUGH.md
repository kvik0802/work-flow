# 🛰️ Particle Python Host: Deep-Dive API Walkthrough

This document provides a comprehensive technical breakdown of the **Particle Python Host** project, covering the Flask Backend API and the WebGL-powered Frontend Engine.

---

## 🐍 1. Backend Architecture (Flask)

The backend is built using **Flask**, a lightweight Python web framework. It serves two primary roles: hosting the static interactive experience and providing a RESTful API for system configuration.

### Core API Endpoints

#### `GET /api/metadata`
Returns high-level project information. This is used by the client to display project versioning and authorship.
- **Response Structure**:
  ```json
  {
    "name": "Particle Orb — Deep Space",
    "version": "1.2.0",
    "author": "VICKY",
    "particle_count": 80000
  }
  ```

#### `GET /api/shapes`
Provides a dynamic list of morph targets supported by the engine. This allows the UI to generate buttons or hints automatically.
- **Response**: A list of objects containing `id`, `label`, and `icon`.

#### `GET/POST /api/settings`
Allows retrieval and real-time updates of the particle engine's physical parameters.
- **Fields**: `bloom_strength`, `bloom_radius`, `trail_persistence`, `interaction_strength`.
- **Usage**: You can remotely trigger visual changes by sending a POST request to this endpoint.

---

## 💠 2. Frontend Engine (WebGL/Three.js)

The "Heart" of the project is the `index.html` (formerly `particle-morphing.html`). It uses a custom **GPGPU-style** particle system.

### Particle Morphing Logic (The "Magic")
Unlike standard animation, which moves objects, this engine interpolates between **80,000 sets of coordinates** on every frame.

1.  **Attribute Buffers**: We store `aStart` (current position) and `aEnd` (target position) for every single particle as attributes in GPU memory.
2.  **Shader Interpolation**: The Vertex Shader uses a `uProgress` uniform and a custom easing function (`eio`) to mix these positions:
    ```glsl
    float p = eio(clamp((uProgress - delay) / (1.0 - delay), 0.0, 1.0));
    vec3 pos = mix(aStart, aEnd, p);
    ```
3.  **Organic Turbulence**: To prevent the morph from looking "robotic," we add **Simplex Noise** turbulence during the transition, creating an arc-like, fluid motion.

### Post-Processing Pipeline
To achieve the "Premium" look, the engine uses a multi-pass composer:
- **RenderPass**: Captures the base scene.
- **UnrealBloomPass**: Creates the high-fidelity glow by isolating bright pixels and blurring them.
- **AfterimagePass**: Implements "Motion Persistence," allowing particles to leave faint ghost trails as they move.

---

## 🛠️ 3. Performance & Optimization

- **Draw Calls**: The entire 80,000 particle system is rendered in **exactly 1 draw call** using `THREE.Points`.
- **Memory**: Attributes are passed as `Float32Array`, which is the most memory-efficient way to handle large datasets in JavaScript.
- **Auto-LOD**: If the user's hardware struggles (FPS < 30), the engine automatically drops the pixel ratio and disables motion trails to preserve responsiveness.

---

## 📈 4. Integration Example

You can interact with the API from the browser console to see it in action:

```javascript
// Fetch all available shapes from the Python API
fetch('/api/shapes')
  .then(res => res.json())
  .then(shapes => console.log("Available Morph Targets:", shapes));

// Update the bloom strength remotely
fetch('/api/settings', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ bloom_strength: 1.5 })
});
```

---
*Created by VICKY for the Particle-Python Project.*
