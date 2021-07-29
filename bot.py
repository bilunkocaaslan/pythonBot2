import requests
from bs4 import BeautifulSoup

POST_LOGIN_URL = 'http://localhost:8080/signin'

POST_HOTEL_URL = 'http://localhost/api/sejour/hotels?d=8f2fccb1&k=82e86870898db0f&s=70898db0f0c6f7532'

POST_CONTRACT_URL = 'http://localhost/api/sejour/contracts?d=8f2fccb1&k=82e86870898db0f&s=70898db0f0c6f7532'

GET_HOTEL_URL = 'http://localhost:8080/api/sejour/hotels'


payload = {
    'username': 'bilun',
	'password': '123456789'  
}


payload1 = {
        'address': "aaB",
        'category':"aaB",
        'city': "aaB",
        'code': "aaB",
        'country': "AaaB",
        'email': "AaaaB",
        'fax': "ABaaaa",
        'hotel_confirmation_types_id': "aaaB",
        'location': "AaaaaB",
        'manager': "AaaB",
        'name': "AaaaB",
       ' phone': "AaaaaaaB",
        'post_code': "ABaaa",
        'service_type_id': "ABaaa",
        'transfer_zone': "Baaaa",
        'zone': "AaaaB"
}

payload2 = {
        'address': "aaB",
        'category':"aaB",
        'city': "aaB",
        'code': "aaB",
        'country': "AaaB",
        'email': "AaaaB",
        'fax': "ABaaaa",
        'hotel_confirmation_types_id': "aaaB",
        'id': "9",
        'location': "AaaaaB",
        'manager': "AaaB",
        'name': "AaaaB",
       ' phone': "AaaaaaaB",
        'post_code': "ABaaa",
        'service_type_id': "ABaaa",
        'transfer_zone': "Baaaa",
        'zone': "AaaaB"
}

with requests.Session() as session:
    post = session.post(POST_LOGIN_URL, data=payload)
    # print(post)
    soup = BeautifulSoup(post.content, 'html.parser')
    post1 = session.post(POST_HOTEL_URL, data=payload1)
    # print(post1)
    post2 = session.post(POST_CONTRACT_URL, data=payload2)
    # print(post2)
    get1=session.get(GET_HOTEL_URL)
    soup = BeautifulSoup(get1.content, 'html.parser')
    print(soup.prettify())