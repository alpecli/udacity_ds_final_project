# Final project of the Data Streaming Udacity nanodegree program.
This project contains the code of the `SF Crimes Statistics with Spark Streaming` project, the final project from Udacity Data Streaming nanodegree program.
The screenshots are all located in the `screenshots.zip` file.
All source code is located in the `src` folder.
All data used in the project is located in the `data` folder.
## Questions
### Q.1 - How did changing values on the SparkSession property parameters affect the throughput and latency of the data?
 ##### A: Changing some configuration values from SparkSession allowed Spark to process Kafka messages faster, which decreased the latency of the data received.
 
 ### Q.2 - What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?
 ##### A: The most efficient properties were `spark.executor.instances`, set to `3`, and `spark.sql.shuffle.partitions`, set to `8`. Increasing the number of executors allowed to create more executors and make better use of the cores of the machine (4 core total), so that the messages could be divided into the cores instead of being concentrated in only one.
 ##### Changing the number of shuffle partitions allowed each executor to perform less tasks, decreasing the amount of data in the shuffle read process, running event faster (dicreasing the duration of a task from 8s to 0.2s).