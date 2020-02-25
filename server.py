from flask import Flask, escape, request, render_template, jsonify
import urllib.request
import os.path

import model

app = Flask(__name__)

# Render the index page which lists all uploads.
@app.route('/')
def index():
	uploads = model.list_uploads()
	return render_template('index.html', uploads=uploads)

# This endpoint which is invoked when the Transloadit
# Assembly has finished
@app.route('/add_uploads', methods=['POST'])
def add_uploads():
	# TODO: Add upload saving

# Helper function for downloading a file from an URL
def download_file(url, destination):
	urllib.request.urlretrieve(url, destination)
