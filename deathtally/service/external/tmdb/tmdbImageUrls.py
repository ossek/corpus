def makeFilmImgUri(baseImgUri,imgSize,posterpath):
    return '{baseImageUrl}/{size}{path}'.format(
        baseImageUrl=baseImgUri,
        size=imgSize,
        path = posterpath)


