# 0x10. Python - Network #0

This project contains a set of Bash and Python scripts that interact with web servers using cURL and Python requests. The scripts perform various HTTP requests and demonstrate different functionalities.

## Requirements

- The scripts are designed to run on Ubuntu 20.04 LTS.
- All Bash scripts are exactly 3 lines long.
- All Python scripts use Python 3.8.5.
- Proper documentation is maintained for modules, classes, and functions.
- The complexity of the peak-finding algorithm is O(n).

## Files and Descriptions

1. **0-body_size.sh**: Displays the size of the response body in bytes for a given URL.
2. **1-body.sh**: Displays the body of the response for a 200 status code after sending a GET request to a URL.
3. **2-delete.sh**: Sends a DELETE request to a URL and displays the response body.
4. **3-methods.sh**: Displays all HTTP methods accepted by a server for a given URL.
5. **4-header.sh**: Sends a GET request with a specific header and displays the response body.
6. **5-post_params.sh**: Sends a POST request with specific parameters and displays the response body.
7. **6-peak.py**: Contains a function to find a peak in a list of unsorted integers.
8. **6-peak.txt**: Contains the complexity analysis of the peak-finding algorithm.

## Usage

To run the scripts, execute them in a terminal with the appropriate arguments. Ensure proper permissions are set for execution.

Example:

bash 
./0-body_size.sh 0.0.0.0:5000
## Testing

The scripts can be tested in the provided sandbox environment using the web server running on port 5000.

