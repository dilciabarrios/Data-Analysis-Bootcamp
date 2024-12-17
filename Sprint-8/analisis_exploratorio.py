import matplotlib
import pandas as pd
import numpy as np
from scipy import stats  
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # Configurar un backend compatible


# Cargar los archivos CSV
df_trips = pd.read_csv('moved_project_sql_result_01.csv')
df_average = pd.read_csv('moved_project_sql_result_04.csv')
df_weather = pd.read_csv('moved_project_sql_result_07.csv')


#Imprimir información general de ambos DataFrames
print('Información general del dataframe que contiene número de viajes')
df_trips.info()

print('\nInformación general del dataframe  que contiene el promedio de viajes')
df_average.info()


# Verificar las primeras filas de ambos DataFrames
print('\nPrimeras filas del data frame que contiene número de viajes:')
print('\n')
print(df_trips.head())

print('\nPrimeras filas del data frame que contiene el promedio de viajes:')
print('\n')
print(df_average.head())
print('\n')

#Los 10 principipales barrios en términos de finalización del recorrido
print('\n Los 10 principales barrios en términos de finalización del recorrido')
print('\n')
df_filtro_ten = df_average.nlargest(10,'average_trips').reset_index(drop=True)
print(df_filtro_ten)
print('\n')


#Verificando si hay duplicados
print('\n')
duplicados_trips= df_trips.duplicated(keep=False).sum()
print('\nCantidad de duplicados en trips:', duplicados_trips)
print('\n')

#Verificando si hay duplicados
duplicados_average_trips= df_filtro_ten.duplicated(keep=False).sum()
print('\nCantidad de duplicados en average_trips:', duplicados_average_trips)
print('\n')


#Filtrar valor maximo y minimo en los recorridos de viajes de las compañías
fil_min = df_trips['trips_amount'].min()
print('\nValor minimo en df_trips:', fil_min)
fil_max = df_trips['trips_amount'].max()
print('\nValor maximo en df_trips:', fil_max)
print('\n')


#Filtrar compañía de taxi con viajes en rango de 2 a 50

print('\nFiltrar compañía con viajes en rango de 2 a 50')
print('\n')
fil_rango_one = df_trips[(df_trips['trips_amount']>=2) & (df_trips['trips_amount']<=50)].reset_index(drop=True)
print(fil_rango_one)
print('\n')


#Filtrar compañía de taxi con viajes en rango de 51 a 1000
print('\nFiltrar compañía con viajes en rango de 51 a 1000')
print('\n')
fil_rango_two = df_trips[(df_trips['trips_amount']>=51) & (df_trips['trips_amount']<=1000)].reset_index(drop=True)
print(fil_rango_two)
print('\n')


#Filtrar compañía de taxi con viajes en rango de 1001 a 6000
print('\nFiltrar compañía con viajes en rango de 1001 a 6000')
print('\n')
fil_rango_three = df_trips[(df_trips['trips_amount']>=1001) & (df_trips['trips_amount']<=6000)].reset_index(drop=True)
print(fil_rango_three)
print('\n')


#Filtrar compañía  de taxi con viajes en rango de 6001 a 20000
print('\nFiltrar compañía con viajes en rango de 6001 a 20000')
print('\n')
fil_rango_four = df_trips[(df_trips['trips_amount']>=6001) & (df_trips['trips_amount']<=20000)].reset_index(drop=True)
print(fil_rango_four)

# Crear grafico de barras (Compañía de taxi y numero de viajes)

fig, axs = plt.subplots(2, 2, figsize=(15, 9))

colors_plan = ['hotpink','purple']

# Gráfico de compañía de taxi con viajes en rango de 2 a 50

axs[0,0].bar(fil_rango_one['company_name'],fil_rango_one['trips_amount'], color='hotpink')
axs[0,0].set_ylabel('Número de viajes')
axs[0,0].set_title('Viajes por cada compañía de taxi (En rango de 2 a 50)')
axs[0,0].tick_params(axis='x')
axs[0,0].tick_params(axis='x', rotation=45)  # Rotar etiquetas
axs[0,0].set_xticks(range(len(fil_rango_one['company_name'])))  # Establecer ticks
axs[0,0].set_xticklabels(fil_rango_one['company_name'], fontsize=6)


# Gráfico de compañía de taxi con viajes en rango de 51 a 1000

