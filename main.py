import requests
import pprint



url = 'https://api.hh.ru/vacancies'

languages = [
    'C#',
    'Objective-C',
    'Ruby',
    'Java',
    'С',
    'TypeScript',
    'Scala',
    'Go',
    'Swift',
    'С++',
    'PHP',
    'Javascript',
    'Python',
    '1C',
]  # 14

total_data_vacansy = []
# language = 'Программист Python'
for language in languages:
    page = 0
    total_pages = 1

    while page < total_pages:
        params = {
            'text': language,
            'area': 1,
            'per_page': 100,
            'page': page
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        # print(response.status_code)
        # print(response.url)
        data_vacancies = response.json()['items']
        total_pages = response.json()['pages']
        total_data_vacansy.extend(data_vacancies)
        # total_data_vacansy.append(data_vacancies)
        # print(total_pages)
        page += 1
    # print(total_data_vacansy)


    if total_data_vacansy:
        vacancy_found = len(total_data_vacansy)
        average = []
        for id in range(vacancy_found):
            # print(id)
            vacancy_salary = total_data_vacansy[id]['salary']
            if vacancy_salary:
                salary_currency = total_data_vacansy[id]['salary']['currency']
                # print(salary_currency)
                salary_from = total_data_vacansy[id]['salary']['from']
                # print(salary_from)
                salary_to = total_data_vacansy[id]['salary']['to']
                # print(salary_to)
                if salary_currency == 'RUR':
                    if salary_from and salary_to:
                        middle_salary = int((salary_from + salary_to) / 2)
                    elif salary_from:
                        middle_salary = int(salary_from * 1.2)
                    elif salary_to:
                        middle_salary = int(salary_to * 0.8)
                    # print(middle_salary)
                average.append(middle_salary)
        # print(average)

        average_salary = int(sum(average) / len(average))
        # print(average_salary)
        vacancies_processed = len(average)
        # print(vacancies_processed)
        vacancy_statistic = {
            language: {
                "vacancies_found": vacancy_found,
                "vacancies_processed": vacancies_processed,
                "average_salary": average_salary
            }
        }
        print(vacancy_statistic)







# url = 'https://api.hh.ru/vacancies'
# languages = [
#     'C#',
#     'Objective-C',
#     'Ruby',
#     'Java',
#     'С',
#     'TypeScript',
#     'Scala',
#     'Go',
#     'Swift',
#     'С++',
#     'PHP',
#     'Javascript',
#     'Python',
#     '1C',
# ]  # 14
# full = []
# for language in languages:
#     params = {
#         'text': 'Программист' + language,
#         'area': 1,
#         'per_page': 20
#     }
#     response = requests.get(url, params=params)
#     response.raise_for_status()
#     # print(response.status_code)
#     vacancy_found = response.json()['found']
#     # print(vacancy_found)
#     item = response.json()['items']
#     # print(item)
#     average = []
#     if vacancy_found:
#         for id in range(len(item)):
#             vacancy_salary = response.json()['items'][id]['salary']
#             if vacancy_salary:
#                 salary_currency = response.json()['items'][id]['salary']['currency']
#                 salary_from = response.json()['items'][id]['salary']['from']
#                 salary_to = response.json()['items'][id]['salary']['to']
#                 if salary_currency == 'RUR':
#                     if salary_from and salary_to:
#                         middle_salary = int((salary_from + salary_to) / 2)
#                     elif salary_from:
#                         middle_salary = int(salary_from * 1.2)
#                     elif salary_to:
#                         middle_salary = int(salary_to * 0.8)
#                         # print(middle_salary)
#                     average.append(middle_salary)
#         average_salary = int(sum(average)/len(average))
#         vacancies_processed = len(average)
#         vacancy_statistis = {
#             language: {
#                 "vacancies_found": vacancy_found,
#                 "vacancies_processed": vacancies_processed,
#                 "average_salary": average_salary
#             }
#         }
#         full.append(vacancy_statistis)
# print(full)



# def get_vacansies_amount(languages, url):
#
#     dict_vacant = {}
#
#     for language in languages:
#         payload = {
#             'text': 'Программист' + language,
#             'area': '1'
#         }
#         response = requests.get(url, params=payload)
#         response.raise_for_status()
#         # print(response.url)
#         vacancy = response.json()['found']
#         # print(vacancy)
#         dict_vacant.update({language: vacancy})
#     print(dict_vacant)
#     return dict_vacant
#
#
#
#
# def get_statistic_salaries(languages, url, vacancy, language):
#     statistic = []
#     # for language in languages:
#         # for
#         # print(language)
#
#     statistic_salaries = {
#         language: {
#             'vacancies_found': vacancy
#         }
#     }
#     # statistic.append(statistic_salaries)
#
#
#     print(statistic_salaries)
#
#
#
# def main():
#     url = 'https://api.hh.ru/vacancies'
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
#     ]   # 18
#     vacancy = get_vacansies_amount(languages, url)
#
#
#     # print(get_vacansies_amount(languages, url))
#     language = get_vacansies_amount(languages, url)
#     # print(language)
#     (get_statistic_salaries(languages, url, vacancy, language))
#     # print(get_vacancies_from_hh(languages))
#     # middle_salary = predict_rub_salary()
#     # print(middle_salary)
#
#
# if __name__ == '__main__':
#
#     main()

