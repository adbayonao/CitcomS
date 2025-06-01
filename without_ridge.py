import numpy as np

# Cargar los datos desde el archivo
data = np.loadtxt("bvel.dat0")

# Obtener las filas que deseas repetir
x = data[109996:110253]  # Ajuste para incluir hasta la fila 110253

# Obtener las filas iniciales que se mantienen iguales
data1 = data[:109996]

# Replicar las filas seleccionadas
y = np.concatenate(([x]*85), axis=0)

# Combinar las filas iniciales con las replicadas
result = np.concatenate((data1, y))

# Guardar el resultado en un nuevo archivo
np.savetxt("bvel.dat0sd", result, fmt="%10.7f")

# Imprimir la longitud del resultado (opcional)
print("Longitud del resultado:", len(result))

