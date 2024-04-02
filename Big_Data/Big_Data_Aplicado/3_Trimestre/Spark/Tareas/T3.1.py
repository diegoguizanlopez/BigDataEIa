#!/usr/bin/env python
# coding: utf-8

# hdfs dfs -mkdir datasets
# 
# hdfs dfs -put /opt/cesga/cursos/pyspark_2022/datasets datasets

# # Recoger datos

# Recogemos los datos del CSV ya en el propio hdfs diciendo que recoja también los Headers(Cabecera) y el inferSchema(La estructura de cada campo) para saber:
#    <li>Nombre de la columna</li>
#    <li>Tipo de columna</li>

# In[1]:


from pyspark.sql.functions import date_format
from pyspark.sql import SparkSession
from pyspark import SparkContext
import sys

if __name__ != '__main__':
    sys.exit(0)
spark = SparkSession \
        .builder \
        .appName('Xuwira05') \
        .getOrCreate()
sc = spark.sparkContext

df = spark.read.csv("datasets/NYC_taxi_trip_records/yellow_tripdata_2018-11.csv", header=True,inferSchema=True)
rdd = df.rdd


# Printamos el Schema para ver la estructura del CSV y recogemos de prueba los primeros X campos

# In[ ]:


df.printSchema()


# In[ ]:


df.take(10)


# Creamos la tabla en SparkSQL denominado *taxi* que irán los datos del csv a partir del DataFrame extraido

# In[3]:


df.createOrReplaceTempView('taxi')


# Hacemos una línea de prueba

# In[ ]:


spark.sql("Select * from taxi").show()


# In[ ]:


dfTime=spark.sql("Select tpep_pickup_datetime from taxi").withColumn('time',date_format('tpep_pickup_datetime','HH:mm:ss')).withColumn('date',date_format('tpep_pickup_datetime','yyyy-MM-dd'))


# In[ ]:


dfTime.show()


# # A) Contar o número de viaxes entre 00:00 e 01:00 de cada día e dar o total por día (agrupados por día, tódolos días teñen un reconto).
# 
# ## <li>Sintaxe antiga e directa con DataFrame</li>
# ## <li>Chamadas á API</li>

# In[ ]:


from pyspark.sql import Row

print("Actividad A) Contar o número de viaxes entre 00:00 e 01:00 de cada día e dar o total por día (agrupados por día, tódolos días teñen un reconto).")

dfFilter=rdd.filter(lambda x: x[2].hour==0 or (x[2].hour==1 and x[2].minute==0 and x[2].second==0)).map(lambda y: Row(tpep_pickup_datetime=y[1])).toDF()

dfFilter.withColumn('date',date_format('tpep_pickup_datetime','yyyy-MM-dd')).groupBy('date').count().sort(['date']).show()


# # B) Contar o número de viaxes entre 00:00 e 01:00 de cada día e dar o total por mes.
# 
# ## <li>Sintaxe antiga e directa con DataFrame</li>
# ## <li>Chamadas á API</li>

# In[ ]:

print("Actividad B) Contar o número de viaxes entre 00:00 e 01:00 de cada día e dar o total por mes.")

dfFilter=rdd.filter(lambda x: x[2].hour==0 or (x[2].hour==1 and x[2].minute==0 and x[2].second==0)).map(lambda y: Row(tpep_pickup_datetime=y[1])).toDF()

dfFilter.withColumn('month',date_format('tpep_pickup_datetime','MM')).groupBy('month').count().sort(['month']).show()


# # C) A media de viaxes ao mes que fai cada conductor.
# 
# ## <li>Sintaxe antiga e directa con DataFrame</li>
# ## <li>Spark SQL</li>

# In[68]:


from pyspark.sql.functions import date_format, avg

print("Actividad C) A media de viaxes ao mes que fai cada conductor.")

result = spark.sql("""
    SELECT VendorID,
           date_format(tpep_pickup_datetime, 'MM') AS date,
           COUNT(*) AS trip_count
    FROM taxi
    GROUP BY VendorID, date
""").groupBy('VendorID').agg(avg('trip_count').alias('Viajes por mes')).orderBy('VendorID')

result.show()


# # D) A media de viaxes ao día que fai cada conductor.
# 
# ## Spark SQL

# In[66]:

print("Actividad D) A media de viaxes ao día que fai cada conductor.")

spark.sql("""
    SELECT VendorID,
           AVG(trips_per_day) AS VIAJES_X_DIA
    FROM (
        SELECT VendorID,
              DATE(tpep_pickup_datetime) AS pickup_date,
               COUNT(*) AS trips_per_day
        FROM taxi
        GROUP BY VendorID, DATE(tpep_pickup_datetime)
    ) AS VIAJES_X_DIA_V
    GROUP BY VendorID
    ORDER BY VendorID
""").show()

#df.withColumn('time',date_format('tpep_pickup_datetime','yyyy-MM')).filter("time = '2018-11'").orderBy('tpep_pickup_datetime').count()


# # E) Cantos pasaxeiros foron como máximo na primeira semana do mes (nunha viaxe).
# 
# ## Spark SQL

# In[17]:

print("Actividad E) Cantos pasaxeiros foron como máximo na primeira semana do mes (nunha viaxe).")

spark.sql("""
    SELECT YEAR(tpep_pickup_datetime) as Anio,
        MONTH(tpep_pickup_datetime) as Mes,
        MAX(passenger_count) as Pasajeros
    FROM taxi
    WHERE DAY(tpep_pickup_datetime) <= 7
    GROUP BY Anio, Mes
""").show()


# # F) Cantos pasaxeiros foron como máximo en todo o mes (nunha viaxe).
# 
# ## Sintaxe antiga e directa con DataFrame

# In[59]:


print("Actividad F) Cantos pasaxeiros foron como máximo en todo o mes (nunha viaxe).")

from pyspark.sql.functions import year, month, max,min

taxi_df = df.withColumn("passenger_count", df["passenger_count"].cast("int"))

max_passengers_per_month = taxi_df.groupBy(year("tpep_pickup_datetime").alias("Anio"), month("tpep_pickup_datetime").alias("Mes")).agg(max("passenger_count").alias("Max_de_pasajeros")).orderBy(["Anio","Mes"])

max_passengers_per_month.show()


# # G) Cantos cartos costou o percorrido máis caro.
# 
# ## <li>Sintaxe antiga e directa con DataFrame</li>
# ## <li>Spark SQL</li>

# In[60]:

print("Actividad G) Cantos cartos costou o percorrido máis caro.")

max_fare = df.agg(max('fare_amount').alias('MAS_CARO'))

max_fare.show()


# In[61]:

print("G.2")

spark.sql("""
    SELECT MAX(fare_amount) AS MAS_CARO
    FROM taxi
""").show()

# In[61]:

print("G.3")

print("MAS_CARO:",rdd.max(lambda x:x[10]).__getitem__('fare_amount'))


# # H) Cantos cartos costou o percorrido máis barato.
# ## <li>Sintaxe antiga e directa con DataFrame</li>
# ## <li>Spark SQL</li>

# In[67]:

print("Actividad H) Cantos cartos costou o percorrido máis barato.")

spark.sql("""
    SELECT MIN(fare_amount) AS MAS_BARATO
    FROM taxi
""").show()


# In[ ]:

print("H.2")

min_fare = df.agg(min('fare_amount').alias('MAS_BARATO'))

min_fare.show()


# In[61]:

print("H.3")

print("MAS_BARATO:",rdd.min(lambda x:x[10]).__getitem__('fare_amount'))

if spark and sc:
    spark.stop()