# Artévia – Fashion E-Commerce Website

> Fashion that moves with you. A modern, premium static website served via Nginx in Docker.

---

## Project Structure

```
website/
├── src/                        # All source files
│   ├── index.html              # Main HTML entry point
│   └── assets/
│       ├── css/
│       │   └── style.css       # Global styles & design system
│       ├── js/
│       │   └── script.js       # Interactions, animations, cart logic
│       └── images/             # All product & editorial images
│           ├── hero_model.png
│           ├── men_category.png
│           ├── women_category.png
│           ├── kids_category.png
│           ├── new_vibes_model.png
│           ├── product1.png
│           ├── product2.png
│           ├── product3.png
│           └── product4.png
├── nginx/
│   └── nginx.conf              # Nginx: gzip, caching, SPA fallback, security headers
├── Dockerfile                  # nginx:alpine image definition
├── docker-compose.yml          # One-command local deployment
├── .dockerignore               # Files excluded from Docker build context
└── README.md                   # This file
```

---

## Prerequisites

| Tool          | Version    | Install                        |
|---------------|------------|--------------------------------|
| Docker        | 24+        | https://docs.docker.com/get-docker/ |
| Docker Compose| v2 (plugin)| Included with Docker Desktop   |

---

## Getting Started

### 1. Clone / Navigate to the project

```bash
cd /path/to/website
```

### 2. Build & Run

```bash
docker compose up --build
```

The site will be available at: **http://localhost:8080**

### 3. Run in Detached Mode (background)

```bash
docker compose up --build -d
```

### 4. View Logs

```bash
docker compose logs -f
```

### 5. Stop

```bash
docker compose down
```

### 6. Rebuild After Changes

```bash
docker compose up --build --force-recreate
```

---

## Nginx Configuration Highlights

| Feature              | Detail                                          |
|----------------------|-------------------------------------------------|
| **Gzip**             | Enabled for HTML, CSS, JS, JSON, SVG            |
| **HTML caching**     | `no-cache` – always fetches latest              |
| **CSS/JS caching**   | `max-age=7d` (1 week)                           |
| **Image caching**    | `max-age=1y` (1 year, immutable)                |
| **Security headers** | X-Frame-Options, X-XSS-Protection, nosniff      |
| **SPA fallback**     | All routes resolve to `index.html`              |

---

## Docker Image Details

| Property     | Value           |
|--------------|-----------------|
| Base image   | `nginx:alpine`  |
| Final size   | ~25–30 MB       |
| Exposed port | `80` (internal) |
| Host port    | `8080`          |

---

## Development (without Docker)

This is a Node.js Express application. To run it locally:

1. Install dependencies:
```bash
npm install
```

2. Start the server:
```bash
node app.js
```

Then visit: **http://localhost:3000**

---

## Tech Stack

- **HTML5** – Semantic markup
- **Vanilla CSS** – Custom design system (no frameworks)
- **Vanilla JS** – Interactions & animations
- **Nginx Alpine** – Production-grade static file server
- **Docker** – Containerized, reproducible environment

---

&copy; 2024 Artévia. All rights reserved.
