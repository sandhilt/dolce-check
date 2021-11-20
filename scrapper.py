import scrapy


class CoffeePriceSpider(scrapy.Spider):
    name = "coffee_price_spider"
    start_urls = ['https://www.nescafe-dolcegusto.com.br/sabores']

    def parse(self, response):
        SET_SELECTOR = '.product-card'
        for product in response.css(SET_SELECTOR):
            NAME_SELECTOR = '.product-card__name--link.product-color ::text'
            IMAGE_SELECTOR = '.product-card__image img ::attr(data-src)'
            OLD_PRICE_SELECTOR = '.product-card__price--old .price ::text'
            PRICE_SELECTOR = '[data-price-type=\'finalPrice\'] .price ::text'
            INFO_SELECTOR = '.product-card__info--oos-panel-label ::text'
            INTENSITY_SELECTOR = '.product-card__intensity--score ::text'
            URL_SELECTOR = '.product-card__image--wrapper a ::attr(href)'

            intensity = product.css(INTENSITY_SELECTOR).extract_first()
            yield {
                'name': product.css(NAME_SELECTOR).extract_first().strip(),
                'image': product.css(IMAGE_SELECTOR).extract_first(),
                'old_price': product.css(OLD_PRICE_SELECTOR).extract_first(),
                'price': product.css(PRICE_SELECTOR).extract_first(),
                'info': product.css(INFO_SELECTOR).extract_first(),
                'intesity': intensity.strip() if intensity else None,
                'url': product.css(URL_SELECTOR).extract_first(),
            }
