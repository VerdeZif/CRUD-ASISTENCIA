
import { useState } from "react"
import axios from "axios";
import '../components/style/FormAlum.css'

function FormAlum({ onAgregar }){
    const [nombre, setNombre] = useState("");
    const [apellido, setApellido] = useState("");
    const [matricula, setMatricula] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!nombre || !apellido || !matricula) return;


        // --- DATOS SIMULADOS PARA PRUEBAS ---
        const nuevoEstudiante = {
            id: Math.floor(Math.random() * 10000), // id temporal
            nombre,
            apellido,
            matricula,
            asistencia: "",
            fecha: ""
        };

        onAgregar(nuevoEstudiante); // agrega al estado local

        setNombre("");
        setApellido("");
        setMatricula("");

        alert("✅ Estudiante agregado (mock)!");

        // try {
        //     const nuevoEstudiante = {
        //         nombre,
        //         apellido,
        //         matricula,
        //         asistencia: "", 
        //         fecha: ""       
        //     };

        //     const response = await axios.post("http://127.0.0.1:8000/api/asistencias/", nuevoEstudiante);

        //     onAgregar(response.data);

        //     setNombre("");
        //     setApellido("");
        //     setMatricula("");

        //     alert("✅ Estudiante guardado con éxito!");
        // } catch (error) {
        //     console.error(error);
        //     alert("❌ Error al guardar el estudiante");
        // }

    };
    return(
        <div>
            <form onSubmit={handleSubmit}>
                <h1>Datos del Estudiante</h1>   
                <input 
                    type="text" 
                    placeholder="Nombre del estudiante" 
                    value={nombre} 
                    onChange={(e) => 
                    setNombre(e.target.value)} 
                    required>
                </input>

                <input 
                    type="text" 
                    placeholder="Apellido del estudiante" 
                    value={apellido} 
                    onChange={(e) => setApellido(e.target.value)} 
                    required>                
                </input>

                <h2>Estado de matricula</h2>
                <div className="mt">
                    <input type="radio" id="con" name="oki" value="si" checked={matricula === "si"} 
                        onChange={(e) => setMatricula(e.target.value)}></input>
                    <label htmlFor="con">Con matricula</label>
                    
                    <input type="radio" id="sin" name="oki" value="no" checked={matricula === "no"} 
                        onChange={(e) => setMatricula(e.target.value)}></input>
                    <label htmlFor="sin">Sin matricula</label>
                </div>
                        
                <button type="submit">Agregar</button>

            </form>
        </div>
    )
}
export default FormAlum