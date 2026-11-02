import modelos_biblioteca as mb

def main():
    # Cargar inventario y usuarios desde archivos
    inventario_biblioteca = {}
    categorias_disponibles = set()
    usuarios_registrados = {}

    print("---1. Registrando usuarios ---")
    usuarios_registrados = mb.registrar_usuario(usuarios_registrados, "U001", "Ana Pérez")
    usuarios_registrados = mb.registrar_usuario(usuarios_registrados, "U002", "Luis González")
    print("Usuarios:", usuarios_registrados)

    print("\n---2. Registrando libros ---")
    inventario_biblioteca, categorias_disponibles = mb.registrar_libro(inventario_biblioteca, "978-3-16", "El Principito", "Saint-Exupéry", "Ficción", categorias_disponibles)
    print("Inventario:", inventario_biblioteca)
    print("Categorías disponibles:", categorias_disponibles)

    print("\n---3. Prestando libro ---")
    usuarios_registrados = mb.prestar_libro("978-3-16", "U001", inventario_biblioteca, usuarios_registrados)
    print("Usuarios después del préstamo:", usuarios_registrados)
    print("Inventario después del préstamo:", inventario_biblioteca)

if __name__ == "__main__":
    main()