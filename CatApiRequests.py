import json

import requests
cat_facts = ""

def getCatFacts(cat_facts):
    cat_facts = requests.get("https://cat-fact.herokuapp.com/facts?animal_type=cat")
    #print(cat_facts)
    return cat_facts
def amountofCatFacts(cat_facts):

    cat_facts_data = json.dumps(cat_facts)
    print(cat_facts_data)

def getCatFact(cat_facts):
    data = getCatFacts(cat_facts).json()
    json_str = json.dumps(data[0])
    resp=json.loads(json_str)
    print(resp)
    factId= resp['_id']
    cat_fact_link = requests.get("https://cat-fact.herokuapp.com/facts/"+factId)
    print(cat_fact_link)

    return cat_fact_link
if __name__ == '__main__':
    getCatFact(cat_facts)