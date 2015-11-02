# Random Portfolio Dataset Generation

This package provides a simplified way to generate random variance-covariance matrix for portfolio optimization problems.

It follows the paper of Hirschberger et al. to generate the random matrix. The rest is shaped for my research needs, but can be modified for any purpose.

## Usage

Inside /src folder, call

```
randomportfolio.py [-h] -n ASSET -f FILENAME [-s SEED] [-e PARAM_E]
                        [-v PARAM_V] [-b PARAM_E_BAR]

Arguments:
  -h, --help            show help message and exit
  -n ASSET, --asset ASSET
                        number of assets
  -f FILENAME, --filename FILENAME
                        file name
  -s SEED, --seed SEED  seed number
  -e PARAM_E, --param_e PARAM_E
                        the e parameter for the method
  -v PARAM_V, --param_v PARAM_V
                        the v parameter for the method
  -b PARAM_E_BAR, --param_e_bar PARAM_E_BAR
                        the e-bar parameter for the method
```

## Example

```
> python randomportfolio.py -n 200 -f RD1 -s 1122015
Random Portfolio
----------------
Parsing info...
Generating root...
Saving to file...
All done!
```

Randomly generated data can be found under /data/Q, /data/M, /data/mu, and /data/P

# Reference

Hirschberger, Markus, Yue Qi, and Ralph E. Steuer. "Randomly generating portfolio-selection covariance matrices with specified distributional characteristics." European Journal of Operational Research 177.3 (2007): 1610-1625.