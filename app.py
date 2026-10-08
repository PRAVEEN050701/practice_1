from flask import Flask
app = Flask (__name__)
@app.route("/")
def home():
    return("API is running")
@app.route("/health")
def health():
    return("health ok")
@app.route("/products")
def product():
    return("list of products")
if __name__ == "__main__":
 app.run(host="0.0.0.0",port="8080")