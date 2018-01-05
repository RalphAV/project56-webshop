from django import template
from django.db.models import Q

from store.collections.filter import filterObjects
from ..models import Products, ProductDetails
import urllib.request, json
from ..database.getData import getProdImage, getProdName, getProdPublish, getProdPrice, getProdAuthor, getProdStock
from ..database.getData import getProdName, getProdNum, getProdPrice, getProdStock, getProdGenre, getProdType, getProdAuthor, getProdDesc, getProdImage, getProdLanguage, getProdPublish, getProdRating, getProdTotalPages, getProdData
from ..database.verifyData import verifyProdNum
from random import randint
register = template.Library()

@register.assignment_tag

def any_function():
    with urllib.request.urlopen('https://gateway.marvel.com/v1/public/comics?ts=1&format=comic&formatType=comic&noVariants=true&orderBy=-title&limit=1&apikey=144ba3e33cfbf7edd53ed87d7b64c23a&hash=2c814cdb9f5c3d39bbf973ec7fcc6c6b') as url:
        data = json.loads(url.read().decode())
        title =  data['data']['results'][0]['title']
        desc = 'description: ' + data['data']['results'][0]['description']
        count = 'pagecount: ', data['data']['results'][0]['pageCount']
        fullurl = str(data['data']['results'][0]['thumbnail']['path']) + '.jpg'
    return "{0}, {1}, {2}, {3}".format(title, desc, count, fullurl)

def getRows(getal):
    return (int(getal / 3))

@register.simple_tag()
def prodName(prodNum):
    return getProdName(prodNum)

@register.simple_tag()
def prodImageTag(prodNum):
    return getProdImage(prodNum)

@register.simple_tag()
def prodUrlTag(prodNum):
    url = "/product/" + str(prodNum)
    return url

@register.simple_tag()
def prodTitleTag(prodNum):
    return getProdName(prodNum)

@register.simple_tag()
def prodPublTag(prodNum):
    return getProdPublish(prodNum)

@register.simple_tag()
def prodPriceTag(prodNum):
    return getProdPrice(prodNum)

@register.simple_tag()
def prodAuthorTag(prodNum):
    return getProdAuthor(prodNum)

@register.simple_tag()
def prodStockTag(prodNum):
    return getProdStock(prodNum)

# Text shortener gemaak door Selim :D. Pakt helft van de text en zet daar puntjes achter (bij het eerst volgende spatie teken)

@register.simple_tag()
def textshortener(txt):
    cnt = 0
    list = []
    for i in txt:
        cnt += 1
        if i == " ":
            list.append(cnt - 1)

    lastspace = list[int(len(list) / 2)]

    return txt[:lastspace] + "..."

@register.simple_tag()
def listloop(userAuth):
    cnt = 1
    mod = 1
    txt = ""
    randomlyselectedprod = randint(1, 69)

    prodratingtxt = ""
    for r in range(getProdRating(randomlyselectedprod)):
        prodratingtxt += "<i class='fa fa-star' aria-hidden='true'></i>"

    print("This is the length of the desc: ", len(getProdDesc(randomlyselectedprod)))

    if len(getProdDesc(randomlyselectedprod)) > 550:
        proddesc = textshortener(getProdDesc(randomlyselectedprod))
        txt += """<div class="startwrap" style="border-radius: 3px"><div class="itemoftheday"><div class="itempart1"><p>Uitgelichte Product</p></div><div class="itempart2"><p>{0}</p></div></div>
            <div class="leftstart"><img src="{1}" id="zoom_05"></div>
            <div class="rightstart"><h1>{2}</h1><p style="padding-bottom: 50px;">{3}</p><a href="/product/{4}"><p id="leesmeer"><i class="fa fa-angle-double-right" aria-hidden="true"></i>Lees meer</p></a></div></div>""".format(prodratingtxt, getProdImage(randomlyselectedprod), getProdName(randomlyselectedprod), proddesc, randomlyselectedprod)
    else:
        txt += """<div class="startwrap" style="border-radius: 3px"><div class="itemoftheday"><div class="itempart1"><p>Uitgelichte Product</p></div><div class="itempart2"><p>{0}</p></div></div>
            <div class="leftstart"><img src="{1}" id="zoom_05"></div>
            <div class="rightstart"><h1>{2}</h1><p>{3}</p></div></div>""".format(prodratingtxt, getProdImage(randomlyselectedprod), getProdName(randomlyselectedprod), getProdDesc(randomlyselectedprod))

    # txt += """<div class="startwrap" style="border-radius: 3px"><div class="itemoftheday"><div class="itempart1"><p>Uitgelichte Product</p></div><div class="itempart2"><p>{0}</p></div></div>
    # <div class="leftstart"><img src="{1}" id="zoom_05"></div>
    # <div class="rightstart"><h1>{2}</h1><p>{3}</p></div></div>""".format(prodratingtxt, getProdImage(randomlyselectedprod), getProdName(randomlyselectedprod), proddesc)

    for i in range(4):
        txt += "<ul class='list'>"
        for x in range(3):
            cnt += 10
            if cnt >= 60:
                mod += 1
                cnt = mod

            prodratingtxt = ""
            for r in range(getProdRating(cnt)):
                prodratingtxt += "<i class='fa fa-star' aria-hidden='true'></i>"

            txt = txt + "<li><div class='productwrap'><a href='" + prodUrlTag(cnt) + "'><img src='" + prodImageTag(cnt) + "' id='zoom_05'></a><p class='author'>" + prodAuthorTag(cnt) + "</p><p class='name'>" + prodTitleTag(cnt) + "</p><p>{0}</p><p class='price'>€ ".format(prodratingtxt) + str(prodPriceTag(cnt)) + "</p><button name='addToCartItemBoxButton' value='" + str(cnt) + "'class='addtocart'><i class='fa fa-plus' aria-hidden='true'></i><i class='fa fa-shopping-cart' aria-hidden='true'></i></button>"
            if userAuth:
                txt = txt + "<button name='moveToWishListButton' value='" + str(cnt) +"' class='wishlist'><i class='fa fa-heart' aria-hidden='true'></i></button>"
            txt = txt + "<p class='stock'>Voorraad: " + str(prodStockTag(cnt)) + "</p></div></li>"

        txt += "</ul>"
    return txt

