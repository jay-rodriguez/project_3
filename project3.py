import urllib

# String variable named url to url that leads to access log that needs to be retrieved 
url = 'https://s3.amazonaws.com/tcmg476/http_access_log'

# Using urlretieve method to save log file to local disk 
urllib.urlretrieve(url, '/Users/juan/Desktop/http_access_localcp.log')

# Initalizing variable named 'file' and is set to local path of log filed retrieved 
file = '/Users/juan/Desktop/http_access_localcp.log'

# Initalizing variable named 'count' to 0 
# Well serve as a counter as program counts number of request in log file. Number of lines = number of request 
count = 0 

# Using open function to open file with mode 'r' used for reading 
with open(file, 'r') as f: 
# Inizalizing for loop and adding 1 to count for every line read 
	for line in f: 
		count += 1 
# Printing the total number of requests which also equals total number of lines 
print"Total number of requests:",  count






