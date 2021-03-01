import requests
import urllib


def get_api(url):
    result = requests.get(url)
    # json形式に変更
    return result.json()


def main():

    productId = "c79426c3c98e443eefbfc26cfde6298f"
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?format=json&productId={}&applicationId=1019079537947262807".format(
        productId)

    result = get_api(url)
    # print(result)
    item_key = ['itemName', 'ProductDetails','maxPrice','minPrice']
    item_list = []
    # for i in range(len(result)):
    tmp_item = {}
    item = result['Products'][0]['Product']
    for key, value in item.items():
        if key in item_key:
            tmp_item[key] =value
    item_list.append(tmp_item)
    print(item_list)

    # for name, price in zip(data['itemName'], data['itemPrice']):
    #     print(name + ':' + price)

main()
