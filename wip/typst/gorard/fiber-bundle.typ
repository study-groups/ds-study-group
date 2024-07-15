#set document(author: "Your Name", title: "Your Title")
#set page(paper: "us-letter")

#align(center)[
  #text(size: 24pt, weight: "bold", fill: black)[Introduction to Fiber Bundles]
  #v(10pt)
  #link("https://x.com/getjonwithit")[#text(weight: "bold", fill: blue)[Jonathan Gorard]]
]
// Set all links to be bold and blue
#show link: it => [#text(weight: "bold", fill: blue)[#it]]

#let audioExample = [
  #link("https://www.youtube.com/watch?v=nvH2KYYJg-o&t=506s")[
    #image("graphical-score-with-tagent-space.png", width: 80%)
  ]
]

#grid(
  columns: (auto, auto),
  gutter: 20pt,
)


#let tweetImg = [
  #rect(
    fill: rgb("#f0f0f0"),
    width: 200pt,
    height: 80pt,
    radius: 5pt
  )[
    #grid(
      columns: (50pt, auto),
      gutter: 10pt,
      [#rect(
        fill: rgb("#cccccc"),
        width: 50pt,
        height: 50pt
      )],
      [#align(left)[
        #text(weight: "bold")[Jonathan Gorard]
        #linebreak()
        \@getjonwithit
        #v(5pt)
        #link("https://x.com/getjonwithit/status/1810017994908594385")[Read on X]
      ]]
    )
  ]
]

#tweetImg




Fibrations/bundles/sections/etc. are slightly opaque-sounding terms for an otherwise very intuitive idea: that you can parameterize a collection of spaces in terms of points from a different space, and then assemble new spaces out of points taken from that collection... (1/15)

Take the simple example of a curve on a 2D plane. That curve is a 1D space, and at every point along it there is a line (i.e. a different 1D space) that is tangent to it. *So we can say that the collection of tangent lines is parameterized by the points on the curve.* (2/15)

This is a simple example of a tangent bundle: the underlying curve is called the base space, the tangent lines are called the tangent spaces, and if we imagine "gluing" all of those tangent lines together, we obtain a higher-dimensional (2D) space called the total space. (3/15)

The fact that it's possible to "glue" the tangent spaces together to form a space of the same basic "kind" as the base space is a non-trivial fact: such a gluing is known as a connection on the tangent bundle (and, in general, there exist many different possible ones). (4/15)

In much the same way, you can take a curved 2D surface as the base space, take 2D tangent planes at every point, and then glue those tangent planes together to form a 4D total space of the resulting tangent bundle. Tangent bundles are examples of vector bundles... (5/15)

...because the spaces being parameterized (i.e. the tangent spaces) are all vector spaces. The more general case, where the spaces being parameterized are arbitrary topological spaces, is known as a fiber bundle (with the spaces being parameterized known as fibers). (6/15)

A famous example is the Hopf fibration, whose base space is a 2-sphere (i.e. an ordinary sphere in 3D), whose fibers are 1-spheres (i.e. circles), and whose total space is a 3-sphere (i.e. a hypersphere in 4D). It can be generalized naturally to several higher dimensions. (7/15)

All of these examples so far are known as trivial bundles, because the vector spaces/fibers are all "the same", e.g. all of the tangent spaces to a manifold are isomorphic as vector spaces. So the total space is diffeomorphic. That is, any tangent space can be smoothly transformed into another. (8/15)

But you can have non-trivial bundles too (where the fibers are not all the same, and so the total space is not given by a simple product space). Once a bundle structure has been defined, it becomes possible to define things like vector and tensor fields in terms of it. (9/15)

What is a vector field? Well, it's an assignment of a vector to each point in some space (where a vector is just a point in a vector space). So we're really constructing a tangent bundle on a space, and then selecting a distinguished point from each fiber of that bundle. (10/15)

This operation (of assembling a new space by selecting a distinguished point from each fiber in a bundle) is called taking a (global) section of that bundle. So the collection of possible vector fields on a space is just the collection of sections of its tangent bundle. (11/15)

Typically we want our vector fields to be smooth (i.e. infinitely differentiable in each component), so we consider the collection of smooth sections of the tangent bundle. What about a (smooth) covector field? Well that's just a (smooth) section of the cotangent bundle. (12/15)

