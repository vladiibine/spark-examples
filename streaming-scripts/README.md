###Streaming stateful word count
The idea: this kind of works like an append only database. Will count words you give it, and will display the results, forever. You can keep giving words to the beast, and it will keep counting them

###Run it
Look in the one-liners file for how to submit this to the spark engine. 
Basically it's something like this (assuming you can get to the `spark-submit` executable like I show in this example)

``` bash
./spark-1.6.0-bin-hadoop2.6/bin/spark-submit ./streaming-scripts/streaming_word_count.py
```

Then go into another shell, open a netcat session, and type words, pressing Enter every so often. The port spark listens to, 9999, is hardcoded.

``` bash
nc 9999
```
