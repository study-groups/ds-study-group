# run ipython
# ipython> load generator.py
# ipython> <shift><enter> # to complete load command

# multiply by 100 only if x mod 2 is zero (e.g. x is divisable by 2)
[x if x % 2 else x * 100 for x in range(1, 10)]
