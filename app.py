from flask import Flask, render_template_string

app = Flask(__name__)

# Simulamos contenido básico como plantilla HTML
template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Publicidad Visual Pro</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; }
        header, nav, section, footer { padding: 20px; }
        header { background: #001f3f; color: white; text-align: center; }
        nav { background: #f0f0f0; }
        nav a { margin-right: 15px; text-decoration: none; color: #0074D9; }
        .portada {
            background: url('https://cdn.openai.com/chatgpt/production/0348ab95-7f37-4b20-9f08-e4e2041cbb88.png') no-repeat center center;
            background-size: cover;
            height: 300px;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
        }
        section { margin: 20px; }
        .servicio, .trabajo { margin-bottom: 20px; padding: 10px; background: white; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .contacto, .quienes { background: #e0f7fa; padding: 20px; border-radius: 8px; }
        footer { background: #001f3f; color: white; text-align: center; }
    </style>
</head>
<body>
    <header>
        <h1>Publicidad Visual Pro</h1>
        <p>Diseñamos e instalamos publicidad visual con impacto</p>
    </header>

    <nav>
        <a href="#servicios">Servicios</a>
        <a href="#portafolio">Portafolio</a>
        <a href="#quienes">Quiénes Somos</a>
        <a href="#contacto">Contacto</a>
    </nav>

    <div class="portada">Publicidad de alto impacto visual</div>

    <section id="servicios">
        <h2>Servicios</h2>
        <div class="servicio"><strong>Diseño gráfico y branding</strong><br>Creación de identidad visual profesional.</div>
        <div class="servicio"><strong>Impresión y producción</strong><br>Adhesivos, gigantografías, pendones y más.</div>
        <div class="servicio"><strong>Instalación y fabricación</strong><br>Letras 3D, estructuras metálicas, bastidores.</div>
        <div class="servicio"><strong>Mantenimiento de publicidad</strong><br>Reparaciones y limpieza de soportes existentes.</div>
        <div class="servicio"><strong>Innovaciones futuras</strong><br>Stands interactivos, señalética digital.</div>
    </section>

    <section id="portafolio">
        <h2>Portafolio</h2>
        <div class="trabajo">Letra corpórea para tienda comercial (antes/después)</div>
        <div class="trabajo">Gráfica vehicular para empresa logística</div>
        <div class="trabajo">Señalética institucional en oficina corporativa</div>
    </section>

    <section id="quienes" class="quienes">
        <h2>Quiénes Somos</h2>
        <p>Somos una empresa con más de 10 años en el rubro de la publicidad visual. Nos destacamos por ofrecer soluciones a medida, tiempos rápidos y materiales de alta calidad.</p>
        <p>Hemos trabajado con más de 300 clientes en Chile y Sudamérica.</p>
    </section>

    <section id="contacto" class="contacto">
        <h2>Contacto</h2>
        <form>
            Nombre: <input type="text"><br><br>
            Correo: <input type="email"><br><br>
            Mensaje: <textarea></textarea><br><br>
            <button type="submit">Enviar</button>
        </form>
        <p>O contáctanos directo por WhatsApp: <strong>+56 9 1234 5678</strong></p>
    </section>

    <footer>
        &copy; 2025 Publicidad Visual Pro | contacto@publicidadpro.cl
    </footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)
