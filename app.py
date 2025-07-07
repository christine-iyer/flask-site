from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    image_url0 = url_for('static', filename='botanical-gin.png')
    image_url1 = url_for('static', filename='rose-gin.jpg')
    image_url2 = url_for('static', filename='melon-gin.png')
    return f"""
    <html>
        <body>
            <h2>Hello, Flask!</h2>
            <h3>Here are some og out faves:</h3>
            <p>We love these gins:</p>
            <img src="{image_url0}" alt="Example Image" style="width: 200px; height: auto;">
            <img src="{image_url1}" alt="Example Image" style="width: 200px; height: auto;">
            <p>And my famous melon ball:</p>
            <img src="{image_url2}" alt="Example Image" style="width: 200px; height: auto;">
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)