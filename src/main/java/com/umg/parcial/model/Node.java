package com.umg.parcial.model;
import lombok.Data;

@Data
public class Node {
    private Tarea tarea;
    private Node next; // Apuntador al siguiente nodo

    public Node(Tarea tarea) {
        this.tarea = tarea;
        this.next = null; // Por defecto, el siguiente nodo es nulo
    }
}