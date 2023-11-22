from pyspark.sql import SparkSession
import gerenciador as ger

if __name__ == "__main__":

    spark = SparkSession.builder.master("local[*]").appName("Exercicio Intro").getOrCreate()
    df_nomes = spark.read.csv("nomes_aleatorios.txt", header=False, inferSchema=True, sep="\t")
    df_nomes.show(5)

    df_nomes = df_nomes.withColumnRenamed("_c0", "Nomes")
    df_nomes.show(10)

    df_nomes = ger.criarColunaEscolaridade(df_nomes)

    df_nomes = ger.criarColunaPais(df_nomes)

    df_nomes = ger.criarColunaAnoNascimento(df_nomes)

    df_select = df_nomes.filter("AnoNascimento >= 2000")
    df_select.show(10)

    df_nomes.createOrReplaceTempView("pessoas")
    spark.sql("SELECT * FROM pessoas WHERE AnoNascimento >= 2000").show(10)

    millennials = df_nomes.select("*").filter((df_nomes["AnoNascimento"] >= 1980) & (df_nomes["AnoNascimento"] <= 1994)).count()
    print("Número de pessoas da geração Millennials:", millennials)

    millennials_sql = spark.sql("SELECT COUNT(*) AS total FROM pessoas WHERE AnoNascimento BETWEEN 1980 AND 1994").collect()[0]["total"]
    print("Número de Millennials (Spark SQL):", millennials_sql)

    df_nomes = ger.criarColunaGeracao(df_nomes)

    df_nomes.createOrReplaceTempView("pessoas_com_geracao")

    df_pessoas_por_pais_geracao = spark.sql("""
        SELECT Pais, Geracao, COUNT(*) AS Quantidade 
        FROM pessoas_com_geracao 
        GROUP BY Pais, Geracao 
        ORDER BY Pais, Geracao
    """)

    df_pessoas_por_pais_geracao.show()

    
