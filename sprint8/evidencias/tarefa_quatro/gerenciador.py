from pyspark.sql.functions import rand, when, element_at, lit, expr, col

def criarColunaEscolaridade(df):
    return df.withColumn("Escolaridade", 
        when(rand() <= 0.33, "Medio")
        .when(rand() <= 0.66, "Superior")
        .otherwise("Fundamental"))

def criarColunaPais(df):
    america_do_sul = ["Brasil", "Argentina", "Colômbia", "Chile", "Peru", "Venezuela", "Equador", "Bolívia", 
        "Paraguai", "Uruguai", "Guiana", "Suriname", "Guiana Francesa"]

    return df.withColumn("Pais", element_at(lit(america_do_sul), 
        (rand() * len(america_do_sul)).cast("int") + 1))

def criarColunaAnoNascimento(df):
    return df.withColumn("AnoNascimento", expr("CAST((RAND() * (2010 - 1945) + 1945) AS INT)"))

def criarColunaGeracao(df):
    return df.withColumn("Geracao",
        when((col("AnoNascimento") >= 1944) & (col("AnoNascimento") <= 1964), "Baby Boomers")
        .when((col("AnoNascimento") >= 1965) & (col("AnoNascimento") <= 1979), "Geração X")
        .when((col("AnoNascimento") >= 1980) & (col("AnoNascimento") <= 1994), "Millennials")
        .when((col("AnoNascimento") >= 1995) & (col("AnoNascimento") <= 2015), "Geração Z")
        .otherwise("Outros"))
