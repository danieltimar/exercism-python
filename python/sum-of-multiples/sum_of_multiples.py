def sum_of_multiples(limit, multiples):

    all_multiples = set()

    for i in multiples:
        multiples_as_iterable = range(i, limit, i)
        all_multiples.update(multiples_as_iterable)

    return sum(all_multiples)
