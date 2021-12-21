
# Port Scanner
Scan web/server hosts and identify open ports. This service allows for multiple port scans using a queue to store all current requested scans. It will also allow for ip range scanning on a local/public network. 

# Features
1. Scan host with parameters for port ranges

# Queue Based Implementation
The port scanner service will allow for multiple scans by using a "queue" to store backlogged scans. It will prioritize scans that will take less time based off the port ranges selected. For faster scan time, it should prioritize smaller port ranges.

## Scan Model
This is the data structure that will be added to the queue each time. 

**Username**: Person whose doing the scan
**Hostname**: Host that's being scanned
**StartPort**: Start Port range
**EndPort**: End port range

### Create Scan
1. Creates an instance of a scan
2. Will create the data structure of the model above
3. Once the scan is created, it should be ready to add to the queue

### Queue Scan
1. When the user runs the **!port_scan** command, it will add it to the queue
2. User can keep adding scans to the queue
3. Scans can't have ranges greater than 1-65535
4. Should alert the user and let them know that the scan has been added to the queue

### Run Scans
1. Goes through all the scanner objects in the queue
	* Runs each scan and sends a progress message back to the user that requested it. 
2. Once the scan is done, send results back to designated user and dequeue's
	
### Get Current Scan
1. Return the current scan in the queue
2. Reports how many more scans are in the queue
3. Would be cool if there was a time estimate

### View Scans
1. Shows all the current scans in the queue
2. Should show it in order

### Threaded scan
1. Implement multithreading to create faster scan times
	* Split ranges into sections and scan multiple ports at the same time
	* Create 2-4 threads per scan to avoid scanning the range linearly
