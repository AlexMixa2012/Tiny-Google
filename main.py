from flask import Flask
import random

facts_list = ["Интересный факт: Раньше русский язык был другим! Его писали по другому.  В 1918 году провели реформу и русский язык стал нормальным",
              "Интересный факт: Крупные компании любят Python",
              "Интересный факт: Питон просто изучать Язык, Python относительно легко освоить — потому его предпочитают начинающие программисты и школьники. Никакого сложного синтаксиса — изучение основ займет 2–3 месяца."]

coins = ["Орёл", "Решка"]

app = Flask(__name__)

@app.route("/")
def main():
    return f'<h1>TINY GOOGLE</h1> <a href="/random_fact">Посмотреть случайный факт!</a>, <a href="/coin">Брось монетку</a>'

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/coin")
def coin_toss():
    return f'<h2>{random.choice(coins)}</h2>'

app.run(debug=True)
