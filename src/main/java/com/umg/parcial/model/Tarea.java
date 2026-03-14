package com.umg.parcial.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data // Genera Getters, Setters y toString automáticamente
@AllArgsConstructor // Genera un constructor con todos los atributos
@NoArgsConstructor // Genera un constructor vacío
public class Tarea {
    private int id;
    private String titulo;
    private boolean completada;
}
