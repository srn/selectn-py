def selectn(attr, dic):
    return reduce(lambda d, k: d.get(k) if isinstance(d, dict) else None, attr.split('.'), dic)
