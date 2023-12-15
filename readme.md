# Recomendador de contraseñas
***
## Descripcion
El Recomendador de Contraseñas es una aplicación sensilla construida con FastAPI que proporciona una manera segura y eficiente de generar contraseñas robustas para su uso en diversos servicios y aplicaciones. Este recomendador utiliza principios de seguridad y buenas prácticas para garantizar la creación de contraseñas fuertes y seguras.
***
## Requisitos
- Python >= 3
- FastAPI
- Uvicorn 
- SQLAlchemy 
- Pyjwt

***
## Instalación 
Clona el Repositorio:

- git clone https://github.com/LUISARAMIREZ08/Recomendador-de-Contrasenas-.git
***
## Activación de entorno virtual
Una vez que se haya clonado el repositorio, se abre la terminal y se ejecutan los siguientes comandos:
- Ve a la siguiente ruta para activar el entorno virtual:
  - cmd.exe
  
    **C:\> <venv>\Backend\venv\Scripts\activate.bat**

  - PowerShell

    **PS C:\> <venv>\Backedn\venv\Scripts\Activate.ps1**
***
## Intala las dependencias del proyecto 
En la terminal y dentro del entorno virtual, ejecuta el siguiente comando en la ruta C:\> <venv>\Backend:

**pip install -r requirements.txt**
***
## Ejecución 
- Ejecuta el servidor:
   **uvicorn main:app --reload**

- Accede a la documentación Swagger en http://localhost:8000/docs 
***
## Autenticación de Usuario
## Login
Para autenticarse en la aplicación, utiliza el endpoint POST /login.
- Ingresa el email: admin@mail.com
- Ingresa la contraseña: 123456

Al realizar la autenticación exitosa, se generará un token que deberá ser ingresado en el encabezado de autorización (Authorize).
***
## Endpoints del Recommender API
1. Obtener toda la Lista de Recommenders 
2. Obtener Recommender por ID 
3. Actualizar Contraseña de Recommender por ID 
4. Eliminar Recommender por ID
5. Generar Contraseña aleatoria 


