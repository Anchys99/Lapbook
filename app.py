from flask import Flask, render_template

app = Flask(__name__)

TEMAS = [
    {
        "id": "html", "nombre": "HTML", "lema": "El esqueleto de la web",
        "concepto": "HyperText Markup Language es el lenguaje de marcado que define la estructura y el contenido de una página: qué es un título, un párrafo, una imagen o un enlace.",
        "elementos": ["<h1>–<h6>: títulos", "<p>: párrafos", "<a>: enlaces", "<img>: imágenes", "<ul> y <li>: listas", "<form> e <input>: formularios", "<header>, <main>, <footer>: semántica"],
        "ventajas": ["Fácil de aprender", "Lo entienden todos los navegadores", "Mejora el SEO y la accesibilidad con etiquetas semánticas", "Es la base de cualquier sitio web"],
        "funcionalidad": "El navegador lee el HTML, construye el árbol DOM y lo muestra en pantalla. CSS lo decora y JavaScript lo vuelve dinámico.",
        "ejemplo": "<h1>Hola, mundo</h1>\n<p>Mi primer <a href=\"#\">enlace</a>.</p>",
        "curiosidad": "HTML fue creado por Tim Berners-Lee en 1991.",
    },
    {
        "id": "css", "nombre": "CSS", "lema": "La piel y el estilo",
        "concepto": "Cascading Style Sheets describe cómo se ve el HTML: colores, tipografías, espacios, posiciones y animaciones.",
        "elementos": ["Selectores: .clase, #id, etiqueta", "Propiedades: color, margin, padding", "Valores: px, rem, %, hex", "Flexbox y Grid para el diseño", "Media queries para pantallas móviles", "Variables: --color-principal"],
        "ventajas": ["Separa el contenido del diseño", "Un solo archivo estiliza muchas páginas", "Diseño adaptable (responsive)", "Animaciones sin necesidad de JavaScript"],
        "funcionalidad": "El navegador compara cada selector con los elementos del DOM y aplica las reglas según su especificidad y su orden (la cascada).",
        "ejemplo": "h1 {\n  color: #7c3aed;\n  background: #22c55e;\n  padding: 1rem;\n}",
        "curiosidad": "CSS apareció en 1996 para dejar de usar etiquetas como <font>.",
    },
    {
        "id": "js", "nombre": "JavaScript", "lema": "El cerebro de la interacción",
        "concepto": "Es un lenguaje de programación que se ejecuta en el navegador (y en servidores con Node.js) y permite reaccionar a lo que hace la persona usuaria.",
        "elementos": ["Variables: let, const", "Tipos: string, number, boolean, array, object", "Funciones y funciones flecha", "Condicionales y ciclos", "Eventos: click, input, submit", "DOM: querySelector, classList", "fetch() para pedir datos"],
        "ventajas": ["Páginas dinámicas e interactivas", "Corre en todos los navegadores", "Enorme comunidad y librerías", "Sirve para frontend y backend"],
        "funcionalidad": "Escucha eventos, lee o cambia el DOM y puede pedir datos al servidor sin recargar la página.",
        "ejemplo": "document.querySelector('button')\n  .addEventListener('click', () => {\n    alert('¡Hola!');\n  });",
        "curiosidad": "Brendan Eich lo creó en solo 10 días, en 1995.",
    },
    {
        "id": "jinja", "nombre": "Jinja", "lema": "Plantillas que piensan",
        "concepto": "Jinja es un motor de plantillas de Python (usado por Flask) que mezcla HTML con datos del servidor antes de enviar la página.",
        "elementos": ["{{ variable }}: muestra un valor", "{% for %}: repite bloques", "{% if %}: condiciones", "{% extends %} y {% block %}: herencia", "{% include %}: reutilizar partes", "Filtros: {{ nombre|upper }}", "url_for(): rutas a archivos estáticos"],
        "ventajas": ["Evita repetir HTML", "Herencia de plantillas (un solo layout)", "Escapa HTML automáticamente (más seguridad)", "Separa la lógica de la presentación"],
        "funcionalidad": "Flask recibe una petición, ejecuta render_template(), Jinja reemplaza las llaves con datos reales y el navegador recibe HTML ya listo.",
        "ejemplo": "<ul>\n{% for t in temas %}\n  <li>{{ t.nombre }}</li>\n{% endfor %}\n</ul>",
        "curiosidad": "Su nombre viene de 'templo' en japonés, y se parece a las plantillas de Django.",
    },
    {
        "id": "sql", "nombre": "SQL", "lema": "La memoria de los datos",
        "concepto": "Structured Query Language sirve para crear, consultar, modificar y borrar información guardada en bases de datos relacionales.",
        "elementos": ["Tablas, filas y columnas", "SELECT: consultar", "INSERT: agregar", "UPDATE: modificar", "DELETE: eliminar", "WHERE, ORDER BY, GROUP BY", "JOIN: unir tablas", "Claves primarias y foráneas"],
        "ventajas": ["Estándar usado en todo el mundo", "Maneja millones de registros", "Mantiene los datos consistentes y seguros", "Consultas claras, casi como leer inglés"],
        "funcionalidad": "La aplicación envía una consulta al gestor (SQLite, MySQL, PostgreSQL) y este devuelve solo las filas que se pidieron.",
        "ejemplo": "SELECT nombre, edad\nFROM alumnos\nWHERE edad > 15\nORDER BY nombre;",
        "curiosidad": "SQL nació en los años 70 en IBM y todavía es la base de casi toda app.",
    },
]

FLAPS = [
    ("concepto", "Conceptos"),
    ("elementos", "Elementos"),
    ("ventajas", "Ventajas"),
    ("funcionalidad", "Funcionalidad"),
    ("ejemplo", "Ejemplo"),
    ("curiosidad", "Etc."),
]

@app.route("/")
def index():
    return render_template("index.html", temas=TEMAS, flaps=FLAPS)

if __name__ == "__main__":
    app.run(debug=True)
