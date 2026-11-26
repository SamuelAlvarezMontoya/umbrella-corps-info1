Esto es Umbrella Corps un sistema de gestión de laboratorio de microbiología.

Está desarrollado en Python para el registro, seguimiento, análisis y control de muestras microbiológicas, cepas bacterianas y pruebas de sensibilidad antibiótica. Este es el desarrollo para la última actividad evaluativa del curso. Este es su desarrollo, lo trabajamos por commits, usando git y github.

Integrantes del Equipo:
Samuel Álvarez (Líder técnico, bases de datos, autenticación y módulo Administrador)
Hans Cardeño (Módulo Bacteriólogo y gestión de muestras en tiempo real)
Juan Pablo Villota (Análisis epidemiológico y exportación de reportes)

Algunos conceptos microbiológicos clave para entender el código (consulta):
-Tinción de Gram: Prueba diferencial de laboratorio que clasifica las bacterias en Gram positivas (pared celular gruesa de peptidoglicano, se tiñen de violeta) y Gram negativas (pared delgada con membrana externa, se tiñen de rosado/rojo), orientando la selección inicial del antibiótico.

-Concentración Mínima Inhibitoria (CMI): Es la concentración más baja de un antimicrobiano capaz de inhibir el crecimiento visible de un microorganismo tras un periodo de incubación estándar. Permite clasificar la cepa como Sensible, Intermedia o Resistente.

-Multirresistencia Bacteriana (MDR - *Multidrug-Resistant*): Condición en la cual una bacteria adquiere resistencia a al menos un agente antimicrobiano en tres o más categorías diferentes de antibióticos, representando una alerta epidemiológica prioritaria en entornos clínicos.

Se usó:
Lenguaje: Python 
Base de Datos Relacional: MySQL (XAMPP local) — Base de datos: ProF_Info120262
Base de Datos No Relacional: MongoDB Atlas (Nube) — Base de datos: ProF_Info120262
Manejo de Archivos: CSV, JSON, TXT y XML