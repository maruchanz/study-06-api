import requests
import urllib
import pandas as pd

def get_api(url):
    result = requests.get(url)
    # json形式に変更
    return result.json()


def main():
    genreId = "503054"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?format=json&genreId={}&applicationId=1019079537947262807".format(
        genreId)

    result = get_api(url)
    # print(result)
    item_key = ['itemName', 'itemPrice','rank']
    item_list = []
    count = len(result['Items'])
    # a = result['Items'][29]['Item']
    # print(a)

    for item in result["Items"]:
        tmp_item = {}
        # print(item)
        # APIで取得するサイトの構造に従って抽出
        # item = result['Items'][i]['Item']
        tmp_item["itemName"] = item["Item"]["itemName"]      
        tmp_item["itemPrice"] = item["Item"]["itemPrice"]
        tmp_item["rank"] = item["Item"]["rank"]
        # print(item)
        # print(item.items())

        # for key, value in item.items():
        #     if key in item_key:
        #         tmp_item[key] = value
            
        
        item_list.append(tmp_item)
    print(item_list)
   
    df = pd.json_normalize(item_list)
    df.to_csv('rank_list.csv') 

main()