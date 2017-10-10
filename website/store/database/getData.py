from ..models import Products, ProductDetails


def getProdNum(prNum):
    object = Products.objects.get(prodNum = prNum)
    return object.prodNum

def getProdName(prNum):
    object = Products.objects.get(prodNum = prNum)
    return object.prodName

def getProdPrice(prNum):
    object = Products.objects.get(prodNum = prNum)
    return object.prodPrice

def getProdStock(prNum):
    object = Products.objects.get(prodNum = prNum)
    return object.prodStock

def getProdGenre(prNum):
    object = ProductDetails.objects.get(prodNum = prNum)
    return object.genre

def getProdType(prNum):
    object = ProductDetails.objects.get(prodNum = prNum)
    return object.type

def getProdPublish(prNum):
    object = ProductDetails.objects.get(prodNum = prNum)
    return object.publisher

def getProdTotalPages(prNum):
    object = ProductDetails.objects.get(prodNum = prNum)
    return object.totalPages

def getProdLanguage(prNum):
    object = ProductDetails.objects.get(prodNum = prNum)
    return object.language

def getProdRating(prNum):
    object = ProductDetails.objects.get(prodNum = prNum)
    return object.rating

def getProdAuthor(prNum):
    object = ProductDetails.objects.get(prodNum = prNum)
    return object.author

def getProdDesc(prNum):
    object = ProductDetails.objects.get(prodNum = prNum)
    return object.desc

def getProdImage(prNum):
    object = ProductDetails.objects.get(prodNum = prNum)
    return object.imageLink

def getResult(query):
    object = ProductDetails.objects.raw('SELECT * FROM ProductDetails'
                                        'WHERE prodNum LIKE ' + query +
                                        'OR prodName LIKE ' + query +
                                        'OR prodPrice LIKE ' + query +
                                        'OR prodStock LIKE ' + query +
                                        'OR genre LIKE ' + query +
                                        'OR type LIKE ' + query +
                                        'OR publisher LIKE ' + query +
                                        'OR totalPages LIKE ' + query +
                                        'OR language LIKE ' + query +
                                        'OR author LIKE ' + query +
                                        'OR desc LIKE ' + query)
    return object

def getPublisherBox(publisherQuery):
  object = ProductDetails.objects.get(publisher = publisherQuery)
  return object.prodNum

def getRatingBox(ratingQuery):
  object = ProductDetails.objects.get(rating = ratingQuery)
  return object.prodNum

def getTypeBox(typeQuery):
  object = ProductDetails.objects.get(type = typeQuery)
  return object.prodNum

def getLanguageBox(languageQuery):
  object = ProductDetails.objects.get(language = languageQuery)
  return object.prodNum

def getPriceBox(priceMin, priceMax):
  object = ProductDetails.objects.raw('SELECT * FROM ProductDetails'
                                      'WHERE prodPrice >= ' + priceMin +
                                      'AND prodPrice <= ' + priceMax)
  return object.prodNum
