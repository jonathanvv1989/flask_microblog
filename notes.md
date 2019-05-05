# Forms - GET and POST
## HTTP protocol definition
* GET (default): return information to the client (browser)
* POST: browser submits form data to the server
In reality GET can be used to send information to the server but the URL bar
gets cluttered
## HTML template (<form> tag) attributes
1. **action**:
* URL to submit when returning form
* action="" is returning the original URL
2. **method (http request method)**:
* GET (default): add form fields to URL
* POST: form data submitted in the body of the request
3. **novalidate**
* tell browser to no apply validation on fields in the form
* optional attribute
# Forms - Validation
## wtforms.validators built-in
* on each element passed as list of functions: validators=[validator1(), etc..]
* DataRequired(), Email(), EqualTo(*field_to_check_equality*)
```python
class RegistrationForm(FlaskForm):
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField(
      'Repeat Password',
      validators=[DataRequired(), EqualTo('password')]
  )
```
## custom
* In class Form add method named as validate_*field*
```python
class MyTestForm(FlaskForm):
  testfield = StringField('Testfield')

  def validate_testfield(self, testfield):
    """for instance test if field already exist in database (username ...)"""
    ...
```
# HTML - userful tags
## span vs div
* div: used for styling block element on seperate line
* span: used for styling inline element
## Miscellaneous
* br: carriage-return
## Backend view function
1. **@app.route attribute**
* methods: list of methods accepted by end point (e.g. ['GET', 'POST'])
* Method not Allowed error: returned if browser sends method not configured
2. **form.validate_on_submit() (form is a form subclassing FlaskForm)**
* runs all the validation of the form and return True if they pass
# Forms - Using flash() (Flask function)
1. **View function**
* flash(msg_as_str) stores message
* example: if something: ... flash('my msg {}'.format(form_attr))
2. **HTML Template**
* get_flashed_messages() (returns list) to retrieve and display stored msg
* general structure: {% with messages = get_flashed_messages() %} + if + for
* {% with xx %}{% end with %}: define variable in the scope of endwith
# Database (SQLAlchemy) - 1 to many relationship
1. **Many side (model)**
* create a db.Column which is a db.ForeignKey('table.column')
* e.g.: user_id = db.Column(db.Integer, db.ForeignKey('user.id')) (Post model)
* Note we use db table name 'user'
2. **1 side (model)**
* create a db.relationship with backref
* e.g.: posts = db.relationship('Post', backref='author', lazy='dynamic')
* Note we use the model (class) name 'Post'
3. **Why do we need the backref?**
* Facilitate Foreign_Key reference when create entries in *many* table
* e.g.: Post(body='my post', author=User.query.get(1))
* *author* does not exist in *post* table but is defined in *user* as relationship
* It will automatically populate correct user_id (fk) field in *post* table
# Flask shell
1. **Why?**
* Run python session in the context of the application
* Configure a *shell context* where you pre import desired variables
2. **How?**
* In main application module (microblog.py) add *make_shell_context* function
* It should return a dict with keys = desired object names, value = object
* Decorate function with *app.shell_context_processor*
* objects can be db, models (User, Post etc...) and remember to import them at the top of the file
# User Login
## Password hashing
1. **werkzeug.security functions**
* generate hash: generate_password_hash('password')
* check password: check_password_hash(hash, 'passwordtotest')
2. **Integrate werkzeug in SA User model**
* create a set_password method populating self.password_hash (using generate_password_hash)
* create a check_password method returning boolean (using check_password_hash)
3. **Backend user creation workflow**
* create user: u = User(username='john', email='john@test.com')
* set hash (user creation): u.set_password('thepassword')
* check hash (user login): u.check_password('thepasswordtocheck')
