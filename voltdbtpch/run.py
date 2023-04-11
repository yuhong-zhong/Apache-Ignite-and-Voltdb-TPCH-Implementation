from base import *
import sys

if __name__ == "__main__":
	conf = voltdbtpchconf('config.conf')

	if invalid_conf(conf):
		print("Invalid configuration")
		exit(1)
		
	conn = connection(conf)
	runner = voltdbtpchrunner(conf, conn)

	query = None
	if len(sys.argv) > 1:
		query = int(sys.argv[1])
		
	start_time = time.time()
	runner.run_queries(query)
	print("Total execution time = ", (time.time() - start_time), "seconds")

	conn.close()
