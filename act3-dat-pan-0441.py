import pandas as pd
import matplotlib.pyplot as plt
## Ramirez Azul NC 0441 NL 47
print("Diccionario de inversiones en bolsa")
# 1. Crear diccionario con datos de inversiones en bolsa
inversiones_bolsa = {
    'id_inversion': [101, 102, 103, 104, 105, 106],
    'cliente': ['Ana', 'Luis', 'Sofia', 'Carlos', 'Maria', 'Jorge'],
    'ticker': ['AAPL', 'TSLA', 'AMZN', 'MSFT', 'GOOGL', 'META'],
    'nombre_empresa': ['Apple', 'Tesla', 'Amazon', 'Microsoft', 'Google', 'Meta'],
    'cantidad_acciones': [10, 5, 8, 15, 12, 6],
    'precio_compra': [150, 200, 130, 250, 120, 180],
    'precio_actual': [180, 220, 150, 300, 140, 200],
    'inversion_inicial': [1500, 1000, 1040, 3750, 1440, 1080],
    'valor_actual': [1800, 1100, 1200, 4500, 1680, 1200],
    'rendimiento_porcentaje': [20.0, 10.0, 15.3, 20.0, 16.6, 11.1]
}

print("Analisis Exploratorio de Datos EDA")
print("Exploratory Data Analysis) porRamirez Azul NC 0441 NL 47")
print("5. Crear el diccionario con 10 listas y 6 elementos")

# 2. Convertir el diccionario en un DataFrame
df = pd.DataFrame(inversiones_bolsa)
print("\n--- Tabla original de inversiones en bolsa ---")
print(df)

# 3. Exportar los datos a CSV
print("+-+-+ Convertir el DataFrame en archivo CSV +-+-+")
df.to_csv(
    'inversiones_bolsa_0441.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("+-+-+ 8. Leer los datos desde el archivo CSV +-+-+")
print("inversiones_bolsa_0441.csv")

# 4. Leer el archivo CSV
df = pd.read_csv('inversiones_bolsa_0441.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
print("+-+-+ 9. Análisis Exploratorio de Datos (EDA) +-+-+")

# 5. Primeros y últimos registros
print("+-+-+ \n1. PRIMEROS REGISTROS (Head): +-+-+")
print(df.head(3)) # Muestra los primeros 3
print("+-+-+ \n2. ÚLTIMOS REGISTROS (Tail): +-+-+")
print(df.tail(2)) # Muestra los últimos 2

# 6. Dimensiones y estructura
print("+-+-+ 6. Dimensiones y estructura +-+-+")
print(df) # Mostrar tabla original o matriz
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("+-+-+ 7. Estadísticas y limpieza +-+-+")
print("+-+-+- \n7. ESTADÍSTICAS DESCRIPTIVAS: +-+-+")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Empresas únicas:", df['nombre_empresa'].unique())

# 8. Análisis específico
print(df)
print("--------------------------------------------------------")
print("\n11. INVERSIONES POR EMPRESA:")
print(df['nombre_empresa'].value_counts())

print("\n12. PROMEDIO DE VALOR ACTUAL: $", df['valor_actual'].mean())
print("13. VALOR ACTUAL MÁXIMO: $", df['valor_actual'].max())
print("14. VALOR ACTUAL MÍNIMO: $", df['valor_actual'].min())

# 9. Ordenamiento, filtrado y agrupación
print("---- 9. Ordenamiento, filtrado y agrupación ----")
print("\n15. INVERSIONES ORDENADAS POR VALOR ACTUAL (Mayor a menor):")
print(df.sort_values(by='valor_actual', ascending=False))

print("\n16. INVERSIONES CON RENDIMIENTO MAYOR A 15%:")
filtro = df[df['rendimiento_porcentaje'] > 15.0]
print(filtro)

print("\n17. RESUMEN POR RENDIMIENTO PORCENTUAL:")
resumen = df.groupby('rendimiento_porcentaje').agg(
    inversiones=('id_inversion', 'count'),
    valor_actual_promedio=('valor_actual', 'mean'),
    inversion_maxima=('inversion_inicial', 'max')
)
print(resumen)

# 18. Gráfica de barras: Cantidad de acciones por empresa
print("18. Gráfica de barras: Cantidad de acciones por empresa")
plt.figure(figsize=(8, 5))
plt.bar(df['nombre_empresa'], df['cantidad_acciones'], color='skyblue')
plt.title('Cantidad de acciones adquiridas por empresa - Ramirez Azul 0441')
plt.xlabel('Empresa')
plt.ylabel('Cantidad de acciones')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Valor actual por cliente
plt.figure(figsize=(8, 5))
plt.bar(df['cliente'], df['valor_actual'], color='lightgreen')
plt.title('Valor actual de inversión por cliente - EDA Ramirez Azul 0441')
plt.xlabel('Cliente')
plt.ylabel('Valor actual ($ USD)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de rendimientos porcentuales
plt.figure(figsize=(8, 5))
plt.hist(df['rendimiento_porcentaje'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de rendimientos porcentuales - Ramirez Azul 0441')
plt.xlabel('Rendimiento (%)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Inversión inicial vs Valor actual
plt.figure(figsize=(8, 5))
plt.scatter(df['inversion_inicial'], df['valor_actual'], color='red', s=100)
plt.title('Relación entre inversión inicial y valor actual - Ramirez Azul 0441')
plt.xlabel('Inversión inicial ($ USD)')
plt.ylabel('Valor actual ($ USD)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de valores actuales
plt.figure(figsize=(7, 5))
plt.boxplot(df['valor_actual'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de valores actuales (Boxplot) - EDA Ramirez Azul 0441')
plt.ylabel('Valor actual ($ USD)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas - EDA Ramirez Azul 0441')
plt.tight_layout()
plt.show()

print("Ramirez Azul NC 0441 NL 47")