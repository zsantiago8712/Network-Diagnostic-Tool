# Network Diagnostic Tool

Una herramienta de diagnóstico de red que ayuda a identificar y solucionar problemas de conectividad de manera sistemática.

## 📋 Características

- Diagnóstico completo de conectividad a servidores y páginas web
- Verificación de resolución DNS
- Pruebas de ping
- Verificación de puertos (HTTP/HTTPS)
- Análisis de ruta (traceroute)
- Sugerencias de solución para cada problema detectado
- Compatible con Windows y Linux

## 🔧 Requisitos Previos

- Python 3.7 o superior
- Conexión a Internet
- Permisos de administrador (para algunas funcionalidades)

## 📦 Dependencias

```bash
requests==2.31.0
dnspython==2.4.2
```

## 💻 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/network-diagnostic-tool.git
cd network-diagnostic-tool
```

2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate     # En Windows
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## 🚀 Uso

### Como Script de Python

```bash
python network_diagnostic.py ejemplo.com
# o
python network_diagnostic.py 8.8.8.8
```

### Como Ejecutable

```bash
./network_diagnostic ejemplo.com  # Linux/Mac
# o
network_diagnostic.exe ejemplo.com  # Windows
```

## 📝 Ejemplos de Uso

```bash
# Diagnosticar un dominio
python network_diagnostic.py google.com

# Diagnosticar una IP
python network_diagnostic.py 142.250.200.110

# Diagnosticar un servidor local
python network_diagnostic.py localhost
```

## 🔍 Interpretación de Resultados

El script mostrará los resultados en el siguiente formato:

- ✓ (check mark): Indica una prueba exitosa
- ✗ (cross mark): Indica un fallo en la prueba
- ⚠ (warning): Indica problemas detectados con sus posibles soluciones

## 🛠️ Solución de Problemas

### Errores Comunes

1. "Permission denied":

   - Ejecuta el script con permisos de administrador

2. "Module not found":

   - Verifica que has instalado todas las dependencias
   - Asegúrate de estar en el entorno virtual correcto

3. "Connection timeout":
   - Verifica tu conexión a Internet
   - Comprueba si el objetivo está accesible

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE.md](LICENSE.md) para más detalles.

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir los cambios que te gustaría realizar.

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request
