from flask import Flask, render_template, jsonify

app = Flask(__name__)

POSTS = [{
    "Id": 1,
    "Title": "My first post",
    "Body": "This is my first post",
    "Slug": "my-first-post"
}, {
    "Id": 2,
    "Title": "My second post",
    "Body": "This is my second post",
    "Slug": "my-second-post"
}]


@app.route('/')
def Index():
  return render_template("home.html", posts=POSTS)


@app.route('/api/posts')
def list_jobs():
  return jsonify(POSTS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
