"""
This multiplies by 10 the initia number.

I think this might get done on different nodes??? ... that's if we had any?
"""
from operator import add
import sys
from pyspark import SparkContext

sc = SparkContext(appName='VladsApp')
partitions = int(sys.argv[1]) if len(sys.argv) > 1 else 2

def f(_):
    return 1

count = sc.parallelize(range(10 * partitions), partitions).map(f).reduce(add)
print ('>>>>>VWH:::', count)
sc.stop()
