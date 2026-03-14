package com.umg.parcial.service;

import java.util.List;
import org.springframework.stereotype.Service;
import com.umg.parcial.model.Tarea;
import com.umg.parcial.repository.TareaRepository;

@Service
public class TareaService {

    private final TareaRepository tareaRepository;

    public TareaService(TareaRepository tareaRepository) {
        this.tareaRepository = tareaRepository;
    }

    public Tarea crearTarea(Tarea tarea) {
        return tareaRepository.insertar(tarea);
    }

    public List<Tarea> obtenerTodas() {
        return tareaRepository.listar();
    }

    public Tarea obtenerPorId(int id) {
        return tareaRepository.buscarPorId(id);
    }

    public boolean eliminarTarea(int id) {
        return tareaRepository.eliminar(id);
    }
}
