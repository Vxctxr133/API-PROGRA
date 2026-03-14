package com.umg.parcial.repository;

import java.util.ArrayList;
import java.util.List;
import org.springframework.stereotype.Repository;
import com.umg.parcial.model.Node;
import com.umg.parcial.model.Tarea;

@Repository
public class TareaRepository {
    private Node head; // La cabeza de nuestra lista enlazada

    public TareaRepository() {
        this.head = null;
    }

    // 1. Crear elemento
    public Tarea insertar(Tarea tarea) {
        Node newNode = new Node(tarea);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.getNext() != null) {
                current = current.getNext(); // Recorremos hasta el último nodo
            }
            current.setNext(newNode); // Enlazamos el nuevo nodo al final
        }
        return tarea;
    }

    // 2. Listar elementos (Extraemos las tareas de los nodos para enviarlas al cliente)
    public List<Tarea> listar() {
        List<Tarea> listaRespuestas = new ArrayList<>(); 
        Node current = head;
        while (current != null) {
            listaRespuestas.add(current.getTarea());
            current = current.getNext();
        }
        return listaRespuestas;
    }

    // 3. Buscar por id
    public Tarea buscarPorId(int id) {
        Node current = head;
        while (current != null) {
            if (current.getTarea().getId() == id) {
                return current.getTarea();
            }
            current = current.getNext();
        }
        return null; // Si no lo encuentra
    }

    // 4. Eliminar elemento
    public boolean eliminar(int id) {
        if (head == null) return false; // Lista vacía

        // Si el elemento a eliminar es la cabeza
        if (head.getTarea().getId() == id) {
            head = head.getNext(); 
            return true;
        }

        Node current = head;
        while (current.getNext() != null) {
            if (current.getNext().getTarea().getId() == id) {
                // Saltamos el nodo para eliminarlo de la lista
                current.setNext(current.getNext().getNext());
                return true;
            }
            current = current.getNext();
        }
        return false;
    }
}