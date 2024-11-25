# Informe de Avance Realizado en Clase

Vamos a explicar cómo se diseñó e implementó el proyecto `distributed_config` siguiendo los requisitos proporcionados. Este informe incluye la descripción de las clases, la estructura del proyecto, la ejecución, pruebas realizadas y análisis del código desarrollado.

---

## Objetivo

El proyecto tiene como objetivo simular un sistema de gestión de configuraciones distribuidas para un clúster de nodos (similar a Kubernetes). El sistema permite:
1. Validar configuraciones antes de propagarlas.
2. Propagar configuraciones a nodos activos secuencialmente.
3. Manejar errores en nodos inactivos sin interrumpir el flujo.
4. Generar reportes detallados y registrar logs en varios niveles (`DEBUG`, `INFO`, `ERROR`).

---

## Estructura del Proyecto

### Clases Principales

1. **`ConfigManager`**
   - Carga y valida las configuraciones desde un archivo `JSON` o `YAML`.
   - Propaga las configuraciones a los nodos secuencialmente.
   - Genera un reporte final con el estado de cada nodo y el tiempo total del proceso.

2. **`Node`**
   - Representa un nodo dentro del clúster.
   - Recibe configuraciones y las aplica si está activo.
   - Genera errores si el nodo está inactivo.

3. **`LoggerConfig`**
   - Gestiona el sistema de logging para registrar eventos durante la ejecución.
   - Configura niveles de logging (`DEBUG`, `INFO`, `ERROR`) con timestamps y mensajes detallados.

4. **`CLIManager`**
   - Implementa una interfaz de línea de comandos para interactuar con el sistema.
   - Permite cargar configuraciones, visualizar el estado de los nodos y actualizar configuraciones específicas.

---