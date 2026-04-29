# Technical Skills & Packages Breakdown

This document provides a comprehensive list of the technologies, libraries, and technical skill sets employed in the development of the **Particle Orb — Deep Space** project.

## 🛠️ Software Packages & Libraries

### Backend (Python)
- **[Flask](https://flask.palletsprojects.com/)**: A lightweight WSGI web application framework used to serve the frontend and handle REST API requests for project metadata and settings.

### Frontend (JavaScript/WebGL)
- **[Three.js](https://threejs.org/)**: The primary 3D engine used for rendering the high-density particle system, managing the scene, camera, and renderer.
- **[lil-gui](https://lil-gui.georgealways.com/)**: A lightweight controller library used for the real-time visual tuning interface (Bloom, Trails, Particle Size).
- **Three.js Addons**:
    *   `OrbitControls`: Enables intuitive mouse-based camera movement (Rotate, Zoom, Pan).
    *   `EffectComposer`: Manages the post-processing pipeline.
    *   `UnrealBloomPass`: Adds the cinematic "nebula" glow effect.
    *   `AfterimagePass`: Creates smooth motion trails for moving particles.

---

## 🧠 Technical Skill Sets

### 1. Computer Graphics & Shaders
- **WebGL Programming**: Deep integration with the browser's GPU for high-performance rendering.
- **GLSL (Shader Language)**: Authoring custom **Vertex Shaders** (for particle positions, morphing logic, and twinkling) and **Fragment Shaders** (for glossy, gem-like pixel rendering).
- **Post-Processing**: Implementing cinematic visual filters like Bloom and Motion Blur.

### 2. Frontend Engineering
- **Modern JavaScript (ES6+)**: Utilizing `importmaps`, modules, and asynchronous logic.
- **Advanced CSS3**: Implementing **Glassmorphism** (backdrop-filters, semi-transparent blurs) and responsive UI layouts.
- **Canvas API**: Used for the text-to-point generation engine to convert words into 3D particle coordinates.

### 3. Backend & API Design
- **RESTful API Development**: Designing endpoints for metadata retrieval and dynamic settings updates.
- **Python Scripting**: Automating the server-side logic and environment configuration.

### 4. Applied Mathematics
- **Vector & Matrix Math**: Handling 3D transformations, rotations, and raycasting.
- **Animation Easing**: Implementing **Cubic Easing (In-Out)** for natural, smooth morphing transitions.
- **Procedural Logic**: Utilizing noise functions and stochastic logic for organic particle "breathing" and starfield generation.

### 5. DevOps & Workflow
- **Version Control (Git)**: Managing repository history, branching, and remote synchronization.
- **NPM Tooling**: Configuring custom scripts (`npm start`) to streamline the development workflow.
- **Project Architecture**: Organizing a "monorepo" style structure with separated `/backend` and `/frontend` concerns.

---
*Built by Naini Vivekanand*
