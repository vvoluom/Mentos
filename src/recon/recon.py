from recon.scan import nmap as nm

"""
    Iterate through all the IP addresses, storing found data inside a dictionary.
"""
def main(tgtFile :str) -> dict:
    IPList = parseFile(tgtFile)  
    IPDict = scanIPS(IPList)
    
    print(IPDict)
    return IPDict

"""
    Read the file contents into a list
"""
def parseFile(tgtFile :str) -> list:
    IPList = []
    try:
        with open(tgtFile) as file:
            data = file.read()
            #Parse Contents by new line into list
            IPList = data.splitlines()
    except EnvironmentError: 
        print ("Failed to read file")

    return IPList

"""
    Get the Ports running on the current IP address
"""
def scanIPS(IPList : list) -> dict:
    IPDict = {}
    TempPorts = [80,443,8080,8443]

    for i in IPList:
        #Get a List of Ports that are either Opened or Closed, Ignore Filtered Ports
        PortList = [nm.nmapPortScan(i,str(x)) for x in TempPorts]
        #Save the ports in the dictionary under the IP key
        IPDict[i] = PortList
 
    return IPDict