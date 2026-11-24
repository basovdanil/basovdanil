# Данил Басов

[![checks](https://github.com/basovdanil/portfolio/actions/workflows/checks.yml/badge.svg)](https://github.com/basovdanil/portfolio/actions/workflows/checks.yml)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Делаю отчёты на данных, которые можно перепроверить. Выгрузка идёт в расчёт, а в конце скрипт проверки возвращает `0`, если всё сошлось, или `4`, если есть расхождение.

## Кейсы

| Кейс | Данные | Результат |
|:--|:--|:--|
| [ОСВ: найти дефекты](https://basovdanil.github.io/portfolio/case-osv/case-osv.html) | 16 счетов, вымышленные | 5 дефектов: красное сальдо, разрыв итогов, отрицательный оборот |
| [Вакансии: выгрузка без персональных данных](https://basovdanil.github.io/portfolio/case-jobs/case-jobs.html) | trudvsem.ru, открытые | 505 строк, 0 почт, 0 телефонов |
| [Операции: одна команда](https://basovdanil.github.io/portfolio/case-tables/case-tables.html) | три файла, синтетика | слияние, сравнение версий, раскладка: 9 из 9 сверок |

Числа в таблице посчитаны скриптами по CSV из репозитория.

## Проекты

Семь инструментов: пять на чистом Python, без установки зависимостей, и два ML-пайплайна на scikit-learn. К каждому приложены данные, тесты и тег `v1.0.0`. GitHub Actions гоняет тесты на каждый push — последние прогоны зелёные у всех восьми.

| Проект | Что делает | Проверка |
|:--|:--|:--|
| [osv-check](https://github.com/basovdanil/osv-check) | проверяет оборотно-сальдовую ведомость из 1С | 13 тестов, демо даёт 5 находок |
| [table-etl](https://github.com/basovdanil/table-etl) | слияние, дифф и разбивка табличных выгрузок | 11 тестов, демо 51 → 45 и 72 → 60 строк |
| [forecast-baseline](https://github.com/basovdanil/forecast-baseline) | бэктест пяти базовых прогнозов | 16 тестов, недельная сезонность MAPE 8,81 % |
| [sql-analytics](https://github.com/basovdanil/sql-analytics) | десять SQL-отчётов по таблице продаж | 19 тестов, сходимость 12 из 12 |
| [titanic-baseline](https://github.com/basovdanil/titanic-baseline) | кросс-валидация трёх моделей и генератор submission | 28 тестов, случайный лес 0,8316 ± 0,0120 |
| [churn-baseline](https://github.com/basovdanil/churn-baseline) | отток: кросс-валидация и подбор порога при дисбалансе | 19 тестов, логистическая регрессия 0,8446 ± 0,0132 |
| [hh-vacancy-check](https://github.com/basovdanil/hh-vacancy-check) | проверяет, открыта ли вакансия на hh.ru, без входа в аккаунт | 16 тестов, дедлайн берётся из `validThrough` |
| [pii-scan](https://github.com/basovdanil/pii-scan) | ищет персональные данные в CSV до отправки файла наружу | 15 тестов, примеры в отчёте маскируются |

## Стек

Python, SQL и Excel. К каждому результату приложен скрипт проверки: арифметика, дубликаты, сходимость разбивки с итогом.

## Ссылки

- Страницы кейсов: https://basovdanil.github.io/portfolio/
- Код и данные: https://github.com/basovdanil/portfolio (7 скриптов, 13 CSV, 2 книги)
- Почта: basovdanil@yandex.ru

---

## English

Data analyst in retail and food manufacturing. My rule: a report is only done when a separate check
script recomputes it and returns `0` on match or `4` on a mismatch — every case and project below
ships with that check, its data and its tests.

- **Cases** (write-ups with numbers): <https://basovdanil.github.io/portfolio/>
- **Tools** (Python 3.9+, standard library only unless stated): `osv-check` (trial balance from 1C),
  `table-etl` (merge/diff/split of spreadsheet exports), `forecast-baseline` (backtest of five
  baselines), `sql-analytics` (ten SQL reports with 12 reconciliations), `hh-vacancy-check`
  (is an hh.ru vacancy still open), `pii-scan` (personal data in a CSV export), plus two
  scikit-learn baselines: `titanic-baseline`, `churn-baseline`.
- Every repository is tagged `v1.0.0`, has a green CI badge and an English README.
