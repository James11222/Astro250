# HW 4

In this directory the solution to the homework is in the `hw_4.ipynb` notebook, but its contents are packaged into a python script. To run this script run `python estimate_pi.py` in the terminal or in a notebook. There is one optional flag argument `-n` which tells the scripty how many processes are desired in the multiprocessing/dask implementation. In the multiprocessing case it actually spawns `n` processes. For the Dask implementation it divides the number of samples into `n` chunks to process through in parallel. 

A typical use of this script would be as follows:

```python

python estimate_pi.py -n 4

```

