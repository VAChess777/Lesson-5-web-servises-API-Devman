import os

import requests
from dotenv import load_dotenv
from terminaltables import AsciiTable


def get_all_info_vacancies_hh(language):
    url = 'https://api.hh.ru/vacancies'
    total_info_vacancies_hh = []
    page = 0
    total_pages = 1
    while page < total_pages:
        params = {
            'text': language,  # Programming language.
            'area': 1,  # City code, 1 - Moscow.
            'per_page': 100,  # Number of vacancies per page.
            'page': page  # Current search page.
        }
        response = requests.get(
            url,
            params=params
        )
        response.raise_for_status()
        total_pages = response.json()['pages']
        total_info_vacancies_hh.extend(response.json()['items'])
        page += 1
    return total_info_vacancies_hh


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        middle_salary = int((salary_from + salary_to) / 2)
    elif salary_from:
        middle_salary = int(salary_from * 1.2)
    elif salary_to:
        middle_salary = int(salary_to * 0.8)
    return middle_salary


def predict_rub_salary_hh(vacancy):
    rub_salary_for_hh = 0
    if vacancy['salary'] and vacancy['salary']['currency'] == 'RUR':
        salary_from = vacancy['salary']['from']
        salary_to = vacancy['salary']['to']
        rub_salary_for_hh = predict_salary(salary_from, salary_to)
    return rub_salary_for_hh


def get_hh_statistic(total_info_vacancies_hh):
    amount_vacancies = len(total_info_vacancies_hh)
    if amount_vacancies:
        middle_salaries = [
            predict_rub_salary_hh(vacancy) for vacancy in total_info_vacancies_hh
        ]
        vacancies_processed = len(middle_salaries)
        average_salary = int(sum(middle_salaries) / vacancies_processed)
        hh_statistics = {
            'vacancies_found': amount_vacancies,
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }
        return hh_statistics


def get_all_language_stat_from_hh(languages):
    statistic_hh = {}
    for language in languages:
        total_info_vacancies_hh = get_all_info_vacancies_hh(language)
        statistic_hh[language] = get_hh_statistic(total_info_vacancies_hh)
    return statistic_hh


def get_all_info_vacancies_sj(language, secret_key):
    super_job_url = 'https://api.superjob.ru/2.0/vacancies'
    page = 0
    next_page = 1
    total_info_vacancies_sj = []
    while next_page:
        headers = {'X-Api-App-Id': secret_key}
        params = {
            'keyword': language,  # Programming language.
            'town': 4,  # City id. Id: 4 - Moscow.
            'count': 5,  # Number of results per search page
            'page': page,  # Page number of the search result
            'catalogues': 48,  # Catalog number. 48 - Development, programming
            'no_agreement': 1  # Without vacancies, where the salary is by agreement
        }
        response = requests.get(
            super_job_url,
            headers=headers,
            params=params
        )
        response.raise_for_status()
        next_page = response.json()['more']
        total_info_vacancies_sj.extend(response.json()['objects'])
        page += 1
    return total_info_vacancies_sj


def predict_rub_salary_sj(vacancy):
    sj_predict_salary = 0
    salary_from = vacancy['payment_from']
    salary_to = vacancy['payment_to']
    if vacancy['currency'] == 'rub':
        sj_predict_salary = predict_salary(salary_from, salary_to)
    return sj_predict_salary


def get_sj_statistic(total_info_vacancies_sj):
    amount_vacancies = len(total_info_vacancies_sj)
    if amount_vacancies:
        middle_salaries = [
            predict_rub_salary_sj(vacancy) for vacancy in total_info_vacancies_sj
        ]
        vacancies_processed = len(middle_salaries)
        average_salary = int(sum(middle_salaries)/amount_vacancies)
        sj_statistics = {
            'vacancies_found': amount_vacancies,
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }
        return sj_statistics


def get_all_language_stat_from_sj(languages, secret_key):
    statistic_sj = {}
    for language in languages:
        total_info_vacancies_sj = get_all_info_vacancies_sj(language, secret_key)
        statistic_sj[language] = get_sj_statistic(total_info_vacancies_sj)
    return statistic_sj


def get_table(site_name, statistic):
    title = '{} Moscow----------'.format(site_name)
    if statistic:
        table_title = [[
            'Programming language',
            'Vacancies found',
            'Vacancies processed',
            'Average salary'
        ]]
        table_instance = AsciiTable(table_title, title)
        for language, language_stat in statistic.items():
            if language_stat:
                row = [language]
                for key, value in language_stat.items():
                    row.append(value)
                table_title.append(row)
        return table_instance.table


def main():
    load_dotenv()
    secret_key = os.getenv('SUPER_JOB_KEY')
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
    ]
    site_name = 'HH'
    print(get_table(site_name, get_all_language_stat_from_hh(languages)))
    site_name = 'SJ'
    print(get_table(site_name, get_all_language_stat_from_sj(languages, secret_key)))


if __name__ == "__main__":

    main()