#different options to use with python random module
random.choice(seq)
Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.

random.choices(population, weights=None, *, cum_weights=None, k=1)
Return a k sized list of elements chosen from the population with replacement. If the population is empty, raises IndexError.

If a weights sequence is specified, selections are made according to the relative weights. Alternatively, if a cum_weights sequence is given, the selections are made according to the cumulative weights (perhaps computed using itertools.accumulate()). For example, the relative weights [10, 5, 30, 5] are equivalent to the cumulative weights [10, 15, 45, 50]. Internally, the relative weights are converted to cumulative weights before making selections, so supplying the cumulative weights saves work.

If neither weights nor cum_weights are specified, selections are made with equal probability. If a weights sequence is supplied, it must be the same length as the population sequence. It is a TypeError to specify both weights and cum_weights.

The weights or cum_weights can use any numeric type that interoperates with the float values returned by random() (that includes integers, floats, and fractions but excludes decimals). Weights are assumed to be non-negative and finite. A ValueError is raised if all weights are zero.

For a given seed, the choices() function with equal weighting typically produces a different sequence than repeated calls to choice(). The algorithm used by choices() uses floating point arithmetic for internal consistency and speed. The algorithm used by choice() defaults to integer arithmetic with repeated selections to avoid small biases from round-off error.

New in version 3.6.

Changed in version 3.9: Raises a ValueError if all weights are zero.

random.shuffle(x[, random])
Shuffle the sequence x in place.

The optional argument random is a 0-argument function returning a random float in [0.0, 1.0); by default, this is the function random().

To shuffle an immutable sequence and return a new shuffled list, use sample(x, k=len(x)) instead.

Note that even for small len(x), the total number of permutations of x can quickly grow larger than the period of most random number generators. This implies that most permutations of a long sequence can never be generated. For example, a sequence of length 2080 is the largest that can fit within the period of the Mersenne Twister random number generator.

Deprecated since version 3.9, will be removed in version 3.11: The optional parameter random.