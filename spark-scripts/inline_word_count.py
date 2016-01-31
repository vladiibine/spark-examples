from pyspark import SparkContext

sc = SparkContext(appName='Asdf')

print(sc.parallelize(["""asdf zxcv asdf qwer qwer 
    fdfd
    fdfd
    fff
    fff
    f
    f
    f
    f
    f
    """]).flatMap(lambda x: x.splitlines()).flatMap(lambda line: line.split(' ')).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b).collect())
print('<<<<<<<<<<<<<<<<VWH this was the result')

sc.stop()