axs[0,1].bar(fil_rango_two['company_name'],fil_rango_two['trips_amount'], color='hotpink')
axs[0,1].set_ylabel('Número de viajes')
axs[0,1].set_title('Viajes por cada compañía de taxi (En rango de 51 a 1000)')
axs[0,1].tick_params(axis='x')
axs[0,1].tick_params(axis='x', rotation=45)  # Rotar etiquetas
axs[0,1].set_xticks(range(len(fil_rango_two['company_name'])))  # Establecer ticks
axs[0,1].set_xticklabels(fil_rango_two['company_name'], fontsize=6)

# Gráfico de compañía de taxi con viajes en rango de 1001 a 6000

axs[1,0].bar(fil_rango_three['company_name'],fil_rango_three['trips_amount'], color='hotpink')
axs[1,0].set_ylabel('Número de viajes')
axs[1,0].set_title('Viajes por cada compañía de taxi (En rango de 1001 a 6000)')
axs[1,0].tick_params(axis='x')
axs[1,0].tick_params(axis='x', rotation=45)  # Rotar etiquetas
axs[1,0].set_xticks(range(len(fil_rango_three['company_name'])))  # Establecer ticks
axs[1,0].set_xticklabels(fil_rango_three['company_name'], fontsize=6)

# Gráfico de compañía  de taxi con viajes en rango de 6001 a 20000

axs[1,1].bar(fil_rango_four['company_name'],fil_rango_four['trips_amount'], color='hotpink')
axs[1,1].set_ylabel('Número de viajes')
axs[1,1].set_title('Viajes por cada compañía de taxi (En rango de 6001 a 20000)')
axs[1,1].tick_params(axis='x')
axs[1,1].tick_params(axis='x', rotation=45)  # Rotar etiquetas
axs[1,1].set_xticks(range(len(fil_rango_four['company_name'])))  # Establecer ticks
axs[1,1].set_xticklabels(fil_rango_four['company_name'], fontsize=6)


# Ajustar el diseño
plt.tight_layout()
plt.show()


print('\n')
print('******Comentarios sobre gráficos de Compañías de taxi y numero de viajes******')
print(""" Podemos observar que las 9 principales compañías con más recorridos son:

- Flash Cab
- Taxi Affiliation Services
- Medallion Leasing
- Yellow Cab
- Taxi Affiliation Services Yellow
- Chicago Carriage Cab Corp
- City Service
- Sun Taxi
- Star North Management LLC

Se observa que estas compañías dominan el número de recorridos en la ciudad, el número de recorridos es muchisimo mayor comparación a otras.
Podemos ver que entre todas las compañías hay una variaciones significativas de recorridos, ya que podemos observar con menos de  40 recorridos.
""")

# Crear grafico de barras (Los 10 principipales barrios en términos de finalización del recorrido)

df_filtro_ten.plot(kind='bar', x='dropoff_location_name', y='average_trips', color='hotpink', figsize=(10, 5), legend=False)

# Añadir títulos y etiquetas
plt.title('Principipales barrios en términos de finalización del recorridos')
plt.xlabel('Nombre de los Barrios')
plt.ylabel('Recorridos')

# Mostrar el gráfico
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
plt.tight_layout()  # Ajustar el diseño
plt.ylim(0,20000)
plt.show()

print('\n')
print('******Comentarios sobre gráfico de los 10 principipales barrios en términos de finalización del recorrido******')
print(""" Podemos observar que los 4 principales barrios con mayor términos de finalización del recorrido son:
      
-Loop
-River North
-Streeterville
-West Loop

Entre 5000 a 10000 recorridos, mientras que los otros barrios estan por debajo de los 5000 recorridos.

""")



print('\n')
#Imprimir información general del Dataframe df_weather
print('Información general del dataframe:')
print('\n')
df_weather.info()
print('\n')

# Verificar las primeras filas del Dataframe
print('\nPrimeras filas del dataframe:')
print('\n')
print(df_weather.head())


print('\n')
print('Hipótesis')
print("""
        
Hipótesis nula Nula (H₀): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare los sábados lluviosos(Bad) es igual a la duración promedio en los sábados no lluviosos (Good).

Hipótesis alternativa(H₁): La duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare los sábados lluviosos(Bad) es diferente a la duración promedio en los sábados no lluviosos(Good).

Nivel de significancia: α = 0.05"""

)

print('\n')

# Convertir start_ts a datatime
df_weather['start_ts'] = pd.to_datetime(df_weather['start_ts'])

