from flask import Flask, render_template
import datetime

app = Flask(__name__)

jokes = [
    'What do you call an old snowman? Water.',
    'How did the reindeer learn to play piano? He was elf-taught.',
    'How much did Santa pay for his sleigh? Nothing, it was on the house!',
    'I got a Christmas card full of rice in the post today. I think it was from my Uncle Ben.',
    "What is Santa's favourite kind of pizza? One that is deep-pan, crisp and even.",
    'How does Santa keep his suits wrinkle free? He hangs them in the Claus-et.',
    'What do you call Frosty the Snowman on a sunny day? A puddle.',
    'How does Santa deliver presents during a thunderstorm? With raindeer!',
    'Why did the Christmas tree go to the barber? Because it needed a trim.',
    'What do elves learn in school? The elf-abet.',
    'Why did the turkey join the band? Because it had the drumsticks!',
    'What do you call a cat in the desert? Sandy Claws!',
    "Who is Santa's favorite singer? Elf-is Presley!",
    "What's Santa's favorite type of music? Wrap!",
    'What do you call a bankrupt Santa? Saint Nickel-less!',
    'How does Santa keep track of all the chimneys he has been down? He uses a log book!',
    'What do elves eat for breakfast? Frosted Flakes or Ice Crispies!',
    'What do you call Santa when he stops moving? Santa Pause!',
    'What do elves post on Social Media? Elf-ies!',
    'What do snowmen wear on their heads? Ice caps!',
    'How does a snowman get to work? By icicle!',
    'What do snowmen like to do on the weekend? Chill!',
    "Why are Christmas Trees so fond of the past? Because the present's beneath them!",
    'Who hides in the bakery at Christmas? A mince spy!',
    'What happened to the man who stole an Advent Calendar? He got 25 days!'
]

current_day = datetime.datetime.now().day
joke_for_today = jokes[current_day - 1] if 1 <= current_day <= 25 else "No joke for today!"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', joke_for_today=joke_for_today, current_day=current_day)

@app.route("/one")
def one():
    return render_template('one.html', title='Day One' )

if __name__ == '__main__':
    app.run(debug=True)
