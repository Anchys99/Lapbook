const solapas = document.querySelectorAll('.solapa');
const contador = document.getElementById('contador');
const barra = document.getElementById('barraRelleno');
document.getElementById('total').textContent = solapas.length;

function actualizarProgreso() {
  const vistas = document.querySelectorAll('.solapa.vista').length;
  contador.textContent = vistas;
  barra.style.width = (vistas / solapas.length * 100) + '%';
}

function alternar(solapa, abrir) {
  const btn = solapa.querySelector('.solapa-btn');
  const cuerpo = solapa.querySelector('.solapa-cuerpo');
  const estado = abrir ?? btn.getAttribute('aria-expanded') !== 'true';
  btn.setAttribute('aria-expanded', estado);
  cuerpo.classList.toggle('abierta', estado);
  if (estado) solapa.classList.add('vista');
  actualizarProgreso();
}

solapas.forEach(s => s.querySelector('.solapa-btn').addEventListener('click', () => alternar(s)));

// Pestañas de temas
const pestanas = document.querySelectorAll('.pestana');
pestanas.forEach(p => p.addEventListener('click', () => {
  pestanas.forEach(x => { x.classList.remove('activa'); x.setAttribute('aria-selected', 'false'); });
  p.classList.add('activa');
  p.setAttribute('aria-selected', 'true');
  document.querySelectorAll('.tema').forEach(t => t.classList.remove('visible'));
  document.getElementById('tema-' + p.dataset.tema).classList.add('visible');
}));

// Abrir / cerrar las solapas del tema visible
const visibles = () => document.querySelectorAll('.tema.visible .solapa');
document.getElementById('abrirTodo').onclick = () => visibles().forEach(s => alternar(s, true));
document.getElementById('cerrarTodo').onclick = () => visibles().forEach(s => alternar(s, false));

// Copiar código de ejemplo
document.querySelectorAll('.copiar').forEach(b => b.addEventListener('click', async () => {
  const texto = b.previousElementSibling.innerText;
  try { await navigator.clipboard.writeText(texto); b.textContent = '¡Copiado!'; }
  catch { b.textContent = 'No se pudo copiar'; }
  setTimeout(() => { b.textContent = 'Copiar código'; }, 1500);
}));

// Reto rápido
const preguntas = [
  { p: '¿Qué lenguaje define la estructura de una página?', o: ['HTML', 'CSS', 'SQL'], c: 0 },
  { p: '¿Cuál se usa para dar colores y estilos?', o: ['Jinja', 'CSS', 'JavaScript'], c: 1 },
  { p: '¿Qué hace {% for %} en Jinja?', o: ['Repite bloques', 'Borra datos', 'Cambia colores'], c: 0 },
  { p: '¿Qué sentencia SQL consulta datos?', o: ['INSERT', 'DELETE', 'SELECT'], c: 2 },
  { p: '¿Qué lenguaje reacciona a un clic?', o: ['JavaScript', 'HTML', 'SQL'], c: 0 },
];
let actual = -1;
const $ = id => document.getElementById(id);

function nuevaPregunta() {
  let n;
  do { n = Math.floor(Math.random() * preguntas.length); } while (n === actual);
  actual = n;
  const q = preguntas[n];
  $('pregunta').textContent = q.p;
  $('resultado').textContent = '';
  $('opciones').innerHTML = '';
  q.o.forEach((txt, i) => {
    const b = document.createElement('button');
    b.textContent = txt;
    b.onclick = () => {
      const ok = i === q.c;
      b.classList.add(ok ? 'bien' : 'mal');
      $('resultado').textContent = ok ? '¡Correcto!' : 'Casi. Prueba otra opción.';
    };
    $('opciones').appendChild(b);
  });
}
$('siguiente').onclick = nuevaPregunta;
nuevaPregunta();
