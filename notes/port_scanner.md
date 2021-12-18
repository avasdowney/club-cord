
# Port Scanner
Scan web/server hosts and identify open ports. This service allows for multiple port scans using a queue to store all current requested scans. It will also allow for ip range scanning on a local/public network. 

# Features
1. Scan host with parameters for port ranges
2. Create "queued" scans
	* Allow multiple scans to happen (Not at the same time)
	* Store each search in a "queue" node and perform the scans in order
3. Create a function to priortize queue's that will take less time to perform a scan
	* Can use the port ranges as an indicator for how long the search will take
	* Prioritize smaller port ranges Ex. (1, 10), (1, 255), (1, 65535)
4. Implement multithreading to create faster scan times
	* Split ranges into sections and scan multiple ports at the same time
	* Create 2-4 threads per scan to avoid scanning the range linearly
