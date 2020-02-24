import nmap

"""
    This retrieves information with regards to ports on that IP Address
"""
def nmapPortScan(tgtHost: str, tgtPort: str) -> dict:
    protocolInfo = {}
    portInfo = {}

    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost,tgtPort)
    protocols = nmScan[tgtHost].all_protocols()
    for prot in protocols:
        if(nmScan[tgtHost][prot][int(tgtPort)]['state'] != "filtered"):
            protocolInfo["Port"]  = tgtPort
            protocolInfo["State"] = nmScan[tgtHost][prot][int(tgtPort)]['state']
            protocolInfo["Type"]  = nmScan[tgtHost][prot][int(tgtPort)]['name']
            protocolInfo["Product"] = nmScan[tgtHost][prot][int(tgtPort)]['product']
            protocolInfo["Version"] = nmScan[tgtHost][prot][int(tgtPort)]['version']
            portInfo[prot] = protocolInfo
            print ("[*] " + tgtHost + " tcp/"+tgtPort +" "+portInfo[prot]["State"]+" "+portInfo[prot]["Type"]+" "+portInfo[prot]["Product"]+" "+portInfo[prot]["Version"])
        else:
            protocolInfo = {}
    return portInfo

"""
    This should scan for Operating Systems
"""
# def nmapOSScan(tgtHost: str) -> str:
#     nmScan = nmap.PortScanner()
#     nmScan.scan(tgtHost,tgtPort)
#     state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
#     print ("[*] " + tgtHost + " tcp/"+tgtPort +" "+state)
#     return(state)
