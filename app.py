import requests
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/posts')
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return "Hello World-----Posts"
@app.route('/comments')
def get_comments():
    url = "https://jsonplaceholder.typicode.com/comments"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return "Hello Comments"
@app.route('/albums')
def get_albums():
    url = "https://jsonplaceholder.typicode.com/albums"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return "Hello Albums"
if __name__ == '__main__':
    app.run(debug=True)
