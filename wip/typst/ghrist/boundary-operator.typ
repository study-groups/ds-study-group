#set text(font: "New Computer Modern")
#show link: it => text(fill: blue, underline(it))

#let bg-color = rgb("#1e1e1e")
#let text-color = rgb("#ffffff")
#let accent-color = rgb("#00ffff")

#let ghrist_lecture_header(
  title: "Boundary Operator Part 1",
  subtitle: "Derivative as a Boundary Extractor: Insights from Prof. Robert Ghrist",
  chapter: "Calculus Chapter 2",
  section: "Lecture 11 Bonus",
  description: "In this lecture, Prof. Robert Ghrist explores the boundary operator and its applications in topology, providing insights into an unusual instance of a product rule.",
  video_link: "@ghrist2016",
  image_path: "./calc-1-boundary.png"
) = {
  block(
    width: 100%,
    fill: bg-color,
    inset: 20pt,
    radius: 5pt,
  )[
    #align(center)[
      #text(size: 24pt, weight: "bold", fill: text-color)[#title]
    ]
    
    #v(10pt)
    
    #grid(
      columns: (auto, auto, 1fr),
      column-gutter: 20pt,
      align(top)[
        #text(size: 11pt, fill: text-color)[
          #chapter : #section
          
          #description
          
          #link(video_link)[#text(fill: accent-color)[▶ Watch Video]]
        ]
      ],
      align(top)[
        #if image_path != none [
          #image(image_path, width: 100pt)
        ]
      ]
    )
    
    #v(10pt)
    
    #line(length: 100%, stroke: 0.5pt + text-color)
    
    #align(center)[
      #text(size: 14pt, style: "italic", fill: text-color)[
        #subtitle
      ]
    ]
  ]
}

#ghrist_lecture_header()



= Lecture 11 Bonus: Patterns in Mathematics


== Boundary Operator and Product Rule

The boundary operator $delta$ acts on spaces, similar to differentiation acting on functions. For spaces $A$ and $B$:

$delta(A times B) = (delta A times B) union (A times delta B)$

This resembles the product rule for differentiation:

$diff/(diff x)(f(x)g(x)) = f'(x)g(x) + f(x)g'(x)$

  #image("./calc-1-boundary.png", width: 80%)

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

  #align(center)[
    #image("./calc-1-lists.png", width: 90%)
  ]


This demonstrates how concepts from calculus (derivatives, Taylor series) can appear in computer science contexts, specifically in analytic combinatorics.


#pagebreak()


#block(
  width: 100%,
  fill: bg-color,
  inset: 20pt,
  radius: 5pt,
)[
  #align(center)[
    #text(size: 24pt, weight: "bold", fill: text-color)[Ghrist: Boundary Operator]
  ]
  
  #v(10pt)
  
  #grid(
    columns: (auto, auto, 1fr),
    column-gutter: 20pt,
    align(left)[
      #text(size: 11pt, fill: text-color)[
        CalcGREEN 1 : Ch. 12.5 : BONUS! Boundaries & Products
        
        Let's learn about topology, where an unusual instance of a product rule emerges.
        
        #link("https://www.youtube.com/watch?v=ChyWP552mLU&list=PL8erL0pXF3JaFSMdokheNMvTa96jdc4GU&index=92")[#text(fill: accent-color)[▶ Watch Video]]
      ]
    ],
    align(left)[
      #image("./calc-green-boundary.jpg", width: 100pt)
    ]
  )
  
  #v(10pt)
  
  #line(length: 100%, stroke: 0.5pt + text-color)
  
  #align(center)[
    #text(size: 14pt, style: "italic", fill: text-color)[
      Derivative as a Boundary Extractor: Insights from Prof. Robert Ghrist
    ]
  ]
]


= Derivative as a Boundary Extractor: Insights from Prof. Robert Ghrist

The concept of a derivative is traditionally understood as a measure of how a function changes as its input changes. However, Prof. Robert Ghrist provides a more abstract perspective by viewing the derivative as a boundary extractor, which offers deeper insights, particularly in topology and differential geometry.

