from flask import Flask, request
import requests

app = Flask(__name__)

import os

SUPABASE_URL = os.getenv("SUPABASE_URL")

SUPABASE_KEY = os.getenv("SUPABASE_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}


@app.route("/", methods=["GET", "POST"])
def calculadora():
#CONEXION CON LA BD
    resultado = ""

    if request.method == "POST":

        nombre = request.form.get("nombre", "").strip()

        if len(nombre) > 50:
            nombre = nombre[:50]
        
        expresion = request.form.get("expresion", "")
#BACKEND DE LA CALCULADORA
        try:

            from simpleeval import simple_eval

            resultado = str(simple_eval(expresion))
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
#ESTRUCTURA DE LA CALCULADORA
    return f"""
<!DOCTYPE html>
<html>

<head>
    <title>Calculadora Supabase</title>

    <style>

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Arial, sans-serif;
        }}

        body {{
            background: linear-gradient(135deg, #0f172a, #1e293b);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }}

        .container {{
            width: 420px;
            background: white;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 15px 40px rgba(0,0,0,.3);
        }}

        h1 {{
            text-align: center;
            color: #0f172a;
            margin-bottom: 20px;
        }}

        input[type=text] {{
            width: 100%;
            padding: 12px;
            margin-bottom: 12px;
            border: 2px solid #e2e8f0;
            border-radius: 10px;
            font-size: 16px;
        }}

        .display {{
            width: 100%;
            padding: 18px;
            font-size: 24px;
            text-align: right;
            border: none;
            background: #f1f5f9;
            border-radius: 10px;
            margin-bottom: 15px;
        }}

        .buttons {{
            display: grid;
            grid-template-columns: repeat(4,1fr);
            gap: 10px;
        }}

        button {{
            border: none;
            border-radius: 10px;
            padding: 18px;
            font-size: 20px;
            cursor: pointer;
            transition: .2s;
        }}

        button:hover {{
            transform: scale(1.05);
        }}

        .num {{
            background: #e2e8f0;
            color: #0f172a;
        }}

        .op {{
            background: #2563eb;
            color: white;
        }}

        .clear {{
            background: #ef4444;
            color: white;
        }}

        .save {{
            background: #10b981;
            color: white;
            margin-top: 15px;
            width: 100%;
            font-weight: bold;
        }}

        .resultado {{
            margin-top: 20px;
            background: #f8fafc;
            border-left: 5px solid #10b981;
            padding: 15px;
            border-radius: 10px;
        }}

        .resultado span {{
            font-size: 28px;
            font-weight: bold;
            color: #10b981;
        }}

    </style>

</head>

<body>

    <div class="container">

        <h1>🧮 Calculadora + Supabase</h1>

        <form method="POST">

            <input
                type="text"
                name="nombre"
                placeholder="Ingresa tu nombre"
                required
            >

            <input
                id="expresion"
                class="display"
                type="text"
                name="expresion"
                readonly
                required
            >

            <div class="buttons">

                <button type="button" class="num" onclick="agregar('7')">7</button>
                <button type="button" class="num" onclick="agregar('8')">8</button>
                <button type="button" class="num" onclick="agregar('9')">9</button>
                <button type="button" class="op" onclick="agregar('/')">÷</button>

                <button type="button" class="num" onclick="agregar('4')">4</button>
                <button type="button" class="num" onclick="agregar('5')">5</button>
                <button type="button" class="num" onclick="agregar('6')">6</button>
                <button type="button" class="op" onclick="agregar('*')">×</button>

                <button type="button" class="num" onclick="agregar('1')">1</button>
                <button type="button" class="num" onclick="agregar('2')">2</button>
                <button type="button" class="num" onclick="agregar('3')">3</button>
                <button type="button" class="op" onclick="agregar('-')">−</button>

                <button type="button" class="num" onclick="agregar('0')">0</button>
                <button type="button" class="num" onclick="agregar('.')">.</button>
                <button type="button" class="clear" onclick="limpiar()">C</button>
                <button type="button" class="op" onclick="agregar('+')">+</button>

            </div>

            <button class="save" type="submit">
                Calcular y Guardar en Supabase
            </button>

        </form>

        <div class="resultado">
            <h3>Resultado</h3>
            <span>{resultado}</span>
        </div>

    </div>

    <script>

        function agregar(valor) {{
            document.getElementById("expresion").value += valor;
        }}

        function limpiar() {{
            document.getElementById("expresion").value = "";
        }}

    </script>

</body>

</html>
"""