# Extrar el dia, mes y año de fecha
df_weather['day'] = df_weather['start_ts'].dt.day_name()  # Día de la semana
df_weather['month'] = df_weather['start_ts'].dt.month  # Mes
df_weather['year'] = df_weather['start_ts'].dt.year  # Año


print(df_weather)
print('\n')

# Evaluar valores unicos de dia de la semana en campos de fecha
day_unique = sorted(df_weather['day'].unique())
print('Dias unicos de la semana del dataframe:', day_unique)
print('\n')

# Evaluar valores unicos del mes en campos de fecha
month_unique = sorted(df_weather['month'].unique())
print('Mes unico de nuestro dataframe:', month_unique)
print('\n')

# Evaluar valores unicos del año en campos de fecha
year_unique = sorted(df_weather['year'].unique())
print('Año unico de nuestro dataframe:', year_unique)
print('\n')


# Evaluar valores unicos en las condiciones del clima en el dataframe
conditions = sorted(df_weather['weather_conditions'].unique())
print('Condiciones del clima en dataframe:', conditions)
print('\n')

# Filtramos de nuestro dataframe los campos que nos interesa
weather_filtro = df_weather.loc[:, ['weather_conditions','duration_seconds','day']]
print(weather_filtro)
print('\n')


# Filtramos duration seconds por Good 
saturday_good = weather_filtro.query('weather_conditions == "Good"')['duration_seconds']

# Filtramos duration seconds por Bad
saturday_bad = weather_filtro.query('weather_conditions == "Bad"')['duration_seconds']

# Ordenar la serie de Good y Bad
saturday_good_conditions = saturday_good.sort_values().reset_index(drop=True) 
saturday_bad_conditions = saturday_bad.sort_values().reset_index(drop=True) 
print('\n')


# Promedio Good
mean_good = round(saturday_good_conditions.mean(),2) #Redondear usando solo 2 decimales
print('Duración Promedio en conditions Good:', mean_good)


# Promedio Bad
mean_bad = round(saturday_bad_conditions.mean(),2) #Redondear usando solo 2 decimales
print('Duración Promedio en conditions Bad:', mean_bad)

print('\n')

# Contar cantidad de registros de Good y Bad
print('Cantidad de registros recorridos cuando la condicion es Goood:',saturday_good_conditions.count())
print('Cantidad de registros recorridos cuando la condicion es Bad:',saturday_bad_conditions.count())



print('\n')
# Realizar la prueba t de Student
resultado = stats.ttest_ind(saturday_good_conditions, saturday_bad_conditions)

t_statistic, p_value = stats.ttest_ind(saturday_good_conditions,saturday_bad_conditions,equal_var=True)

# Resultados
print('Estadística t:', t_statistic)
print('\n')
print('Valor p:', p_value)
print('\n')

# Interpretar los resultados
alpha = 0.05
if p_value < alpha:
    print("Rechazamos la hipótesis nula, la duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare los sábados lluviosos(Bad) es diferente a la duración promedio en los sábados no lluviosos(Good).")
else:
    print("No podemos rechazar la hipótesis nula, la duración promedio de los viajes desde el Loop hasta el Aeropuerto Internacional O'Hare los sábados lluviosos(Bad) es igual a la duración promedio en los sábados no lluviosos (Good).")
    
print('\n')


# Crear grafico de barras para condiciones del tiempo Good y Bad

df = pd.DataFrame(weather_filtro)

# Calcular la suma de duración por condición climática
weather_duration = df.groupby("weather_conditions")["duration_seconds"].mean()

# Crear el diagrama de barras
plt.figure(figsize=(8, 5))
weather_duration.plot(kind='bar', color=['skyblue', 'lightcoral'])

# Añadir etiquetas y título
plt.title("Duración total por condición climática", fontsize=14)
plt.xlabel("Condiciones climáticas", fontsize=12)
plt.ylabel("Duración total (segundos)", fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

print("""
 Conclusión: Podemos concluir que cuando la condiciones del clima cuando son "Bad", afecta de manera significativamente a la duración de los recorridos (siendo mucho mayor), esto tambien
 podemos observar afecta en la cantidad de recorridos que se realizan de igual manera, para el dia sabado en condiciones con "Bad", se realizaron 180 recorridos, mienstras
 que condiciones de "Good", se realizaron 888.
"""
)
