## setup up basic flask app ##

# create three files for contents and requirements
# 	main.py
#	requirements.txt
#	app.yaml

# add version of Flask to requirements.txt (e.g.)
# Flask==1.1.2

# add python version to app.yaml (e.g.)
# runtime: python38

# activate the virtual environment for running code
# source venv/bin/activate

# install Flask while in the virtual environment 
# python3 -m pip install -r requirements.txt

# add below to main.py for content delivery
# from flask import Flask
#
# app = Flask(__name__)
# 
# @app.route("/")
# def index():
#     return "Congratulations, it's a web app!"
#
# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=8080, debug=True)


