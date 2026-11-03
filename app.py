from flask import Flask, request
import requests

app = Flask(__name__)

SUPABASE_URL = "https://unrajkbriivdyobaoara.supabase.co"

SUPABASE_KEY = "sb_publishable_Qdi3qlS_3xkGrcV16R5Mgg_uW9BRQ_p"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}


@app.route("/", methods=["GET", "POST"])
def calculadora():

    resultado = ""

    if request.method == "POST":

        nombre = request.form.get("nombre", "")
        expresion = request.form.get("expresion", "")

        try:

            resultado = str(eval(expresion))

            print("Nombre:", nombre)
            print("Resultado:", resultado)

            response = requests.post(
                f"{SUPABASE_URL}/rest/v1/Usuarios",
                headers=HEADERS,
                json={
                    "Nombre": nombre,
                    "Resultado": resultado
                }
            )

            print("STATUS:", response.status_code)
            print("RESPUESTA:", response.text)

        except Exception as e:

            resultado = f"Error: {e}"

    return f"""
    <!DOCTYPE html>
    <html>

    <head>

        <title>Calculadora Supabase</title>

        <style>

            body {{
                font-family: Arial;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
            }}

            input {{
                width: 100%;
                padding: 10px;
                margin-bottom: 10px;
            }}

            button {{
                width: 100%;
                padding: 10px;
                background: #0078d4;
                color: white;
                border: none;
            }}

        </style>

    </head>

    <body>

        <h1>Calculadora + Supabase</h1>

        <form method="POST">

            <input
                type="text"
                name="nombre"
                placeholder="Nombre"
                required
            >

            <input
                type="text"
                name="expresion"
                placeholder="5+5"
                required
            >

            <button type="submit">
                Calcular y Guardar
            </button>

        </form>

        <h2>Resultado:</h2>

        <p>{resultado}</p>

    </body>

    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)