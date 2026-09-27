# Punto de entrada de la aplicación.
# Su única responsabilidad es crear el servidor Flask y conectar las rutas.
from flask import Flask
from controllers.automata_controller import automata_bp

app = Flask(__name__)

# Conecta las rutas definidas en el Controller (Blueprint) con la app principal.
app.register_blueprint(automata_bp)

if __name__ == "__main__":
    # debug=True recarga el servidor automáticamente al detectar cambios en el código
    # y muestra errores detallados en el navegador (solo para desarrollo).
    app.run(debug=True, port=5000)