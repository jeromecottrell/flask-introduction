from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    html = """
        <html>
            <h1>Welcome to our Library!</h1>
            {authors_html}
        </html>
    """
    authors = ["Alan Poe", "Jorge L. Borges", "Mark Twain", "Stephen King"]
    authors_list = "<ul>"
    authors_list += "\n".join([
        "<li>{}</li>".format(author) for author in authors
    ])
    authors_list += "<ul>"

    return html.format(authors_html=authors_list)
