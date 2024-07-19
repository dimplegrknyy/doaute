if inLower48(x, y):
    return lower48Point.point(x, y)
elif inAlaska(x, y):
    return alaskaPoint.point(x, y)
elif inHawaii(x, y):
    return hawaiiPoint.point(x, y)
else:
    return None
