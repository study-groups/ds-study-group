#import "@preview/cetz:0.2.2": canvas, plot

#let f(x) = calc.exp(-calc.pow(x, 2))
#let T1(x) = 1 - calc.pow(x, 2)
#let T2(x) = 1 - calc.pow(x, 2) + calc.pow(x, 4) / 2
#let T3(x) = 1 - calc.pow(x, 2) + calc.pow(x, 4) / 2 - calc.pow(x, 6) / 6

= Power Series

A power series is a fundamental concept in mathematics, representing an infinite sum of terms where each term is a constant multiplied by a variable raised to a non-negative integer power. The general form of a power series centered at x = a is:

$ sum_(n=0)^infinity c_n (x - a)^n $

where $c_n$ are constants called the coefficients of the series, and $a$ is the center of the series.

== Taylor Series

A Taylor series is a specific type of power series that represents a function as an infinite sum of terms calculated from the function's derivatives at a single point. For a function f(x) that is infinitely differentiable at a point a, its Taylor series is:

$ f(x) = sum_(n=0)^infinity (f^(n)(a))/(n!) (x-a)^n $

where $f^(n)(a)$ represents the nth derivative of f evaluated at point a.

== Application to the Gaussian Function

An important application of power series is in representing the Gaussian function. The function $f(x) = e^(-x^2)$ is significant in mathematics, particularly in probability theory and statistics. It represents the unnormalized probability density function of a Gaussian distribution with zero mean and unit variance.

The Taylor series expansion of this function around x = 0 provides a power series representation:

$ e^(-x^2) = 1 - x^2 + (x^4)/2! - (x^6)/3! + (x^8)/4! - ... $

This expansion allows us to approximate and analyze the Gaussian function using polynomial terms, demonstrating the practical utility of power series in mathematical analysis.

#pagebreak()

= Power Series and Topological Data Analysis

Power series, particularly Taylor series, provide a link between a function and its derivatives. This connection can be leveraged in topological data analysis (TDA), where derivatives play a crucial role in boundary extraction.

== Power Series and Derivatives

Recall that a Taylor series expansion of a function f(x) around a point a is given by:

$ f(x) = sum_(n=0)^infinity (f^(n)(a))/(n!) (x-a)^n $

Here, each term involves a derivative of f(x) at point a. This series effectively encodes all the local derivative information of the function into a single expression.

== Derivatives as Boundary Extractors

In TDA, derivatives are often used as boundary extractors. The key idea is that the derivative of a function highlights areas of rapid change, which often correspond to boundaries or features in data.

1. *First Derivative*: Identifies points of rapid change (potential boundaries).
2. *Second Derivative*: Highlights changes in the rate of change (curvature information).
3. *Higher Derivatives*: Provide increasingly fine-grained information about the function's behavior.

== Combining Power Series and TDA

By using the Taylor series representation, we can connect the global behavior of a function to its local derivative information:

1. *Multi-scale Analysis*: Different terms in the Taylor series correspond to different scales of analysis. Lower-order terms (involving lower derivatives) capture broad features, while higher-order terms capture finer details.

2. *Feature Extraction*: By truncating the Taylor series at different orders, we can extract features at various scales, similar to how persistent homology in TDA examines features across different scales.

3. *Boundary Detection*: The coefficients of the Taylor series (which are scaled derivatives) can be used to detect boundaries in data. Large coefficients indicate significant local changes.

4. *Smoothing and Noise Reduction*: Lower-order Taylor approximations can serve as smoothed versions of the original function, potentially helping to reduce noise in data analysis.

5. *Topological Signatures*: The sequence of Taylor coefficients can be viewed as a topological signature of the function, capturing its local behavior at increasingly fine scales.

== Example: Gaussian Function

Consider our earlier example, $f(x) = e^(-x^2)$. Its Taylor series is:

$ e^(-x^2) = 1 - x^2 + (x^4)/2! - (x^6)/3! + (x^8)/4! - ... $

In TDA, we might use this function as a kernel for smoothing data. The Taylor series allows us to understand how this smoothing behaves at different scales:

- The constant term (1) represents the global average.
- The quadratic term (-x^2) captures the primary Gaussian "bell" shape.
- Higher-order terms refine the shape, particularly near the tails.

By analyzing how topological features persist as we include more terms, we gain insight into the multi-scale structure of data smoothed by this Gaussian kernel.

#align(center)[
  #figure(
    canvas({
      plot.plot(
        size: (10, 7.5),
        x-label: "x",
        y-label: "f(x)",
        x-min: -3,
        x-max: 3,
        y-min: 0,
        y-max: 1,
        {
          // Original function
          plot.add(
            f,
            domain: (-3, 3),
            samples: 100,
            label: "f(x)",
            style: (stroke: blue)
          )
          // T1 approximation
          plot.add(
            T1,
            domain: (-3, 3),
            samples: 100,
            label: "T1",
            style: (stroke: red)
          )
          // T2 approximation
          plot.add(
            T2,
            domain: (-3, 3),
            samples: 100,
            label: "T2",
            style: (stroke: orange)
          )
          // T3 approximation
          plot.add(
            T3,
            domain: (-3, 3),
            samples: 100,
            label: "T3",
            style: (stroke: green)
          )
        }
      )
    }),
    caption: "Graph of f(x) = e^(-x^2) and its Taylor polynomial approximations"
  )
]

== Properties

1. *Symmetry*: The function is symmetric about the y-axis, meaning $f(x) = f(-x)$ for all x.

2. *Maximum*: The function reaches its maximum value of 1 at x = 0.

3. *Decay*: As |x| increases, the function rapidly approaches 0.

4. *Integral*: The integral of this function over the entire real line is equal to $sqrt(pi)$, which is fundamental in probability theory.

== Applications

This function appears in various fields:

- *Probability Theory*: It forms the kernel of the normal distribution.
- *Signal Processing*: Used in Gaussian filters for noise reduction.
- *Quantum Mechanics*: Appears in the wavefunction of the quantum harmonic oscillator.
- *Heat Transfer*: Describes temperature distribution in certain scenarios.

The power series representation allows for efficient computation and analysis of this function in these and many other applications.



== Boundary Operator and Product Rule

The boundary operator $delta$ acts on spaces, similar to differentiation acting on functions. For spaces $A$ and $B$:

$delta(A times B) = (delta A times B) union (A times delta B)$

This resembles the product rule for differentiation:

$diff/(diff x)(f(x)g(x)) = f'(x)g(x) + f(x)g'(x)$

== Lists and Geometric Series

Define a deletion operator $D$ on lists. For a list of $n$ elements $x^n$:

$D(x^n) = n x^(n-1)$

Let $L$ represent all finite lists. We can express $L$ as:

$L = 1 + x L$

Solving for $L$:

$L = 1/(1 - x)$

This is the geometric series:

$1/(1 - x) = 1 + x + x^2 + x^3 + ...$

Interpreting this in terms of lists:
- $1$: empty list
- $x$: list with one item
- $x^2$: list with two items
- ...and so on

This demonstrates how concepts from calculus (derivatives, Taylor series) can appear in computer science contexts, specifically in analytic combinatorics.

