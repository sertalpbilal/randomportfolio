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

# MIT License

Copyright (c) [2016] [Sertalp B. Cay]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Citation

[![DOI](https://zenodo.org/badge/22332/sertalpbilal/randomportfolio.svg)](https://zenodo.org/badge/latestdoi/22332/sertalpbilal/randomportfolio)

```
@Misc{sertalp2016randomportfolio,
  Title                    = {Random Portfolio Dataset Generator},
  Author                   = {Sertalp B. \c{C}ay},
  HowPublished             = {\url{http://sertalpbilal.github.io/randomportfolio/}},
  doi = {10.5281/zenodo.53204},
  url = {http://dx.doi.org/10.5281/zenodo.53204}
}
```
