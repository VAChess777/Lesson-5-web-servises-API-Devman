import requests
import pprint

# def get_vacansies_amount():
#     url = 'https://api.hh.ru/vacancies'
#
#     languages = [
#         'C#',
#         'Objective-C',
#         'Ruby',
#         'Java',
#         'С',
#         'TypeScript',
#         'Scala',
#         'Go',
#         'Swift',
#         'С++',
#         'PHP',
#         'Javascript',
#         'Python',
#         '1C',
#         'Pascal',
#         'Basic',
#         'Фортран',
#         'Perl',
#     ]
#
#     dict_vacant = {}
#     for language in languages:
#     # print(language)
#
#
#
#         payload = {
#             'text': 'Программист' + language,
#             'area': '1'
#         }
#         response = requests.get(url, params=payload)
#         response.raise_for_status()
#     # print(response.url)
#         vacancy = response.json()['found']
#         dict_vacant.update({language: vacancy})
#         # print(dict_vacant)
#     return dict_vacant
# print(get_vacansies_amount())


url = 'https://api.hh.ru/vacancies'

payload = {
    'text': 'Программист Python',
    'area': '1',
    'per_page': '20',
    'page': '0'
}
response = requests.get(url, params=payload)
response.raise_for_status()
print(response.status_code)
print(response.json()['per_page'])

id_numbers = response.json()['per_page']
print(id_numbers)
for id in range(id_numbers):
    # print(id)
    # print(response.json()['items'][id]['name'])
    print(response.json()['items'][id]['salary'])
    # print(response.json()['items'][id]['published_at'])
















# 'https://api.hh.ru/'
# # GET /vacancies/{vacancy_id}
#
#
# url = 'https://api.hh.ru/vacancies'
# payload = {
#     'text': 'Программист',
#     'area': '1',
#     'per_page': '100',
#     'page': '1'
#     # 'professional_role': '11',
#     # 'id': '96'
# }
# response = requests.get(url, params=payload)
# response.raise_for_status()
# print(response.status_code)
# print(response.url)
# print(response.json()['found'])  # 15583







# url = 'https://api.hh.ru/vacancies'
# payload = {
#     'text': 'Программист',
#     'area': '1',
#     # 'page': f'{number}'
#     # 'published_at': '2022-10-23',
#     # 'created_at': '2022-10-23'
#     # 'hhtmFrom': 'vacancy_search_list',
#     # # 'per_page': '10',
#     # 'search_period': '7'
#
# }
# response = requests.get(url, params=payload)
# response.raise_for_status()
# print(response.status_code)
# print(response.url)
# print(response.json()['found'])  # 15583
# print(response.json()['per_page'])  # 20
# print(type(response.json()['per_page']))
# print(response.json()['items'][0]['name'])
# print(response.json()['items'][0]['salary']['from'])
# print(response.json()['items'][0]['published_at'])
#
# id_numbers = response.json()['per_page']
# print(id_numbers)
# for id in range(id_numbers):
#     # print(id)
#     # print(response.json()['items'][id]['name'])
#     # print(response.json()['items'][id]['salary']['from'])
#     print(response.json()['items'][id]['published_at'])





# url = 'https://api.hh.ru/vacancies'
# payload = {
#     'text': 'Программист Python',
#
#
#     'area': '1',
#     # 'per_page': '100',
#     # 'page': '0'
#     # 'professional_role': '11',
#     # 'id': '96'
# }
# response = requests.get(url, params=payload)
# response.raise_for_status()
# print(response.url)
# print(response.json()['found'])  # 2173
# print(response.json()['pages'])  # 20
# print(response.json()['per_page'])  # 100



#     vacansies = {
#         f'{language}': vacancy
#     }
#     dict_vacant.append(vacansies)
# print(vacansies)

    # vacansies.append(vacancy)
#     vacansies = {
#         f'{language}': f'{vacancy}'
#         }
#
# print(vacansies)




# hh_url = 'https://api.hh.ru/vacancies'
# params = {
#         'area': 1,  # Код города, 1 - Москва
#         'text': 'программист ' + language,
#         'page': page  # Текущая страница поиска
#     }










