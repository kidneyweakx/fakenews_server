import requests
import json

def cofactapi(news):
    news = '"' + news + '"'
    query = """query {
    ListArticles(
        filter: { moreLikeThis: { like: %s } }
            orderBy: [{ _score: DESC }]
        first: 3
        ) {
        edges {
            node {
            # id
            text
            #hyperlinks {
            #    url
            #}
        articleReplies {
            reply {
                #id
                text
                type
                reference
            }
            }
            }
        }
    }
    }"""%(news)
    url = "https://cofacts-api.g0v.tw/graphql"
    r = requests.post(url, json={'query': query})
    r.encoding = 'utf-8'
    data = json.loads(r.text)
    try:
        label = data['data']["ListArticles"]['edges'][0]['node']['articleReplies'][0]['reply']['type']
        if label == 'RUMOR': return('FakeNews')
        elif label == 'NOT_RUMOR': return('truenews')
    except:
        return('UNKNOWN')


if __name__ == "__main__":
    print(cofactapi("楊梅是皮蛇（帶狀皰疹）的尅星...10分鐘驗完血後，女醫生確定是得了帶狀皰疹...吃了兩天的楊梅後，居然神經不痛康復了"))