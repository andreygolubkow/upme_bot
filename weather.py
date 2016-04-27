from grab import Grab

def weather(city,lan):
    g = Grab()
    g.setup(document_charset='utf-8')
    g.go('https://p.ya.ru/'+city)
    wstr=g.xpath('//div[@class="today-forecast"]').text_content()
    wstr=g.css_text('.temperature-wrapper')+'. '+wstr
    key='trnsl.1.1.20160427T193202Z.39c058144b8ba50d.0c06365f68745560062f765550cb7a548557ee17'
    g.go('https://translate.yandex.net/api/v1.5/tr/translate?key='+key+'&lang='+lan+'&text='+wstr)
    wstr=g.xpath_text('//text')
    return wstr