@register.simple_tag()
def suggesteditems(prod, type):
    object = ProductDetails.objects.raw("SELECT * FROM store_products INNER JOIN store_productdetails on store_products.\"prodNum\" = store_productdetails.\"prodNum\" WHERE \"prodName\" like '%%" + prod.split()[0].replace("'", "''") + "%%' EXCEPT SELECT * FROM store_products INNER JOIN store_productdetails on store_products.\"prodNum\" = store_productdetails.\"prodNum\" WHERE \"prodName\" = '" + prod.replace("'", "''") + "' LIMIT 3")

    txt = ""
    imgarr = []
    titlearr = []
    pricearr = []
    linkarr = []

    for i in object:
        imgarr.append(i.imageLink)
        titlearr.append(i.prodName)
        pricearr.append(i.prodPrice)
        linkarr.append(i.prodNum)

    cnt = 0

    if type == 'Manga':
        object = ProductDetails.objects.raw("SELECT * FROM store_products INNER JOIN store_productdetails on store_products.\"prodNum\" = store_productdetails.\"prodNum\" WHERE NOT \"prodName\" = '" + prod.replace("'", "''") + "' AND \"type\" = 'Manga' ORDER BY RANDOM() LIMIT 3")

        imgarr = []
        titlearr = []
        pricearr = []
        linkarr = []

        for i in object:
            imgarr.append(i.imageLink)
            titlearr.append(i.prodName)
            pricearr.append(i.prodPrice)
            linkarr.append(i.prodNum)
    elif len(titlearr) < 3 :
        object = ProductDetails.objects.raw("SELECT * FROM store_products INNER JOIN store_productdetails on store_products.\"prodNum\" = store_productdetails.\"prodNum\" WHERE NOT \"prodName\" = '" + prod.replace("'", "''") + "' ORDER BY RANDOM() LIMIT 3")

        imgarr = []
        titlearr = []
        pricearr = []
        linkarr = []

        for i in object:
            imgarr.append(i.imageLink)
            titlearr.append(i.prodName)
            pricearr.append(i.prodPrice)
            linkarr.append(i.prodNum)

    for i in range(3):
        txt += "<li><div class='suggwrap'><a href='/product/"+ str(linkarr[cnt]) +"'><img src='" + str(imgarr[cnt]) + "'></a><p>" + str(titlearr[cnt]) + "</p><p>€ " + str(pricearr[cnt]) + "</p></div></li>"
        cnt += 1
    return txt

@register.simple_tag()
def getOrder(order):
    html = ""
    for e in order:
        html += "<tr style='text-align: center;' align='center'><td style='text-align: center; border-left-width: 0; border-top-color: #ffffff; border-top-width: 1px; border-top-style: solid; border-bottom-width: 0; border-bottom-style: solid; border-bottom-color: #e0e0e0; border-left-style: solid; border-left-color: #e0e0e0; -moz-border-radius-bottomleft: 3px; -webkit-border-bottom-left-radius: 3px; border-bottom-left-radius: 3px; background-image: -moz-linear-gradient(top,  #fbfbfb,  #fafafa); padding: 18px 18px 18px 20px;' align='center'>{0}</td><td style='text-align: center; border-left-width: 0; border-top-color: #ffffff; border-top-width: 1px; border-top-style: solid; border-bottom-width: 0; border-bottom-style: solid; border-bottom-color: #e0e0e0; border-left-style: solid; border-left-color: #e0e0e0; -moz-border-radius-bottomleft: 3px; -webkit-border-bottom-left-radius: 3px; border-bottom-left-radius: 3px; background-image: -moz-linear-gradient(top,  #fbfbfb,  #fafafa); padding: 18px 18px 18px 20px;' align='center'>{1}</td><td style='border-top-color: #ffffff; border-top-width: 1px; border-top-style: solid; border-bottom-width: 0; border-bottom-style: solid; border-bottom-color: #e0e0e0; border-left-width: 1px; border-left-style: solid; border-left-color: #e0e0e0; -moz-border-radius-bottomright: 3px; -webkit-border-bottom-right-radius: 3px; border-bottom-right-radius: 3px; background-image: -moz-linear-gradient(top,  #fbfbfb,  #fafafa); padding: 18px;'>{2}</td></tr>".format(e.productNum.prodNum, prodName(e.productNum.prodNum), e.amount)
    return html

@register.simple_tag()
def getOrderNum(order):
    string = str(order.first().orderNum.orderNum)
    return string