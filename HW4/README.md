# HW 4

In this directory the solution to the homework is in the `hw_4.ipynb` notebook, but its contents are packaged into a python script. To run this script run `python estimate_pi.py` in the terminal or in a notebook. There is one optional flag argument `-n` which tells the scripty how many processes are desired in the multiprocessing/dask implementation. In the multiprocessing case it actually spawns `n` processes. For the Dask implementation it divides the number of samples into `n` chunks to process through in parallel. The default choice of `n` is 4, and this will be chosen if the `-n` flag is not given. 

A typical use of this script would be as follows:

```
python estimate_pi.py -n 4
```

Using this code we find that as expected, the simple implementation does end up being the slowest when we have large amounts darts thrown but this is not always the case. This graph clearly shows that the gains from parallelizing our code only really become apparent after +10,000 darts have been thrown. This is because it takes a bit of time to set up the multiple processes/dask arrays initially, but once they are initiallized they can take advantage of the increased computational resources and become more effective. We see that dask is the fastest in this case, but this is to be expected because there is no `for` loops in that implementation to slow down the blazingly fast numpy/dask code. Ultimately it is important to know when parallel computing is actually necessary because it can be quite challenging to implement correctly and may not be worth it if the amount of computations is not very large.

