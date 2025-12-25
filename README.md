# ProyectoTurnosGodoy

Aplicación web para gestionar turnos médicos, pacientes, médicos y especialidades.

## 🎥 Video Explicativo

Un video que muestra cómo funciona la aplicación y cómo usarla:
[Ver video explicativo] - https://drive.google.com/file/d/1V44eToCZ2v1E-eqF5UQSnk3B5DHkMn6b/view?usp=sharing

---

## Descripción

Esta aplicación permite:

- Administrar médicos y sus especialidades.
- Administrar pacientes.
- Crear y listar turnos médicos con fecha, hora y estado.
- Visualizar datos en tablas ordenadas.
- Navegar fácilmente entre secciones.

---

## Tecnologías utilizadas

- Python 3.10
- Django 5.2.9
- SQLite (base de datos por defecto)
- HTML5 / CSS
- Futuro uso de JavaScript y AJAX para filtrados dinámicos.

---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/usuario/ProyectoTurnosGodoy.git
cd ProyectoTurnosGodoy
```

2. Crear y activar entorno virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecutar migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Ejecutar servidor:

```bash
python manage.py runserver
```

6. Superusuario:

- Usuario: admin
- Password: admin

Uso

Inicio: / → enlaces a Turnos, Médicos, Especialidades, Pacientes y Administración.
Médicos: /turnos/medicos/ → agregar y listar médicos.
Especialidades: /turnos/especialidades/ → agregar y listar especialidades.
Pacientes: /turnos/pacientes/ → agregar y listar pacientes.
Turnos: /turnos/ → lista de turnos; /turnos/crear/ → crear nuevo turno.

Autor

Diego A. Godoy

[https://diegoagodoy.github.io/CV-DiegoAGodoy](https://diegoagodoy.github.io/CV-DiegoAGodoy/)/

[https://www.linkedin.com/in/diegoadolfogodoy/]()
