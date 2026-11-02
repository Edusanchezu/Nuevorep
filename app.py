from flask import Flask, render_template, request

app = Flask(__name__)

historial = []

@app.route("/", methods=["GET", "POST"])
def calculadora():

    resultado = ""

    if request.method == "POST":

        expresion = request.form.get("expresion", "")

        try:
            resultado = eval(expresion)
            historial.append(f"{expresion} = {resultado}")

        except:
            resultado = "Error"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Calculadora con Historial</title>

        <style>
            body {{
                font-family: Arial;
                max-width: 600px;
                margin: 40px auto;
                padding: 20px;
                background: #f5f5f5;
            }}

            h1 {{
                text-align: center;
            }}

            input {{
                width: 100%;
                padding: 12px;
                font-size: 20px;
                margin-bottom: 10px;
                box-sizing: border-box;
            }}

            button {{
                width: 100%;
                padding: 12px;
                font-size: 18px;
                background: #0078D7;
                color: white;
                border: none;
                cursor: pointer;
            }}

            button:hover {{
                background: #005ea6;
            }}

            .resultado {{
                margin-top: 20px;
                padding: 10px;
                background: white;
                border-radius: 5px;
            }}

            .historial {{
                margin-top: 20px;
                background: white;
                padding: 15px;
                border-radius: 5px;
            }}

            li {{
                margin-bottom: 5px;
            }}
        </style>

    </head>

    <body>

        <h1>Calculadora con Historial</h1>

        <form method="POST">

            <input
                type="text"
                name="expresion"
                placeholder="Ejemplo: 5+3*2"
                required
            >

            <button type="submit">
                Calcular
            </button>

        </form>

        <div class="resultado">

            <h3>Resultado:</h3>

            <p>{resultado}</p>

        </div>

        <div class="historial">

            <h3>Historial</h3>

            <ul>
                {"".join([f"<li>{item}</li>" for item in historial])}
            </ul>

        </div>

    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True)