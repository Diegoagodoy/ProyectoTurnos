# ProyectoTurnosGodoy

Aplicación web para gestionar turnos médicos, pacientes, médicos y especialidades.

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
- Futuro Uso de JavaScript y AJAX para filtrados dinámicos.

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
Médicos: /turnos/medicos/ → agregar y lista médicos.  
Especialidades: /turnos/especialidades/ → agregar y lista especialidades.  
Pacientes: /turnos/pacientes/ → agregar y lista pacientes.  
Turnos: /turnos/ → lista turnos; /turnos/crear/ → crear nuevo turno.  

Autor  

Diego A. Godoy