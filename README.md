# fuzzy-goggles
This is a test application to blacklist and get information about urls. 

# Setup
To run this app the following tools are required:
```
docker
docker-compose
python
```
It also needs access to dynamodb on AWS hence it is required to export valid "AWS_SECRET_ACCESS_KEY" and "AWS_ACCESS_KEY_ID" environment variables.

To run multiple instance[s] of the app, the following sequence of commands need to be run. In this case we are trying to run 5 instances of the app.
```
docker-compose build
docker-compose up --scale app=5 -d
```
This will bring up 5 instances of the app behind the HA proxy. Traffic will be distributed between these instances in a round-robin fashion. To scale up or down the instance of the app "docker-compose up" command can be executed repeatedly with varying number of app instances. 

For storing and retriving data it uses dynamo db, hence the need to AWS credentials. It expects a table with the name of "UrlBlacklist" which contains "url" as the primary field to already be present.

# Requests and responses

Currently there are two endpoints supported by the app.

1) Get info about a url. A request has to be sent to '/urlinfo/1' endpoint followed by the url about which information is requested. For example to request information about url 'abc.com:99/x?y=z', a GET request will have to be sent to "http://localhost/urlinfo/1/abc.com:99/x?y=z". If request doesn't suffer any unfortunate errors then the expected response would be of format
```
{
"version":"1.0"
"result":{
  "version":"1.0"
  "is_safe": <true/false>
}}
```

>The reason for two versions in the response is so that the information encapsulated in the result can change independent of the outer overall response structure. For example, outer response structure can contain a block for response-context attributes which can convey additonal information to the user, in this case only the outer verison will have to be updated without affecting the meaning conveyed by the version of result block.

2) Add a url to be blacklisted. A request can be sent to the endpoint 'blacklist/1' with a payload containing the url that needs to be blacklisted. For example, to blacklist the url 'abc.com:99/x?y=z', a POST request will be sent to "http://localhost/blacklist/1" with a payload containing `{"url":"abc.com:99/x?y=z"}`. Appropriate http codes will be returned in response.

# Running tests

In order to run tests, the following packages need to be installed:
```
pip install requests
pip install flask
pip install boto3
```

Once installed, the following command can be executed at the location of the test `python -m unittest <module>` including for integration tests.



# Thought Excercise

> One of the features that was not included in the app that I think would have greatly benefited the performance would be to have a local cache on every node running the app instance. This cache would store the result of every url either being in the blacklist or not. This would greatly help with any hot url not hitting the database layer multiple times and increasing the fanout of network calls and processing resources. The policy of eviction in the cache would be the one least recently used. We could start with a small ttl for each cache entry to prevent serving stale data. In further stages of development a service can go through the cache on each node and update the values of the cache whenever a url value is updated.

The size of the URL list could grow infinitely. How might you scale this beyond the memory capacity of the system? 

>To scale the list beyond the memory capacity I would first try to manage it by improving the footprint of each url by only storing their hashed values. After that, I would leverage the disk space. I would propose something along the lines of B-Trees which can have more reliable throughput on reads and also have redo logs to recover from crashes. A page size around 4kb will give it ample capacity for a relatively small memory footprint. If the app ends up being more write heavy than read then a LSM tree with smart management of compactation might be a consideration.

Assume that the number of requests will exceed the capacity of a single system, describe how might you solve this, and how might this change if you have to distribute this workload to an additional region, such as Europe. 

> The effective approach to this would be strategic replication and partitioning. Data can be replicated across multiple instances to provide high availability. There are papers such as dynamo that talk about theory of doing it, and databases such as cassandra implement it. Data can also be partitioned to better disrtibute the workload and improve consistency. This is easier to talk about than to actually implement and handle edge cases. We can leverage existing databases such as dyanmodb which can replicate data across multiple regions to improve response times. This can be further enhanced by understanding usage patterns and replicating certain partitions across specific regions. Along with a distributed cache this might be a feasible approach. 

* What are some strategies you might use to update the service with new URLs? Updates may be as much as 5 thousand URLs a day with updates arriving every 10 minutes.

> There are two approaches to dealing with updates.
> 1) Multiple Http Requests with a limit of, lets say, 50 urls in the payload can be sent over the network. These requests can be distributed across multiple instances to be processed and stored in the appropriate partition. This has the drawback of excessive network activity. The network activity can be reduced by using compact data encoding such as one described in protobuf.
> 2) To support large number of updates we can mandate that a file has to be provided perhaps through s3. We can partition files with indexes and assign each instance to process portion of the file. To make sure that all the urls were processed in case an instance crashed either there can be a service to monitor the processing of each partition of file, or we can maintain a structure for the partitions that have been processed.

* You’re woken up at 3am, what are some of the things you’ll look for?
> The first things I would look for are the metrics that have been collected. I would look for any spikes in metrics or anything unexpected reported in the monitoring services. Next I would look at logs aggregated to get more clues into what could have happened. Given all this information I will take steps in accordance with the team internal policy.

* Does that change anything you’ve done in the app?
> Yes, I would have to comeup with a framework on collecting metrics. I will have to also carefully design where and when the metrics should be emitted by the app.

* What are some considerations for the lifecycle of the app?
> There are internal and external considerations to have in the lifecycle of an app. Internal ones relate to having flexibility in the design of the code so that layers can be swaped, added, and changed with minimal overhead. This helps to quickly evolve by putting more work upfront. For external considerations, responses and requests need to be designed in a manner where they dont break old versions of clients, and also clients need to be designed in a way where they can be forward compatible with changes in responses. Versions in requests and responses do help with the effort where a request or response can be rejected if the version is not compatible. Lastly another consideration would be to convey clearly the design of the application to all stakeholders through detailed design documents.

* You need to deploy new version of this application. What would you do?
> I am not too certain about features supported by HAproxy, but in ELB I would first ask loadbalancer to stop sending new requests to a small percentage of the old version of services. Once the old version of services has processed the pending requests, they can be dropped by the load balancer. A small number of the new version of service can be added to ELB to make sure that they are functioning as expected. In the next stage all the older versions of services can be replaced by newer versions. Having versions in requests and responses would help with forwards and backwards compatability.
