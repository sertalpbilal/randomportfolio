
"""
    randomportfolio
    Random Portfolio: A random covariance generator for portfolio optimization
    Generates variance-covariance matrix Q, return rates mu, batch size M and price vector P
    :author: Sertalp B. Cay    
"""

import argparse
import numpy
import math
import sys

def saveToFile():
    """ Saves the resulting matrix as a space separated file """    
    print "Saving to file..."
    numpy.savetxt('../data/Q/' + args.filename, qmatrix, delimiter='\t')
    numpy.savetxt('../data/M/' + args.filename, mvector, delimiter='\t')
    numpy.savetxt('../data/mu/' + args.filename, muvector, delimiter='\t')
    numpy.savetxt('../data/P/' + args.filename, pvector, delimiter='\t')

def eveeMode():
    """ Generates the root vector L by using ev - \bar{e} method """
    print "Generating root..."
    # Set seed
    numpy.random.seed(args.seed)
    mu, sigma = 0, 0.1 # mean and standard deviation
    m = max(1, round (( args.param_e_bar * args.param_e_bar - args.param_e * args.param_e) / args.param_v))
    e_hat = math.sqrt(args.param_e / m)
    v_hat = - math.pow(e_hat,2) + math.sqrt( math.pow(e_hat, 4) + (args.param_v / m) )
    # Generate random numbers
    randnums = numpy.random.normal(mu, sigma, args.asset*m)
    f = [ e_hat + math.sqrt(v_hat)*r for r in randnums ]
    #f = e_hat + math.sqrt(v_hat) * randnums
    f = numpy.mat(f)
    f = f.reshape(args.asset, m)
    global qmatrix
    qmatrix = numpy.dot(f, f.T)*10000
    global mvector
    mvector = numpy.random.randint(args.batch_lowerb, high=args.batch_upperb, size=args.asset)
    global muvector
    muvector = numpy.random.uniform(args.mu_lowerb, high=args.mu_upperb, size=args.asset)
    global pvector
    pvector = numpy.random.uniform(args.price_lowerb, high=args.price_upperb, size=args.asset)
    
def parseInfo():
    """ Takes the user input and parse parameters """
    print "Parsing info..."
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", type=int, help="output verbosity")
    parser.add_argument("-n", "--asset", type=int, help="number of assets", required=True)
    parser.add_argument("-f", "--filename", help="file name", required=True)
    parser.add_argument("-s", "--seed", type=int,  help="seed number", default=42)
    parser.add_argument("-e", "--param_e", type=float, help="the e parameter for the method", default=0.002)
    parser.add_argument("-v", "--param_v", type=float, help="the v parameter for the method", default=0.000004)
    parser.add_argument("-b", "--param_e_bar", type=float, help="the e-bar parameter for the method", default=0.04)
    parser.add_argument("-ml", "--mu_lowerb", type=float, help="lower bound for expected returns", default=-0.02)
    parser.add_argument("-mu", "--mu_upperb", type=float, help="upper bound for expected returns", default=0.1)
    parser.add_argument("-bl", "--batch_lowerb", type=int, help="lower bound for batch sizes", default=100)
    parser.add_argument("-bu", "--batch_upperb", type=int, help="upper bound for batch sizes", default=1000)
    parser.add_argument("-pl", "--price_lowerb", type=float, help="lower bound for asset prices", default=10)
    parser.add_argument("-pu", "--price_upperb", type=float, help="upper bound for asset prices", default=125)
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