== Traditional View of the Derivative

The derivative of a function $f$ at a point $x$, denoted $f'(x)$, is classically defined as:

$ f'(x) = lim_(Delta x -> 0) (f(x + Delta x) - f(x))/(Delta x) $

This definition emphasizes the rate of change of $f$ with respect to $x$, representing the slope of the tangent line to the curve $y = f(x)$ at the point $(x, f(x))$.

== Derivative as a Boundary Operator

Prof. Ghrist's perspective shifts the focus from the rate of change to boundaries. In this view, the derivative can be seen as an operator that extracts boundaries from functions or differential forms.

For a smooth function $f: RR^n -> RR$, the gradient $nabla f$ is a vector field pointing in the direction of the greatest rate of increase of $f$. This gradient identifies the "edges" or "boundaries" within the domain of $f$.

Generalizing to differential forms, a differential form $omega$ on a manifold $M$ can be integrated over $k$-dimensional submanifolds of $M$. The exterior derivative $d omega$ of a $k$-form $omega$ is a $(k+1)$-form representing the infinitesimal boundaries of $omega$. Stokes' theorem states:

$ integral_(partial Sigma) omega = integral_Sigma d omega $

for any $(k+1)$-dimensional manifold $Sigma$ with boundary $partial Sigma$. Here, $d$ acts as a boundary extractor, identifying boundaries within the space of differential forms.

== Examples of Boundaries in Topology

Topology, the study of abstract spaces, frequently deals with boundaries:

1. *Disk in a Plane*: The boundary is the circle surrounding the disk.
2. *Polygon in a Plane*: The boundary is a set of edges.
3. *Solid Ball*: The boundary is the sphere enclosing the ball.
4. *Solid Cube*: The boundary consists of the six flat faces of the cube.
5. *Solid Torus*: The boundary is a two-dimensional torus, like the glazing on a donut.
6. *Path in Space*: The boundary consists of the two endpoints of the path.

== Cartesian Products and Boundaries

The product of two spaces, known as a Cartesian product, has boundaries that can be understood through a product rule for boundaries:

$ partial(A times B) = (partial A times B) + (A times partial B) $

For instance, consider a solid cylinder, the product of a disk $A$ and an interval $B$. The boundary of the cylinder includes:

- The side of the cylinder (circle $partial A$ times the interval $B$).
- The two caps (disk $A$ times the endpoints $partial B$).

== Applications in Higher Dimensions

In higher dimensions, visualizing boundaries and their interactions becomes complex. For example:

- The product of an interval with a solid cube results in a four-dimensional cube.
- The boundary of a solid cube is the sum of six squares.

== Implications and Conclusion

Viewing the derivative as a boundary extractor aligns with a broader understanding of calculus and differential geometry. This perspective emphasizes the role of derivatives in identifying and analyzing boundaries within various mathematical structures, offering deeper insights into their applications in topology and geometry.

Prof. Ghrist's interpretation highlights the versatility and foundational importance of derivatives, providing new tools and perspectives for mathematicians and scientists in diverse fields. This unifying view bridges the gap between calculus, topology, and geometry, enriching our understanding of mathematical principles.

For more information on the concepts discussed, you can refer to:

- #link("https://en.wikipedia.org/wiki/Topology")[Topology]
- #link("https://en.wikipedia.org/wiki/Derivative")[Derivative]
- #link("https://en.wikipedia.org/wiki/Gradient")[Gradient]
- #link("https://en.wikipedia.org/wiki/Differential_form")[Differential form]
- #link("https://en.wikipedia.org/wiki/Stokes%27_theorem")[Stokes' theorem]

As discussed by Ghrist in @ghrist2016, the boundary operator has significant applications in topology.
Moreover, the insights presented in @ghrist2024 provide a deeper understanding of these concepts.

#pagebreak()

#bibliography("works.bib")
@ghrist2016
@ghrist2024