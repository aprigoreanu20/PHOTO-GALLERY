from flask import Flask, render_template, request, redirect, url_for, session, flash
from website import create_app
from PIL import Image
from website.models import Photo
from website import db
from flask_login import login_required, logout_user, current_user
import os

app = create_app()

def create_thumbnails(filename, dest_dir):
    size = (200, 200)
    img_path = os.path.join('website/static/uploads', filename)
    with Image.open(img_path) as img:
        img.thumbnail(size)
        thumbnail_path = os.path.join(dest_dir, filename)
        img.save(thumbnail_path)

UPLOAD_FOLDER = 'website/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    photos = Photo.query.all()
    return render_template("home.html", photos=photos)

@app.route('/about')
def about_me():
    return render_template("about_me.html")

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        file = request.files['photo']
        name = request.form.get('name')
        category = request.form.get('category')

        new_photo = Photo(filename=file.filename, name=name, category=category, user_id=current_user.id)
        db.session.add(new_photo)
        db.session.commit()

        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            create_thumbnails(file.filename, 'website/static/thumbnails')

        flash("Photo uploaded successfully", category='success')

    return render_template("upload.html")


@app.route('/gallery')
def gallery():
    photos = Photo.query.filter_by(user_id=current_user.id).all()
    return render_template("gallery.html", photos=photos)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)