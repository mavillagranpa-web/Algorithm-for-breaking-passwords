# Password Cracker - Fuerza Bruta

Un programa de fuerza bruta para demostrar la importancia de contraseñas seguras, inspirado en referencias de anime.

## Cómo ejecutar el programa

### Requisitos previos
- Python 3.6+
- Bibliotecas: matplotlib, itertools (vienen con Python)

### Instalación
```bash
# Clonar el repositorio
git clone https://github.com/mavillagranpa-web/Algorithm-for-breaking-passwords.git
cd password-cracker 
# Instalar dependencias (si es necesario)
pip install matplotlib


Ejmplo de salida

Soy… el fantasma de los Uchiha
Conjuntos disponibles: {1: 'abcdefghijklmnopqrstuvwxyz', 2: 'ABCDEFGHIJKLMNOPQRSTUVWXYZÑ', 3: '0123456789', 4: '!@#$%^&*()-_=+,|{};:/?.'}

¿Desea ingresar más datos si/no? si
Ingrese una contraseña de prueba: abc
Contraseña encontrada: abc
Intentos realizados: 731
Tiempo de ejecución: 0.001234 segundos

¿Desea ingresar más datos s/n? si
Ingrese una contraseña de prueba: Mateo123
Contraseña encontrada: Mateo123
Intentos realizados: 711895029
Tiempo de ejecución: 241.674838 segundos



Reflexión: ¿Qué pasa si la contraseña tiene 8+ caracteres y usa mayúsculas, números y símbolos?

Una contraseña con estas características presenta un desafío exponencialmente mayor para un ataque de fuerza bruta:

Complejidad del espacio de búsqueda: Con 26 minúsculas + 27 mayúsculas/Ñ + 10 números + 23 símbolos = 86 caracteres posibles

Cálculo de combinaciones:

8 caracteres: 86⁸ = ≈ 2.99 × 10¹⁵ combinaciones

10 caracteres: 86¹⁰ = ≈ 2.21 × 10¹⁹ combinaciones

12 caracteres: 86¹² = ≈ 1.63 × 10²³ combinaciones

Tiempo estimado: Aunque depende de la velocidad del hardware, una contraseña de 8 caracteres complejos podría tomar:

A 1000 intentos/segundo: ≈ 95,000 años

A 1,000,000 intentos/segundo: ≈ 95 años

A 1,000,000,000 intentos/segundo: ≈ 34 días

Esto demuestra la importancia crucial de usar contraseñas largas y complejas para la seguridad digital.
