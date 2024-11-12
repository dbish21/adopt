from flask import Flask, render_template, redirect, url_for, flash
from models import db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5433/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret123"

# Initialize Flask extensions
db.init_app(app)

# Create tables within application context
def init_db():
    with app.app_context():
        db.create_all()

@app.route('/')
def home():
    """Show homepage with list of pets."""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Show add pet form and handle form submission."""
    form = AddPetForm()

    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            notes=form.notes.data
        )
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added {new_pet.name}!", "success")
        return redirect(url_for('home'))

    return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Show pet edit form and handle edit."""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data == 'True'
        db.session.commit()
        flash(f"Updated {pet.name}!", "success")
        return redirect(url_for('home'))

    return render_template('pet_detail.html', form=form, pet=pet)

if __name__ == '__main__':
    init_db()  # Initialize database tables
    app.run(debug=True)