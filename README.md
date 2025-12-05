Sistema de Registro y Análisis de Desempeño — Sigomota FC
Modelo: Jugador

Un jugador es la representación de un futbolista del equipo Sigomota FC.

Datos Personales del Jugador
Nombre completo

Número de camiseta

Fecha de nacimiento

Nacionalidad

Posición en el campo (Portero, Defensa, Centro, Extremo, Delantero)

Pie dominante

Altura y peso

Datos Deportivos del Jugador

Características: velocidad, resistencia, movilidad, flexibilidad

Rendimiento por posiciones

Nivel del jugador

Estado actual:

Disponible

Lesionado

Suspendido

Modelo: Estadísticas del Jugador
Para cada partido se registran:

Minutos jugados

Goles anotados

Asistencias

Tarjetas amarillas y rojas

Participación o no participación

Criterios de observación del comportamiento (madurez, disciplina, etc.)

Modelo: Partido
Cada partido es una unidad independiente con:

Equipo rival

Condición del partido (Local / Visitante)

Fecha del encuentro

Resultado final

Goles anotados y recibidos

Estado del partido:

Victoria, Empate, Derrota

En caso de empate por penales: registro de goles anotados y recibidos

Además, el partido agrupa todas las estadísticas individuales de los jugadores convocados.

Tecnologías y Requisitos Técnicos
Backend desarrollado con FastAPI, aplicando buenas prácticas.

API documentada y disponible públicamente.

base de datos obligatoria.

Interfaz HTML.

Repositorio compartido entre dos cuentas GitHub (autores del proyecto).

El sistema debe ser reproducible en otra máquina o servidor.

Procedimiento de Desarrollo
Forquear el repositorio base:
https://github.com/sigmoteam/final_DEV_1

Clonar el repositorio forkeado y trabajar el desarrollo localmente.

Implementar:

Modelos de datos

Endpoints REST

Validaciones

Persistencia de la información

Documentación automática FastAPI

Exponer una URL pública para uso y pruebas del sistema.

Construir la interfaz HTML con los endpoints integrados.

Subir datos de prueba suficientes para validar el funcionamiento.

Asegurar que el repositorio final incluya:

Código completo

Documentación (incluyendo este README)

URL pública

Capturas si son necesarias

Estructura recomendada del proyecto
/app
  /models
  /routes
  /schemas
  /database

/public
  index.html

/tests
requirements.txt
