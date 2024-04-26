import httpx
from selectolax.parser import HTMLParser


def get_data(store, url, selector):
    resp = httpx.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0"
        },
    )
    html = HTMLParser(resp.text)
    price_element = html.css_first(selector)
    price = price_element.text().strip() if price_element else "Price not found"
    return {"store": store, "price": price}


def main():
    results = [
        get_data(
            "Daraz",
            "https://www.daraz.com.bd/products/t900-8-i355772340-s1750012930.html?spm=a2a0e.searchlistcategory.sku.5.47da6e86RPdbcP&search=1",
            "span.pdp-price"
        ),
        get_data(
            "Thomann",
            "https://www.thomann.de/gb/shure_sm_7b_studiomikro.htm",
            "div.productpage-price"
        ),
    ]
    print(results)


if __name__ == "__main__":
    main()
