import React, { useEffect, useState } from 'react';
import axios from 'axios';
import FormAlum from './FormAlum';

function AsistenciaList() {
  const [asistencias, setAsistencias] = useState([]);

  const handleAgregar = (nuevo) => {
    setAsistencias([...asistencias, nuevo]);
  };

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/asistencias/")
      .then((response) => {
        setAsistencias(response.data);
        localStorage.setItem("pre-lista", JSON.stringify(response.data));
      })
      .catch((error) => {
        console.error(error);
        const guardado = localStorage.getItem("pre-lista");
        if (guardado) {
          setAsistencias(JSON.parse(guardado));
        }   
      });
  }, []);

  return (
    <div>
      <div className='main-formn'>
        <FormAlum onAgregar={handleAgregar} />
      </div>

      <div className='main-list'>
        <table>
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Apellido</th>
              <th>Asistencia</th>
              <th>Fecha</th>
              <th>Acciones</th>
              <th>Matrícula</th>
            </tr>
          </thead>
          <tbody>
            {asistencias.length === 0 ? (
              <tr>
                <td colSpan="6" style={{ textAlign: "center" }}>
                  NO HAY ESTUDIANTES
                </td>
              </tr>
            ) : (
              asistencias.map((ob, index) => (
                <tr key={ob.id || index}>
                  <td>{ob.nombre}</td>
                  <td>{ob.apellido}</td>
                  <td>
                    <select
                      value={ob.asistencia}
                      onChange={async (e) => {
                        const valor = e.target.value;
                        const fecha = new Date().toLocaleDateString();

                        try {
                          await axios.patch(`http://127.0.0.1:8000/api/asistencias/${ob.id}/`, {
                            asistencia: valor,
                            fecha: fecha
                          });

                          const nuevas = [...asistencias];
                          nuevas[index].asistencia = valor;
                          nuevas[index].fecha = fecha;
                          setAsistencias(nuevas);
                        } catch (error) {
                          console.error(error);
                          alert("❌ Error al guardar asistencia");
                        }
                      }}
                    >
                      <option value="">Seleccionar</option>
                      <option value="Presente">Presente</option>
                      <option value="Inasistencia">Inasistencia</option>
                    </select>
                  </td>
                  <td>{ob.fecha}</td>
                  <td>
                    <button
                      onClick={async () => {
                        const nuevoNombre = prompt("Nuevo nombre:", ob.nombre);
                        const nuevoApellido = prompt("Nuevo apellido:", ob.apellido);

                        if (nuevoNombre && nuevoApellido) {
                          try {
                            await axios.patch(`http://127.0.0.1:8000/api/asistencias/${ob.id}/`, {
                              nombre: nuevoNombre,
                              apellido: nuevoApellido
                            });
                            
                            const nuevas = [...asistencias];
                            nuevas[index].nombre = nuevoNombre;
                            nuevas[index].apellido = nuevoApellido;
                            setAsistencias(nuevas);
                          } catch (error) {
                            console.error(error);
                            alert("❌ Error al actualizar estudiante");
                          }
                        }
                      }}
                    >
                      📝
                    </button>

                    <button
                      onClick={async () => {
                        if (window.confirm("¿Realmente lo eliminará?")) {
                          try {
                            await axios.delete(`http://127.0.0.1:8000/api/asistencias/${ob.id}/`);
                            const nuevas = asistencias.filter((_, i) => i !== index);
                            setAsistencias(nuevas);
                          } catch (error) {
                            console.error(error);
                            alert("❌ Error al eliminar estudiante");
                          }
                        }
                      }}
                    >
                      ❌
                    </button>
                  </td>
                  <td>{ob.matricula === "si" ? "✅ Sí" : "❌ No"}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default AsistenciaList;