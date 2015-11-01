
"""
    randomportfolio
    Random Portfolio: A random covariance generator for portfolio optimization
    :author: Sertalp B. Cay    
"""

import argparse


def saveToFile():
    """ Saves the resulting matrix as a space separated file """    
    print "Saving to file..."

def eveeMode():
    """ Generates the root vector L by using ev - \bar{e} method """
    print "Generating root..."



def parseInfo():
    """ Takes the user input and parse parameters """
    print "Parsing info..."
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", type=int, help="increase output verbosity")
    parser.add_argument("-a", "--asset", type=int, help="number of assets", required=True)
    parser.add_argument("-s", "--seed", type=int,  help="seed number", default=42)
    parser.add_argument("-e", "--param_e", help="the e parameter for the method", default=0.002)
    args = parser.parse_args()
    
def main():
    """ The main method calls parsing, generation and printing subroutines.
    """
    parseInfo()
    eveeMode()
    saveToFile()

if __name__ == '__main__':
    print "Random Portfolio\n----------------"
    main()
    print "All done!"
