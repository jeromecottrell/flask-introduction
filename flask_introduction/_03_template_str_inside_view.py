from flask import Flask
from flask import render_template_string  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    library_name = "ISA"
    html = """
        <html>
            <h1>Welcome to {{library_name}} library!</h1>
            <ul>
                {% for author in authors %}
                <li>{{ author }}</li>
                {% endfor %}
            </ul>
        </html>
    """
    authors_list = ["Alan Poe", "Jorge L. Borges", "Mark Twain", "Stephen King"]

    rendered_html = render_template_string(
        html, library_name=library_name, authors=authors_list
        )
    # Using an <ul> tag add the authors using the template engine
    return rendered_html

