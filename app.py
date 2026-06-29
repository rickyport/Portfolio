"""Personal HomePage"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_mail import Mail, Message

load_dotenv()

app = Flask(__name__)

# Gmail SMTP config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

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

        msg = Message(
            subject=f"New Contact Form Message from {name}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[os.getenv("MAIL_RECIPIENT")],
            reply_to=email
        )

        msg.body = f"""
        Name: {name}
        Email: {email}

        Message:
        {message}
        """

        mail.send(msg)

        return "Message sent successfully!"

    return render_template("contact.html", active_page="contact")


if __name__ == "__main__":
    app.run(debug=True)
