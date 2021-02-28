import requests
import urllib


def get_api(url):
    result = requests.get(url)
    # json形式に変更
    return result.json()


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170426?format=json&keyword={}&applicationId=1019079537947262807&maxPrice".format(
        keyword)

    result = get_api(url)
    print(result)
    # item_key = ['itemName', 'itemPrice','maxPrice','minPrice']
    # item_list = []

    # for i in range(len(result)):
    #     tmp_item = {}
    #     item = result['Items'][i]['Item']
    #     for key, value in item.items():
    #         if key in item_key:
    #             tmp_item[key] =value
    #     item_list.append(tmp_item)
    #     print(item_list)
    





    # for name, price in zip(data['itemName'], data['itemPrice']):
    #     print(name + ':' + price)

main()
