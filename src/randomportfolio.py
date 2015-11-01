
"""
    randomportfolio
    Random Portfolio: A random covariance generator for portfolio optimization
    :author: Sertalp B. Cay    
"""

import argparse
import numpy
import math
import sys

def saveToFile():
    """ Saves the resulting matrix as a space separated file """    
    print "Saving to file..."

def eveeMode():
    """ Generates the root vector L by using ev - \bar{e} method """
    print "Generating root..."
    # Set seed
    numpy.random.seed(args.seed)
    mu, sigma = 0, 0.1 # mean and standard deviation
    randnums = numpy.random.normal(mu, sigma, args.asset*args.asset)
    m = max(1, round (( args.param_e_bar * args.param_e_bar - args.param_e * args.param_e) / args.param_v))
    e_hat = math.sqrt(args.param_e / m)
    v_hat = - math.pow(e_hat,2) + math.sqrt( math.pow(e_hat, 4) + (args.param_v / m) )
    #f = e_hat + math.sqrt(v_hat) * randnums
    print m, e_hat, v_hat
    # print f
    

def parseInfo():
    """ Takes the user input and parse parameters """
    print "Parsing info..."
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=int, help="output verbosity")
    parser.add_argument("-n", "--asset", type=int, help="number of assets", required=True)
    parser.add_argument("-s", "--seed", type=int,  help="seed number", default=42)
    parser.add_argument("-e", "--param_e", type=float, help="the e parameter for the method", default=0.002)
    parser.add_argument("-v", "--param_v", type=float, help="the v parameter for the method", default=0.000004)
    parser.add_argument("-b", "--param_e_bar", type=float, help="the e-bar parameter for the method", default=0.015)
    global args
    args = parser.parse_args()
    if args.param_e_bar <= args.param_e:
        sys.exit("parameter e-bar should be larger than parameter-e")

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
