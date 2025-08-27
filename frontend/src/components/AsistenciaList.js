import React, { useEffect, useState } from 'react';
import axios from 'axios';

function AsistenciaList() {
  const [asistencias, setAsistencias] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/asistencias/')
      .then(response => setAsistencias(response.data))
      .catch(error => console.error(error));
  }, []);

  return (
    <div>
      <h2>Lista de Asistencias</h2>
      <ul>
        {asistencias.map(a => (
          <li key={a.id}>{a.estudiante} - {a.fecha}</li>
        ))}
      </ul>
    </div>
  );
}

export default AsistenciaList;
