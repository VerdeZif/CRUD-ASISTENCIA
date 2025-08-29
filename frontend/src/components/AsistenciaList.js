import React, { useEffect, useState } from 'react';
import axios from 'axios';
import FormAlum from './FormAlum';
import '../App.css'

function AsistenciaList() {
  
  const [asistencias, setAsistencias] = useState([]);

  const handleAgregar = (nuevo) => {
    setAsistencias([...asistencias, nuevo]);
  };
  
  useEffect(() => {

    // --- DATOS SIMULADOS PARA PRUEBAS ---
    const datosMock = [
      { id: 1, nombre: "Juan", apellido: "Pérez", matricula: "si", asistencia: "Presente", fecha: "2025-08-28" },
      { id: 2, nombre: "Ana", apellido: "Gómez", matricula: "no", asistencia: "Inasistencia", fecha: "2025-08-27" },
    ];
    setAsistencias(datosMock);

    // axios.get("http://127.0.0.1:8000/api/asistencias/")
    //   .then((response) => {
    //     setAsistencias(response.data);
        
    //   })
    //   .catch((error) => {
    //     console.error(error);
           
    //   });
  }, []);

  return (
    <div className='cont'>
      <div className='main-form'>
        <p>🧑‍💻</p>
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

                           // --- ACTUALIZAR ESTADO LOCAL (mock)
                        const nuevas = [...asistencias];
                        nuevas[index].asistencia = valor;
                        nuevas[index].fecha = fecha;
                        setAsistencias(nuevas);

                          // try {
                          //   await axios.patch(`http://127.0.0.1:8000/api/asistencias/${ob.id}/`, {
                          //     asistencia: valor,
                          //     fecha: fecha
                          //   });

                          //   const nuevas = [...asistencias];
                          //   nuevas[index].asistencia = valor;
                          //   nuevas[index].fecha = fecha;
                          //   setAsistencias(nuevas);
                          // } catch (error) {
                          //   console.error(error);
                          //   alert("❌ Error al guardar asistencia");
                          // }
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
                          // --- ACTUALIZAR ESTADO LOCAL (mock)
                          const nuevas = [...asistencias];
                          nuevas[index].nombre = nuevoNombre;
                          nuevas[index].apellido = nuevoApellido;
                          setAsistencias(nuevas);
                          // try {
                          //   await axios.patch(`http://127.0.0.1:8000/api/asistencias/${ob.id}/`, {
                          //     nombre: nuevoNombre,
                          //     apellido: nuevoApellido
                          //   });
                            
                          //   const nuevas = [...asistencias];
                          //   nuevas[index].nombre = nuevoNombre;
                          //   nuevas[index].apellido = nuevoApellido;
                          //   setAsistencias(nuevas);
                          // } catch (error) {
                          //   console.error(error);
                          //   alert("❌ Error al actualizar estudiante");
                          // }
                        }
                      }}
                    >
                      📝
                    </button>

                    <button
                      onClick={async () => {
                        if (window.confirm("¿Realmente lo eliminará?")) {
                          // --- ELIMINAR LOCALMENTE (mock)
                          const nuevas = asistencias.filter((_, i) => i !== index);
                          setAsistencias(nuevas);
                          
                          // try {
                          //   await axios.delete(`http://127.0.0.1:8000/api/asistencias/${ob.id}/`);
                          //   const nuevas = asistencias.filter((_, i) => i !== index);
                          //   setAsistencias(nuevas);
                          // } catch (error) {
                          //   console.error(error);
                          //   alert("❌ Error al eliminar estudiante");
                          // }
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