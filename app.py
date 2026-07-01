"""Personal HomePage"""
import os
from flask import Flask, render_template, request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def send_email(name, email, message):
    sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))

    msg = Mail(
        from_email=os.environ.get("MAIL_FROM"),
        to_emails=os.environ.get("MAIL_FROM"),
        subject=f"New Contact Form Message from {name}",
        plain_text_content=f"""
Name: {name}
Email: {email}

Message:
{message}
"""
    )

    response = sg.send(msg)
    return response.status_code

@app.route("/")
def home():
    """Render the home page."""
    return render_template("home.html", active_page="home")

@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html", active_page="about")

@app.route("/resume")
def resume():
    """Render the reume page."""
    return render_template("resume.html", active_page="resume")


# START - Study Material
@app.route("/study")
def study():
    """Render the study page."""
    return render_template("study/index.html", active_page="study")

@app.route("/study/design-patterns")
def design_patterns():
    """Render the study/design-patterns page."""
    return render_template("study/design-patterns.html", active_page="study")

@app.route("/study/python")
def python_notes():
    """Render the study/python page."""
    return render_template("study/python.html", active_page="study")

@app.route("/study/flask")
def flask_notes():
    """Render the study/flask page."""
    return render_template("study/flask.html", active_page="study")

@app.route("/study/sql")
def sql_notes():
    """Render the study/sql page."""
    return render_template("study/sql.html", active_page="study")
# END - Study Material

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Render the contact page."""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        send_email(name, email, message)
        return "Message sent successfully!"

    return render_template("contact.html", active_page="contact")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
