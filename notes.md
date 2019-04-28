# Forms - GET and POST
## HTTP protocol definition
* GET (default): return information to the client (browser)
* POST: browser submits form data to the server
In reality GET can be used to send information to the server but the URL bar
gets cluttered
## HTML template (<form> tag) attributes
1. action:
* URL to submit when returning form
* action="" is returning the original URL
1. method (http request method):
* GET (default): add form fields to URL
* POST: form data submitted in the body of the request
1. novalidate
* tell browser to no apply validation on fields in the form
* optional attribute
## Backend view function
1. @app.route attribute
* methods: list of methods accepted by end point (e.g. ['GET', 'POST'])
* Method not Allowed error: returned if browser sends method not configured
1. form.validate_on_submit() (form is a form subclassing FlaskForm)
* runs all the validation of the form and return True if they pass
# Forms - Using flash() (Flask function)
1. View function
* flash(msg_as_str) stores message
* example: if something: ... flash('my msg {}'.format(form_attr))
1. HTML Template
* get_flashed_messages() (returns list) to retrieve and display stored msg
* general structure: {% with messages = get_flashed_messages() %} + if + for
* {% with xx %}{% end with %}: define variable in the scope of endwith
# Database (SQLAlchemy) - 1 to many relationship
1. Many side (model)
* create a db.Column which is a db.ForeignKey('table.column')
* e.g.: user_id = db.Column(db.Integer, db.ForeignKey('user.id')) (Post model)
* Note we use db table name 'user'
1. 1 side (model)
* create a db.relationship with backref
* e.g.: posts = db.relationship('Post', backref='author', lazy='dynamic')
* Note we use the model (class) name 'Post'
1. Why do we need the backref?
* Facilitate Foreign_Key reference when create entries in *many* table
* e.g.: Post(body='my post', author=User.query.get(1))
* *author* does not exist in *post* table but is defined in *user* as relationship
* It will automatically populate correct user_id (fk) field in *post* table
# Flask shell
1. Why?
* Run python session in the context of the application
* Configure a *shell context* where you pre import desired variables
1. How?
* In main application module (microblog.py) add *make_shell_context* function
* It should return a dict with keys = desired object names, value = object
* Decorate function with *app.shell_context_processor*
* objects can be db, models (User, Post etc...) and remember to import them at the top of the file
