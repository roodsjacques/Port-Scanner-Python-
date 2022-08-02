# Port-Scanner-Python- by Roods Jacques

This program is a Python program that tests the given host or IP address and it would generate a
list of all the TCP Open ports within the range of 1 to 1025. 
The standard Python’s “socket” library was implemented.

If the Ports is open it would create a file and add an entry for each port number that 
is open. 
In case of any exception for instance “host is not available”, “host name would not be 
resolved” or due to any other error, it would write that exception into same file. 
it would record starting and ending date and time at the beginning and 
ending of scan accordingly and write that to the file. It would also show the total time it 
took in port scanning process.
