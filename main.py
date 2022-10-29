import os

import requests
from dotenv import load_dotenv
from terminaltables import AsciiTable


def get_total_data_vacancy_hh(language):
    url = 'https://api.hh.ru/vacancies'
    total_data_vacansy_hh = []
    page = 0
    total_pages = 1
    while page < total_pages:
        params = {
            'text': language,
            'area': 1,
            'per_page': 100,
            'page': page
        }
        response = requests.get(
            url,
            params=params
        )
        response.raise_for_status()
        data_vacancies = response.json()['items']
        total_pages = response.json()['pages']
        total_data_vacansy_hh.extend(data_vacancies)
        page += 1
    return total_data_vacansy_hh


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
    vacancy_salary = vacancy['salary']
    if vacancy_salary:
        vacancy_salary_currency = vacancy['salary']['currency']
        if vacancy_salary_currency == 'RUR':
            salary_from = vacancy['salary']['from']
            salary_to = vacancy['salary']['to']
            rub_salary_for_hh = predict_salary(salary_from, salary_to)
    return rub_salary_for_hh


def get_hh_statistic(total_data_vacansy_hh):
    if total_data_vacansy_hh:
        amount_vacancies = len(total_data_vacansy_hh)
        middle_salaries = [
            predict_rub_salary_hh(vacancy) for vacancy in total_data_vacansy_hh
            if predict_rub_salary_hh(vacancy) != 0
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
        total_data_vacansy_hh = get_total_data_vacancy_hh(language)
        statistic_hh[language] = get_hh_statistic(total_data_vacansy_hh)
    return statistic_hh


def get_total_data_vacancy_sj(language):
    super_job_url = 'https://api.superjob.ru/2.0/vacancies'
    secret_key = os.getenv('SUPER_JOB_KEY')
    page = 0
    next_page = 1
    total_data_vacansy_sj = []
    while next_page:
        headers = {'X-Api-App-Id': secret_key}
        params = {
            'keyword': language,
            'town': 4,
            'count': 5,
            'page': page,
            'catalogues': 48,
            'no_agreement': 1
        }
        response = requests.get(
            super_job_url,
            headers=headers,
            params=params
        )
        response.raise_for_status()
        page += 1
        response_data_vacansies = response.json()['objects']
        total_data_vacansy_sj.extend(response_data_vacansies)
        next_page = response.json()['more']
    return total_data_vacansy_sj


def predict_rub_salary_sj(vacancy):
    sj_predict_salary = 0
    salary_from = vacancy['payment_from']
    salary_to = vacancy['payment_to']
    vacancy_salary_currency = vacancy['currency']
    if vacancy_salary_currency == 'rub':
        sj_predict_salary = predict_salary(salary_from, salary_to)
    return sj_predict_salary


def get_sj_statistic(total_data_vacansy_sj):
    if total_data_vacansy_sj:
        amount_vacancies = len(total_data_vacansy_sj)
        middle_salaries = [
            predict_rub_salary_sj(vacancy) for vacancy in total_data_vacansy_sj
            if predict_rub_salary_sj != 0
        ]
        vacancies_processed = len(middle_salaries)
        average_salary = int(sum(middle_salaries)/amount_vacancies)
        sj_statistics = {
            'vacancies_found': amount_vacancies,
            'vacancies_processed': vacancies_processed,
            'average_salary': average_salary
        }
        return sj_statistics


def get_all_language_stat_from_sj(languages):
    statistic_sj = {}
    for language in languages:
        total_data_vacansy_sj = get_total_data_vacancy_sj(language)
        statistic_sj[language] = get_sj_statistic(total_data_vacansy_sj)
    return statistic_sj


def get_table(site_name, statistic):
    title = '{} Moscow----------'.format(site_name)
    if statistic:
        table_data = [[
            'Programming language',
            'Vacancies found',
            'Vacancies processed',
            'Average salary'
        ]]
        table_instance = AsciiTable(table_data, title)
        for language, language_stat in statistic.items():
            if language_stat:
                row = [language]
                for key, value in language_stat.items():
                    row.append(value)
                table_data.append(row)
        return table_instance.table


def main():
    load_dotenv()
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
    print(get_table(site_name, get_all_language_stat_from_sj(languages)))


if __name__ == "__main__":

    main()