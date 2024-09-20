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

if __name__ == '__main__':

    print(getCatFacts(cat_facts).json())
    amountofCatFacts(cat_facts)
