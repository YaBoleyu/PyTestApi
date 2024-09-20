import CatApiRequests
import requests
cat_facts =''

def test_catFactReturnsJson():
    assert CatApiRequests.getCatFacts(cat_facts).headers["Content-Type"] == "application/json; charset=utf-8"
    print("Expected Format Code: " + "application/json; charset=utf-8" + " Actual Format Code: " + str(CatApiRequests.getCatFact(cat_facts).headers["Content-Type"]))
def test_catAmountofFacts():
    data = CatApiRequests.getCatFacts(cat_facts).json()
    expected_elements = 5
    count = 0
    data_length = len(data)
    for i in range(data_length):
        print(data[i])
        count=count+1
    assert expected_elements == count
    print("Expected Elements: "+str(expected_elements)+" Actual Elements: "+str(count))
def test_getFacts_failure():
    response = requests.get("https://cat-fact.herokuapp.com/nonexist")
    assert response.status_code ==404
    print("Expected Status Code: " + "404" + " Actual Status Code: " + str(response.status_code))
def test_getFacts_success():
    response = CatApiRequests.getCatFacts(cat_facts)
    assert  response.status_code == 200
    print("Expected Status Code: " + "200" + " Actual Status Code: " + str(response.status_code))
if __name__ == '__main__':
    CatApiRequests.getCatFacts()