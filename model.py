import shelve

FILENAME = "upload_data"

def add_uploads(new_uploads):
	with shelve.open(FILENAME) as db:
		uploads = db.get('uploads', [])
		uploads.extend(new_uploads)
		db['uploads'] = uploads

def list_uploads():
	with shelve.open(FILENAME) as db:
		uploads = db.get('uploads', [])
		return uploads