# page = 0  # первая страница поиска (нумерация с 0)
# number_of_pages = 1
# vacancies = []
# while page < number_of_pages:
#     headers = {'User-Agent': 'HH-User-Agent'}
#     params = {
#         'area': 1,  # Код города, 1 - Москва
#         'text': 'программист ' + language,
#         'page': page  # Текущая страница поиска
#     }
#     response = requests.get(hh_url, headers=headers, params=params)
#     page += 1
#     try:
#         response.raise_for_status()
#     except requests.exceptions.HTTPError:
#         continue
#     response_data = response.json()
#     vacancies.extend(response_data['items'])
#     number_of_pages = response_data['pages'] - 1







# {'id': '71147159', 'premium': False, 'name': 'Программист С++ Senior', 'department': None,
#  'has_test': False, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва',
# 'url': 'https://api.hh.ru/areas/1'},
# 'salary': {'from': 400000, 'to': 700000, 'currency': 'RUR', 'gross': False},

#  'type': {'id': 'open', 'name': 'Открытая'},
#  'address': None, 'response_url': None, 'sort_point_distance': None,
#  'published_at': '2022-10-23T13:40:05+0300', 'created_at': '2022-10-23T13:40:05+0300',
#  'archived': False,
#  'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=71147159', 'insider_interview': None,
#  'url': 'https://api.hh.ru/vacancies/71147159?host=hh.ru',
#  'adv_response_url': 'https://api.hh.ru/vacancies/71147159/adv_response?host=hh.ru',
#  'alternate_url': 'https://hh.ru/vacancy/71147159', 'relations': [],
#  'employer': {'id': '9261916',
# 'name': 'Дубайт', 'url': 'https://api.hh.ru/employers/9261916', 'alternate_url': 'https://hh.ru/employer/9261916',
# 'logo_urls': {'90': 'https://hhcdn.ru/employer-logo/5694076.png', '240': 'https://hhcdn.ru/employer-logo/5694077.png',
# 'original': 'https://hhcdn.ru/employer-logo-original/1018327.png'},
# 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=9261916', 'trusted': True},
#  'snippet': {'requirement': 'Опыт коммерческой разработки на С++ от 3-х лет. Опыт работы с низкоуровневыми сетями, '
# 'многопоточностью и асинхронностью. Опыт работы с...', 'responsibility': 'Разработка приложений, работающих с '
# 'биржевой инфраструктурой. Проектирование компонентов low-latency торговой платформы.'},
#  'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
#  'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False}

# Process finished with exit code 0
























# for number in response.json()['items']:
#     for id in response.json()['items']:
#         print(id)


# for number in range(response.json()['per_page']):
#     url = 'https://api.hh.ru/vacancies'
#     payload = {
#         'text': 'Программист',
#         'area': '1',
#     # 'page': f'{number}'
#     # 'published_at': '2022-10-23',
#         'created_at': '2022-10-23',
#     # 'hhtmFrom': 'vacancy_search_list',
#         'per_page': f'{number}',
#     # 'search_period': '7'
#     }
#     response = requests.get(url, params=payload)
#     response.raise_for_status()
#
#     print(response.json()['per_page'])




#
# url = 'https://hh.ru/search/vacancy'
# response = requests.get(url)
# response.raise_for_status()
# print(response.status_code)  # requests.exceptions.HTTPError: 404 Client Error: Not Found for url:
# print(response.url)





# url = 'https://wikipedia.com'
# headers = {
#     'User-Agent': 'curl',
#     'Accept-Language': 'ru-RU',
#     'search_period': '7'
# }
#
# response = requests.get(url, headers=headers)
# response.raise_for_status()
# print(response.status_code)
# print(response.url)





# https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&ored_clusters=true&
# text=programmes&search_period=30&hhtmFrom=vacancy_search_list

# https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&ored_clusters=true&
# text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82&search_period=7&hhtmFrom=vacancy_search_list


# for name in response.json():
#     print(name)
# items
# found
# pages
# per_page
# page
# clusters
# arguments
# alternate_url
# for name in response.json():
#     print(response.json()['items'])


# params=payload

