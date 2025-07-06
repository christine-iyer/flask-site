from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    image_url = url_for('static', filename='botanical-gin.png')
    return f"""
    <html>
        <body>
            <h4>Hello, Flask!</h4>
            <img src="{image_url}" alt="Example Image" style="width: 200px; height: auto;">
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)