# development-utils

Repositorio de utilidades reutilizables para tareas habituales de desarrollo. Su objetivo es centralizar soluciones prácticas, facilitar su consulta y evitar la duplicación de código entre proyectos.

## Contenido

- [Catálogo de utilidades](#catálogo-de-utilidades)
- [Organización del repositorio](#organización-del-repositorio)
- [Cómo utilizar una utilidad](#cómo-utilizar-una-utilidad)
- [Configuración y variables de entorno](#configuración-y-variables-de-entorno)
- [Cómo contribuir](#cómo-contribuir)
- [Criterios de calidad](#criterios-de-calidad)

## Catálogo de utilidades

Antes de crear una nueva utilidad, consulta este catálogo para comprobar si ya existe una solución que puedas reutilizar o ampliar.

Actualmente no hay utilidades publicadas. Al incorporar la primera, sustituye la fila informativa por una entrada con un enlace a su documentación.

| Utilidad | Descripción | Lenguaje | Framework | Documentación |
| --- | --- | --- | --- | --- |
| — | Sin utilidades publicadas por el momento. | — | — | — |

## Organización del repositorio

Las nuevas utilidades deben agruparse por **lenguaje** y, cuando corresponda, por **framework**. Cada utilidad debe disponer de su propia carpeta y de instrucciones suficientes para utilizarla de forma independiente.

Estructura de referencia para futuras incorporaciones:

```text
development-utils/
├── README.md
└── <lenguaje>/
    ├── <utilidad>/
    │   ├── README.md
    │   └── ...
    └── <framework>/
        └── <utilidad>/
            ├── README.md
            └── ...
```

- Utiliza nombres de carpeta descriptivos, en minúsculas y separados por guiones.
- Omite el nivel de framework cuando la utilidad no dependa de uno.
- Mantén junto a cada utilidad su código, documentación, ejemplos y archivos de configuración necesarios.

## Cómo utilizar una utilidad

1. Localiza la solución en el catálogo.
2. Accede a su carpeta y consulta su documentación.
3. Comprueba los requisitos y las versiones compatibles del lenguaje, framework y herramientas.
4. Instala las dependencias siguiendo las instrucciones de esa utilidad.
5. Configura las variables de entorno, si son necesarias.
6. Ejecuta el ejemplo de uso y verifica el resultado esperado antes de integrarla en otro proyecto.

Este repositorio todavía no define requisitos de ejecución ni comandos de instalación globales. Cada utilidad deberá documentar los suyos.

## Configuración y variables de entorno

Cuando una utilidad requiera variables de entorno, incluye un archivo `.env.example` en su misma carpeta para facilitar la reproducción de la configuración.

Este archivo debe:

- Enumerar las variables necesarias e indicar su finalidad en comentarios.
- Distinguir las variables obligatorias de las opcionales.
- Utilizar valores ficticios o de ejemplo, nunca credenciales reales.
- Documentar los valores predeterminados y las restricciones relevantes.

La documentación de la utilidad debe explicar cómo crear la configuración local a partir de ese ejemplo y cómo se cargan las variables. No presupongas que el entorno lee automáticamente un archivo `.env`.

**No publiques contraseñas, tokens, claves privadas ni otros datos sensibles.** Si se utiliza un archivo `.env` local con secretos, exclúyelo del control de versiones mediante la configuración de `.gitignore` correspondiente.

## Cómo contribuir

Para añadir o mejorar una utilidad:

1. **Revisa el catálogo.** Prioriza ampliar una solución existente cuando cubra la misma necesidad.
2. **Organiza los archivos.** Respeta la clasificación por lenguaje y framework.
3. **Implementa una solución acotada.** Evita dependencias innecesarias y comportamientos ajenos al propósito de la utilidad.
4. **Documenta su uso.** Incluye un `README.md` en la carpeta de la utilidad con:
   - Propósito y casos de uso.
   - Requisitos y versiones compatibles.
   - Instalación y dependencias.
   - Configuración y variables de entorno, si aplica.
   - Ejemplo mínimo de ejecución y resultado esperado.
   - Instrucciones de validación o pruebas.
   - Limitaciones conocidas y precauciones de uso.
5. **Añade la configuración de ejemplo.** Incluye `.env.example` cuando sea necesario, sin datos sensibles.
6. **Valida los cambios.** Comprueba las instrucciones desde una configuración limpia y ejecuta las pruebas disponibles.
7. **Actualiza el catálogo.** Añade o ajusta la entrada con su descripción, lenguaje, framework y enlace relativo a la documentación. Indica «No aplica» si no utiliza un framework.
8. **Presenta los cambios para revisión.** Describe el problema resuelto, el alcance de la solución y las comprobaciones realizadas.

## Criterios de calidad

- **Reutilización:** evita valores específicos de un proyecto cuando deban ser configurables.
- **Claridad:** favorece soluciones sencillas y nombres que expresen su intención.
- **Reproducibilidad:** proporciona pasos completos y ejemplos que puedan ejecutarse.
- **Seguridad:** valida las entradas relevantes y explica los efectos sobre archivos, servicios o datos antes de ejecutar acciones que los modifiquen.
- **Mantenimiento:** conserva la documentación y el catálogo alineados con el comportamiento real.