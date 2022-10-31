# Programming vacancies compare

The program uses the API of the Headhunter and Superjob web services to obtain information on programmers' salaries.
The program automatically calculates the average salary for the programming languages of interest and displays the information in the table.

### Software environment and installation:

Python3 should already be installed.

### Program installation:

Download the code: [https://github.com/VAChess777//Lesson-5-web-servises-API-Devman](https://github.com/VAChess777//Lesson-5-web-servises-API-Devman), or clone the `git` repository to a local folder:
```
git clone https://github.com/VAChess777//Lesson-5-web-servises-API-Devman
```

### Installing dependencies:
 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bach
pip install -r requirements.txt
```

### About environment variables:

For the program to work, you will need `API tokens`, which you will then place in the 
environment variables.  The values of which you will put in the `.env` file.

For the work of the program `main.py`, you will need an `API token` from the resource
by the link [https://api.superjob.ru](https://api.superjob.ru). 

When you receive the token, put its value in the `.env` file.
For example: `SUPER_JOB_KEY=v3.r.13856390.5f5d656a28ce...........`.

Then put this value in an environment variable in the program.
For example: `nasa_api_key_epic = os.environ['SUPER_JOB_KEY']`.

To use all of the above environment variables in programs, use the `load_dotenv()` module.

### How to run the program:

Run the script ```main.py``` with the command:
```bach
$ python main.py
```

### How the program works:

The program consists of 1 script:

```main.py``` - 'The program downloads salary information from the headhunter and superjob web services.\ 
				Then the program automatically calculates the average salary for the programming languages of interest and\ 
				displays the information in the table.'

            
### Features works of the program:

The `main.py` program contains the functions:

* The `get_vacancies_hh` function - downloads salary data from the Headhunter server.
* The `predict_salary` function - calculates the middle salary.
* The `predict_rub_salary_hh` function - receives salary data for each vacancy from Headhunter and transmits this data to the a `predict_salary` function.
* The `get_hh_statistic` function - gets statistics on vacancies and salaries from Headhunter. Calculates the average salary and vacancies processed.
* The `get_all_language_stat_from_hh` function - gets statistics on vacancies and salaries from Headhunter for each of the languages of interest.
* The `get_vacancies_sj` function - downloads salary data from the SuperJob server.
* The `predict_rub_salary_sj` function - receives salary data for each vacancy from SuperJob and transmits this data to the a `predict_salary` function.
* The `get_sj_statistic` function - gets statistics on vacancies and salaries from SuperJob. Calculates the average salary and vacancies processed.
* The `get_all_language_stat_from_sj` function - gets statistics on vacancies and salaries from SuperJob for each of the languages of interest.
* The `get_table` function - gets data with the `get_all_language_stat_from_hh` and `get_all_language_stat_from_sj` functions. Then puts this data into tables using `terminaltables` package.
* The `def main():` - main function. 

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).