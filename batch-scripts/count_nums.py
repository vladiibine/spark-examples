from pyspark import SparkContext

sc = SparkContext(appName='VladsApp')

print(
        sc.parallelize([1,2,3,4,2,3,4,3,4,4,5,5,5,5,5,5,5,5,5,5]).map(lambda a: (a, 1)).reduceByKey(lambda a, b: a + b).collect()
        )

