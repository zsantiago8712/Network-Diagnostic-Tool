import subprocess
import sys
import os

def install_dependencies():
    print("Instalando dependencias necesarias...")
    try:
        # Instalar dependencias desde requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencias instaladas correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error instalando dependencias: {e}")
        sys.exit(1)

def check_python_version():
    if sys.version_info < (3, 7):
        print("Este script requiere Python 3.7 o superior")
        sys.exit(1)

def main():
    check_python_version()
    install_dependencies()
    
    print("\nInstalación completada. Puede ejecutar el programa usando:")
    if os.name == 'nt':  # Windows
        print("network_diagnostic.exe [dominio/ip]")
    else:  # Linux/Mac
        print("./network_diagnostic [dominio/ip]")

if __name__ == "__main__":
    main()