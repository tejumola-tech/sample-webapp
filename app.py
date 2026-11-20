from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Azure Web App Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f0f6ff;
                text-align: center;
                padding: 100px 20px;
            }
            h1 { color: #0078d4; }
            p { font-size: 20px; }
            .card {
                background: white;
                padding: 40px;
                border-radius: 12px;
                max-width: 650px;
                margin: auto;
                box-shadow: 0 4px 15px #ddd;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Welcome to My Azure Web App!</h1>
            <p>My first Docker container deployment.</p>
            <p>Deployed using GitHub, Docker and Azure.</p>
            <h3>Application Status: Running</h3>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)