from flask import render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import os
from app import app, db, mail
from app.forms import PropertyForm, ContactForm
from app.models import Property
from flask_mail import Message

@app.route('/')
def home():
    """Render the website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Josiah-John Green")

@app.route('/properties')
def properties():
    """Render the website's property listing page."""
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/create', methods=['GET', 'POST'])
def create():
    """Render the property creation page and handle form submission."""
    form = PropertyForm()

    if form.validate_on_submit():
        try:
            photo = form.photo.data
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            property = Property(
                title=form.title.data,
                description=form.description.data,
                bedrooms=form.bedrooms.data,
                bathrooms=form.bathrooms.data,
                price=form.price.data,
                type=form.type.data,
                location=form.location.data,
                photo=filename
            )
            db.session.add(property)
            db.session.commit()
            
            flash('Property added successfully!', 'success')
            return redirect(url_for('properties'))
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(f"An error occurred: {str(e)}", 'danger')

    return render_template('create.html', form=form)

@app.route('/uploads/<filename>')
def photo(filename):
    """Serve uploaded photos."""
    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

@app.route('/properties/<int:propertyid>')
def view(propertyid):
    """Render the page for a specific property."""
    property = Property.query.get_or_404(propertyid)
    return render_template('view.html', property=property, propertyid=propertyid)

@app.route('/email/<int:propertyid>', methods=['GET', 'POST'])
def email(propertyid):
    """Process and send email."""
    form = ContactForm()
    property = Property.query.get_or_404(propertyid)

    if form.validate_on_submit():
        try:
            name = form.name.data
            email = form.email.data
            subject = form.subject.data
            message = form.message.data

            msg = Message(subject, sender=(name, email), recipients=["recipient@example.com"])
            msg.body = f"From: {name}\nEmail: {email}\nSubject: {subject}\n\n{message}"
            mail.send(msg)

            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('properties'))
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'danger')

    return render_template('email.html', form=form, property=property)