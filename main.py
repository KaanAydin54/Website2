from flask import Flask
import random
app = Flask(__name__)

bilgiler = ["Teknolojik bağımlılıktan mustarip olan çoğu kişi, kendilerini şebeke kapsama alanı dışında bulduklarında veya cihazlarını kullanamadıkları zaman yoğun stres yaşarlar.","2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası kendilerini akıllı telefonlarına bağımlı olarak görüyor."] 
bilmeceler = [""]

@app.route("/")
def ana_sayfa():
    return "<p>İlk Sayfam</p>"


@app.route("/rasgele bilgi")
def hello_word():
    bilgi = random.choice(bilgiler)
    return f"<p>{bilgi}"

@app.route("/Boş bir sayfa")
def hello_earth():
    return f"<h2> Yazacak Birşey Bulamadım<h2>"
app.run(debug=True)
