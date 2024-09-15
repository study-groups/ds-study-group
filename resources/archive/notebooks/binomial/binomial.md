# Binomial distribution in Julia, Python and R 

## Binomial distribution


The notion of "N choose K", written ${n \choose x}$, is the number of ways to choose k elements from a set of n elements without regard to order. 

$$
{n\choose k}=\frac{n!}{(n-k)!k!}.
$$

A binomial function maps two integers, $(a,b)$ to a single integer according to:
$$
(a+b)^n=\sum_{k=0}^n{n\choose k}a^{n-k}b^k.
$$


For example, given 3 binary choices, $(1, 0, 1)$ is considered an element of the subset of possibilites that contain two $1$'s. 

| N | K | $${n \choose k}$$ | avg | Power set = $2^0$ |
----|---|-------------------|-----|-----|
| 0 | 0 | $$\frac{0!}{0!0!}= 1$$ | $$ \frac{1}{1} $$ |  There is 1 way to choose zero <br> elements from zero elements. |

| N | K | $${n \choose k}$$ | avg |  Power set = $2^1 = 2$  |
----|---|-------------------|-----|-----|
| 1 | 0 | 1 | $$\frac{1}{2^N}=\frac{1}{2^1}$$ | total possibilities = <br>power set $2^N$ |
| 1 | 1 | $\frac{1}{2}$ |  0 | 1 |


| N | K | $${n \choose k}$$ | avg | note |
----|---|----|-----|-----|
| 2 | 0 | 0 | 0 | 0 |
| 2 | 1 | $\frac{1}{2}$  | 0 | 0 |
| 2 | 2 | $\frac{1}{2}$  | 0 | 0 |

| N | K | $${n \choose k}$$ | avg | note |
----|---|----|-----|-----|
| 3 | 0 | $$\frac{6}{6} = 1$$ |$$ \frac{1}{8} $$ | 1 way to choose all 0s |
| 3 | 1 | $$\frac{6}{2} = 3$$ | $$\frac{1}{2^3}$$  | 3 ways to choose <br> 1 items from 3 items: <br> (001), (010), (100)|
| 3| 2 | $$\frac{6}{2} = 3 $$ | $$ \frac{3}{8} $$  | 3 ways to choose <br> 2 items from 3 items: <br> (011), (110), (110) |
| 3 | 3 | $$\frac{6}{6} = 1 $$ | $$ \frac{1}{8}$$ |  1 way to choose all 0s |

## Setting up Jupyter Labs on a Linux Server

<img  style="width:40%; margin-left:5em" src="https://imgur.com/9oL8WYk.png"/>

### Python

- `python3 -m venv ~/ds-dev # creates virtualenv with ~/des-dev/bin`
- `pip install plotnine`

### Julia

### R

- In Bash before calling R: `PATH=$PATH:~/ds-devbin`

- In R
```
install.packages('devtools')
devtools::install_github('IRkernel/IRkernel')
IRkernel::installspec()
```
