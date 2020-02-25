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
	# Get the Assembly from the request body
	assembly = request.json

	uploads = []

	# Store all thumbnails that were generated
	for result in assembly['results']['thumbnail']:
		original_name = result['original_name']
		original_ext = os.path.splitext(original_name)[1]

		upload = {
			'original_name': result['original_name'],
			'file_id':       result['original_id'] + original_ext,
			'thumbnail_id':  result['id'] + '.' + result['ext']
		}

		download_file(result['ssl_url'], 'static/thumbnails/' + upload['thumbnail_id'])
		uploads.append(upload)

	# Store all files which have been uploaded
	for file in assembly['uploads']:
		download_file(file['ssl_url'], 'static/files/' + file['id'] + '.' + file['ext'])

	# Save the new entities in the "database"
	model.add_uploads(uploads)

	return jsonify({'ok': True})

# Helper function for downloading a file from an URL
def download_file(url, destination):
	urllib.request.urlretrieve(url, destination)
