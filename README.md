# 🖥️ Sistema de Préstamos de Equipos

Aplicación de consola desarrollada en **Python** para gestionar el inventario, préstamos y devoluciones de equipos de cómputo dentro de una institución educativa o empresarial.

---

## 📁 Estructura del proyecto

```
sistema-prestamos/
├── prestamos_equipos.py   # Archivo principal del sistema
└── README.md
```

---

## 🎯 Descripción

El sistema permite llevar un control organizado del inventario de equipos mediante un menú interactivo. Cada operación está dividida en funciones modulares e independientes que aplican los conceptos de **listas**, **tuplas** y **diccionarios** de Python.

---

## 🧱 Estructura de datos

### Diccionario principal de equipos

```python
equipos = {
    "Laptop Dell": {
        "disponible": True,                          # bool → estado del equipo
        "prestamos": [("Carlos Pérez", "2025-04-20")]  # list de tuplas
    }
}
```

| Concepto        | Uso en el proyecto                                              |
|-----------------|-----------------------------------------------------------------|
| **Diccionario** | Almacena todos los equipos, su estado y su historial           |
| **Lista**       | Guarda el historial de préstamos de cada equipo                |
| **Tupla**       | Registra cada préstamo como `(usuario, fecha)` — inmutable     |

---

## ⚙️ Funciones del sistema

### `mostrar_equipos()`
Recorre el diccionario y muestra cada equipo con su estado actual.

```
✅ Disponible   →  equipo libre para préstamo
❌ Prestado     →  equipo actualmente en uso
```

---

### `registrar_prestamo()`
Registra un nuevo préstamo asociando un equipo a un usuario.

**Validaciones:**
- El equipo debe existir en el sistema.
- El equipo debe estar disponible.
- El nombre del usuario no puede estar vacío.

**Resultado:** Se guarda una tupla `(usuario, fecha)` en la lista de préstamos del equipo y su estado cambia a `disponible = False`.

---

### `devolver_equipo()`
Marca un equipo como devuelto y lo deja disponible nuevamente.

**Validaciones:**
- El equipo debe existir en el sistema.
- El equipo debe estar actualmente prestado.

---

### `ver_historial()`
Muestra el historial completo de préstamos de todos los equipos.

```
🖥️  Laptop Dell:
     1. Usuario: Ana Torres          | Fecha: 2025-05-01
     2. Usuario: Luis Gómez          | Fecha: 2025-05-06

🖥️  Tablet Samsung:
     Sin préstamos registrados.
```

---

### `agregar_equipo()`
Agrega un nuevo equipo al inventario.

**Validaciones:**
- El nombre no puede estar vacío.
- El equipo no debe existir ya en el sistema.

**Resultado:** Se añade al diccionario con `disponible = True` y lista de préstamos vacía.

---

### `menu()`
Función principal que gestiona la navegación del sistema mediante un bucle `while`.

```
======================================
   🖥️  SISTEMA DE PRÉSTAMOS DE EQUIPOS
======================================
  1. Ver inventario de equipos
  2. Registrar préstamo
  3. Devolver equipo
  4. Ver historial de préstamos
  5. Agregar nuevo equipo
  6. Salir
======================================
```

---

## 🗺️ Flujo del programa

```
Inicio
  └── menu()
        ├── 1 → mostrar_equipos()
        ├── 2 → registrar_prestamo()
        │         ├── Validar existencia del equipo
        │         ├── Validar disponibilidad
        │         └── Guardar tupla (usuario, fecha) en historial
        ├── 3 → devolver_equipo()
        │         ├── Validar existencia del equipo
        │         └── Validar que esté prestado
        ├── 4 → ver_historial()
        ├── 5 → agregar_equipo()
        │         └── Validar que no exista previamente
        └── 6 → Salir
```

---

## 🧠 Conceptos aplicados

| Concepto              | Aplicación concreta                                                    |
|-----------------------|------------------------------------------------------------------------|
| **Diccionarios**      | Inventario principal con datos anidados por equipo                     |
| **Listas**            | Historial de préstamos acumulado por equipo                            |
| **Tuplas**            | Registro inmutable de cada préstamo `(usuario, fecha)`                 |
| **Funciones**         | Lógica dividida en módulos independientes y reutilizables              |
| **Bucle `while`**     | Menú que se repite hasta que el usuario elige Salir                    |
| **Condicionales**     | Validaciones en cada operación antes de modificar el estado            |
| **`enumerate()`**     | Numeración del historial al recorrer la lista de préstamos             |
| **`date.today()`**    | Fecha automática del sistema al registrar cada préstamo                |

---

## ▶️ Ejecución

```bash
python prestamos_equipos.py
Img/1.png Img/2.png Img/3.png Img/4.png
```

> Requiere **Python 3.6+**. No necesita librerías externas (solo `datetime` de la librería estándar).

---

## 📦 Inventario inicial

El sistema incluye 5 equipos precargados como ejemplo:

| Equipo             | Estado inicial |
|--------------------|----------------|
| Laptop Dell        | ✅ Disponible  |
| Laptop HP          | ✅ Disponible  |
| Tablet Samsung     | ✅ Disponible  |
| Proyector Epson    | ✅ Disponible  |
| PC de Escritorio   | ❌ Prestado    |

---

## 👤 Autor: Vanessa Ocampo Zapata