from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def start():
    title = "The mission"
    
    text = """It is a late boring evening. Suddenly you get a call from an unknown person asking you whether you'd take part
    in a secret space mission. Departure this night."""

    choices = [
        ('hell_yes',"Hell yes"),
        ('hell_no',"Hell no")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices)



@app.route("/youarein")
def hell_yes():
    title = "You just said yes..."
    
    text = """... to the biggest (and possiby last) adventure of your life.The news is too big to 
    keep it to yourself. However, you don't really have time to inform anyone now."""

    choices = [
        ('callyourmom',"Call your mom"),
        ('adios',"Leave this planet. Laugh at everyone's surprised face, when they find out where you are ")
    ]
    
    
    return render_template('hellyes.html', title=title, text=text, choices=choices, )

@app.route("/youareout")
def hell_no():
    title = "You are out!"
    
    text = """You continue with your boring life. """

    choices = []

    return render_template('hellno.html', title=title, text=text, choices=choices)



@app.route("/mom")
def callyourmom():
    title = "Calling your mom"
    
    text = """She is concerned about your late night call and tells you to 
    grow up and play less games. Once she understands you are serious, she breaks into tears. You are unable to leave her here"""

    choices = []

    return render_template('mom.html', title=title, text=text, choices=choices)

@app.route("/byeearth")
def adios():
    title = "You are out of this world!"
    
    text = """Literally. Well done, enjoy the space radiation. Say hello to SpaceX's starman"""

    choices = []

    return render_template('adios.html', title=title, text=text, choices=choices)