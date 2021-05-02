from flask import Flask, render_template, request, make_response, jsonify
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def upload_video():

  if request.method == "POST":
    file = request.files["file"]
    print("File uploaded")
    print(file)
    res = make_response(jsonify({"message": "File uploaded"}), 200)

    return res

  return render_template("index.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port='5001', debug=True)
