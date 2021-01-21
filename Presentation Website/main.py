from flask import Flask, render_template, request
from flask_mail import Mail, Message

# The webpages are http://127.0.0.1:5000/Home and http://127.0.0.1:5000/Contact

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465

default_email = "any_gmail_dummy@gmail.com"
default_password = "dummy_gmail_password"
app.config['MAIL_USERNAME'] = default_email
app.config['MAIL_PASSWORD'] = default_password

app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/Home')
def home():
    meta = {"title": "Home"}
    meta.update({"icon": "https://static.thenounproject.com/png/2048828-200.png"})
    contact_data = {"name": "Chelcea Claudiu", "post": "Computer Science & Engineering Student",
                    "gmail": "chelceaclaudiumarian@gmail.com", "number": "(+40) 763 665 892",
                    "description": "Results-oriented Computer Science & Engineering student and Research and \
                     Development \
                specialist at Business Organization for Students, aiming to improve and leverage my skills to \
                 successfully fill a Software Engineer Intern position. Frequently praised as innovative and \
                  hard-working by my peers, I can be relied upon to bring a real contribution to the development of the\
                   company."}
    projects = {"name": "Projects", "title1": "PHOTO EDITOR",
                "desc1": "-I created a photo editing program in C that performs a set of operations on an image \
                formatted as PPM or PGM.",
                "desc111":
                    "-The user can give as input a series of commands that can be executed \
                    on the image: apply filters, rotate, crop, select and work with only\
                    parts of the image.", "title2": "PROJECT PRESENTATION WEBSITE",
                "desc2": "-I built a presentation website for the logical design course final project from the faculty,\
                 implementing the server side using Python and Flask and the site pages using HTML & CSS and \
                 Bootstrap.",
                "desc222": "-The website also features a contact form that sends an email with the completed input.",
                "title3": "GRIDDLERS CHECKER",
                "desc3": "I created an algorithm in C language that checks if the solution submitted by the user \
                for the griddlers puzzle is correct, analyzing with gdb and valgrind any possible memory leaks."}
    skills = {"title": "Skills", "pl": "Programming languages", "a": "C", "b": "C++", "c": "HTML & CSS",
              "tech": "Technologies / tools", "tech1": "Linux", "tech2": "Ubuntu", "tech3": "Microsoft Office",
              "lang": "Languages", "lang1": "Romanian (native)", "lang2": "English"}
    extra = {"1": "Extracurricular Activities", "2": "National Strategy for Community Action", "3": "2016 – 2017",
             "4": "My responsabilities:", "5": "-Collecting books and school supplies for children",
             "6": "-Making greeting cards", "7": "-Participation in ecological activities", "8": "Hope Foundation",
             "9": "Jan 2018 – Jun 2018", "10": "About:",
             "11": "-Promoting social inclusion and combating poverty, as well as any form of discrimination.",
             "12": "-Strengthening the capacity of social economy enterprises \
     to operate in a self-sustainable manner.", "13": "Dambovita rural tourism association",
             "14": "Nov 2018 – Feb 2019"}
    extra2 = {"1": "Business Organization for Students", "2": " Research and Development Specialist",
              "3": "Nov 2020 - current ", "4": "Responsibilities: ", "5": "-Conduct research and find new opportunities\
               for expanding \
the visibility of the organization. ", "6": " -Improve communication and collaboration between all \
departments.", "7": " -Find innovative ideas for new projects and develop the ongoing ones. ", "8": "", "9": " "}
    edu = {"1": "Education ", "2": "University Politehnica Of Bucharest ", "3": " Faculty Of Automatic \
Control And Computer Science",
           "4": " Relevant coursework: Computer programming, Introduction in Informatics, Data Structures, Numerical\
            methods, Logical Design, Usage of Operating Systems",
           "5": " 2020-2024", "6": "National College Ienachita Vacarescu ", "7": " Mathematics And \
Computer Science", "8": " 2016-2020", "9": " "}
    return render_template("Home.html", title=meta, contact=contact_data, projects=projects, skills=skills,
                           extra=extra, extra2=extra2, edu=edu)


@app.route('/Contact', methods=['GET', 'POST'])
def contact():
    meta = {"title": "Contact page"}
    meta.update({"icon": "https://i.pinimg.com/originals/bb/18/bd/bb18bdbbef437b2d50518db5a8292c94.png"})
    reason = ["Other", "Project", "Job offer"]
    return render_template("Contact.html", title=meta, reasons=reason)


@app.route('/ThankYou', methods=["POST"])
def thankyou():
    meta = {"title": "Thank you"}
    meta.update({"icon": "https://img.freepik.com/free-icon/present-box-with-big-bow_318-9536.jpg?size=338&ext=jpg"})
    name = request.form.get("name")
    email = request.form.get("email")
    reason = ["Other", "Project", "Job offer"]
    message = request.form.get("message")
    company = request.form.get("company")
    phone = request.form.get("phone")
    meta.update({"name": name})
    meta.update({"email": email})
    meta.update({"message": message})
    meta.update({"company": company})
    meta.update({"phone": phone})

    if not name or not email or not message or not phone or not company:
        meta["title"] = "Error"
        meta["icon"] = "https://www.freeiconspng.com/thumbs/error-icon/error-icon-3.png"
        return render_template("Error.html", title=meta, reasons=reason)

    meta["title"] = "Thank you"
    meta["icon"] = "https://img.freepik.com/free-icon/present-box-with-big-bow_318-9536.jpg?size=338&ext=jpg"
    reason = request.form.get("reason")

    # Configurati un gmail la linia 15 pentru default_email
    msg = Message('Form submission', sender=default_email, recipients=['claudiuchelcea01@gmail.com'])

    msg.body = "Name: " + name + "\n" + "Company: " + company + "\nEmail: " + email + "\nPhone number: " + \
               phone + "\n\nContact reason: " + reason + "\nMessage: " + message
    mail.send(msg)

    return render_template("ThankYou.html", title=meta, reasons=reason)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)
