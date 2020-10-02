# spark-examples
playing with apache spark, to see what it can do and what it's good for

The `batch-scripts` directory contains python modules that calculate stuff on demand, when they are invoked.
The `streaming-scripts` directory contains modules that calculate stuff on streams, meaning they continuously update, as new data comes in


UPDATE:
$ docker-compose up
$ docker-compose exec spark-master /spark/bin/pyspark

...and you're in the pyspark shell. You can have fun starting from there
