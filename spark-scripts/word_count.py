from pyspark import SparkContext
import operator

sc = SparkContext(appName='VladsApp')

print(">>>>>>>>>>VWH results: \n\n\n")
print(sc.textFile('words.txt')
        .flatMap(lambda line: line.split(' '))
        .map(lambda a: (a, 1))
        .reduceByKey(operator.add).collect())
print("\n\n\n<<<<<<<<<<<<<VWH end results")
sc.stop()
