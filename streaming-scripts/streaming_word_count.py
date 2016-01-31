from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext("local[2]", "VladsStreamingWordCount")
ssc = StreamingContext(sc, 10)

lines = ssc.socketTextStream('localhost', 9999)

words = lines.flatMap(lambda line: line.split(" "))

pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

# Print the first ten elements of each RDD generated in this DStream to the console
#wordCounts.pprint()


def update_func(new, old):
    if old is None:
        old = 0
    return sum(new, old)

running_counts = pairs.updateStateByKey(update_func)
running_counts.pprint()

ssc.checkpoint('/tmp/asdf')

ssc.start()
ssc.awaitTermination()
