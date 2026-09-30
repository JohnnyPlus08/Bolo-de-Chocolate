from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Dados da receita que serão enviados para o HTML
    receita = {
        "titulo": "Bolo de Cenoura Fofinho com Cobertura de Chocolate",
        "tempo_preparo": "40 min",
        "rendimento": "12 porções",
        "ingredientes_massa": [
            "3 cenouras médias raladas",
            "4 ovos",
            "1 xícara de óleo de soja",
            "2 xícaras de açúcar",
            "2 xícaras de farinha de trigo",
            "1 colher de sopa de fermento em pó"
        ],
        "ingredientes_cobertura": [
            "1 colher de sopa de manteiga",
            "3 colheres de sopa de chocolate em pó",
            "1 xícara de açúcar",
            "1 xícara de leite"
        ],
        "modo_preparo_massa": [
            "No liquidificador, bata as cenouras, os ovos e o óleo até ficar homogêneo.",
            "Despeje a mistura em uma tigela e adicione o açúcar e a farinha de trigo peneirada.",
            "Misture bem até a massa ficar lisa e, por último, adicione o fermento mexendo delicadamente.",
            "Asse em forno preaquecido a 180°C por cerca de 40 minutos."
        ],
        "modo_preparo_cobertura": [
            "Despeje em uma panela a manteiga, o chocolate em pó, o açúcar e o leite.",
            "Leve ao fogo médio e mexa até levantar fervura e engrossar levemente.",
            "Despeje a cobertura ainda quente sobre o bolo já assado."
        ]
    }
    return render_template('index.html', receita=receita)

if __name__ == '__main__':
    app.run(debug=True)
