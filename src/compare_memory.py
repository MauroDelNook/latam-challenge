import tracemalloc
import gc

# Función para comparar el uso de memoria en dos funciones
def compare_memory(func1, func2, file_path):
    # Comparar dos funciones:

    # Esto por cada función:
    def get_memory_usage(func, *args):
        gc.collect()  # Limpiar memoria en cada corrida
        tracemalloc.start()  # Registrar memoria
        func(*args)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return peak / 1024 / 1024 # Convierte a MB

    mem_usage_func1 = get_memory_usage(func1, file_path)
    mem_usage_func2 = get_memory_usage(func2, file_path)

    print(f"Uso de memoria para {func1.__name__}: {mem_usage_func1:.2f} MB")
    print(f"Uso de memoria para {func2.__name__}: {mem_usage_func2:.2f} MB")