What about a higher-rank tensor field? Well, rather than selecting one distinguished point from each tangent space, we might want to select two (for a rank-2 contravariant tensor field), or perhaps two from its cotangent space (for a rank-2 covariant tensor field), etc. (13/15)

But actually these are all (smooth) sections too, just of a higher-rank vector bundle whose fibers are given by tensor products of (several copies of) the tangent and cotangent spaces, because all tensors are really just "vectors" (in the sense of forming a vector space). (14/15)

I'm mostly posting this as a prelude to talking about some really beautiful bits of symplectic geometry (and associated classical mechanics) that I've been thinking about recently. But there's a subtle beauty to some of this underlying structure too... (15/15)

#audioExample


= First part: Fibrations, Bundles, and Sections

The tweet discusses the concepts of #link("https://en.wikipedia.org/wiki/Fibration")[fibrations], #link("https://en.wikipedia.org/wiki/Fiber_bundle")[bundles], and #link("https://en.wikipedia.org/wiki/Section_(fiber_bundle)")[sections], explaining them through intuitive examples. It starts with the idea that you can parameterize a collection of spaces using points from another space. For instance, a curve on a 2D plane (a 1D space) has a tangent line at each point, forming a collection of tangent lines parameterized by the curve's points. This forms a tangent bundle, where the curve is the base space, and the tangent lines are the tangent spaces. When "glued" together, these tangent lines create a higher-dimensional total space.

The concept extends to 2D surfaces, where tangent planes at each point form a 4D total space when glued together, creating a tangent bundle that is a specific type of #link("https://en.wikipedia.org/wiki/Vector_bundle")[vector bundle]. In more general terms, a #link("https://en.wikipedia.org/wiki/Fiber_bundle")[fiber bundle] involves parameterizing arbitrary topological spaces, known as fibers. An example is the #link("https://en.wikipedia.org/wiki/Hopf_fibration")[Hopf fibration], with a 2-sphere as the base space, 1-spheres as fibers, and a 3-sphere as the total space.

Trivial bundles have fibers that are all "the same," making the total space #link("https://en.wikipedia.org/wiki/Diffeomorphism")[diffeomorphic], whereas non-trivial bundles have varying fibers, resulting in a more complex structure. Once a bundle structure is defined, it allows for the definition of vector and tensor fields.

= Second part: Vector and Tensor Fields within Bundles

The second half of the essay delves deeper into the concept of #link("https://en.wikipedia.org/wiki/Vector_(mathematics_and_physics)")[vector] and #link("https://en.wikipedia.org/wiki/Tensor_field")[tensor fields] within the context of #link("https://en.wikipedia.org/wiki/Fiber_bundle")[bundles]. It starts by explaining that a #link("https://en.wikipedia.org/wiki/Vector_field")[vector field] is essentially an assignment of a vector to each point in a space, constructed by taking a #link("https://en.wikipedia.org/wiki/Tangent_bundle")[tangent bundle] and selecting a distinguished point from each fiber. This process is known as taking a #link("https://en.wikipedia.org/wiki/Section_(fiber_bundle)")[global section] of the bundle, and smooth vector fields are smooth sections of the tangent bundle.

The author then discusses #link("https://en.wikipedia.org/wiki/Covector")[covector fields], which are sections of the #link("https://en.wikipedia.org/wiki/Cotangent_bundle")[cotangent bundle], and higher-rank tensor fields, which involve selecting multiple points from the tangent or cotangent spaces. These are also sections, but of higher-rank vector bundles whose fibers are tensor products of the tangent and cotangent spaces.

= Summary: Fundamentals of Fiber Bundles and Differential Operators

Jonathan Gorard's discussion on fiber bundles provides a foundational understanding of how spaces can be parameterized and assembled using points from other spaces. This concept is crucial in differential geometry, where fiber bundles, such as tangent and cotangent bundles, play a significant role. Differential operators, which act on functions and sections of these bundles, are essential tools in this field. They allow for the definition and manipulation of vector and tensor fields, enabling the study of smooth structures and transformations within these parameterized spaces. Gorard's insights highlight the elegance and utility of fiber bundles in understanding complex geometric and physical phenomena.