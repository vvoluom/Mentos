import pytest
import mentos.recon.scan.nmap as nmap

def test_scan_google():
    ip = "192.168.0.25"
    port = "80"
    assert nmap.nmapScan(ip,port) == "closed", "Test Failed"
