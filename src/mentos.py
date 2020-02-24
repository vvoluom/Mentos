import optparse
import typing
from recon import recon as recon

"""
    Input should be a text file with IP Addresses
    The IP Addresses are then parsed and saved in an array.
"""
def main():
    parser = optparse.OptionParser('usage %prog '+\
                                   '-F <IP File>')
    parser.add_option('-F', dest='tgtHost', type='string',\
                      help='specify file with IP Addresses')

    (options, args) = parser.parse_args()
    

    tgtFile = options.tgtHost
    recon.main(tgtFile)

if __name__ == '__main__':
    main()