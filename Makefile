# Start the spark server/nodes
up:
	docker-compose up -d

# Kill the spark server/nodes
down:
	docker-compose down

# Enter spark shell
shell:
	docker-compose exec spark-master /spark/bin/pyspark

# "ssh" into the master node
ssh:
	docker-compose exec spark-master /bin/bash
