let mapa;
let marker;

async function cargarCalles() {
  const res = await fetch('data/calles.json');
  const calles = await res.json();

  const selector = document.getElementById('selectorCalles');

  calles.forEach(calle => {
    const option = document.createElement('option');
    option.value = calle.id;
    option.textContent = calle.nombre;
    selector.appendChild(option);
  });

  selector.addEventListener('change', () => mostrarCalle(calles, selector.value));

  // Mostrar la primera por defecto
  mostrarCalle(calles, calles[0].id);
}

function mostrarCalle(calles, id) {
  const calle = calles.find(c => c.id === id);

  document.getElementById('titulo').textContent = calle.nombre;
  document.getElementById('leyenda').textContent = calle.leyenda;
  document.getElementById('imagen').src = calle.imagen;

  if (!mapa) {
    mapa = L.map('map').setView(calle.coords, 17);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(mapa);
    marker = L.marker(calle.coords).addTo(mapa);
  } else {
    mapa.setView(calle.coords, 17);
    marker.setLatLng(calle.coords);
  }
}

cargarCalles();