# Playwright Pytest Test

This repo provides auto tests for [Automation Exercise Site](https://www.automationexercise.com/) <br />
The test cases you can find [Testcases Page](https://www.automationexercise.com/test_cases) of this site

## Dependencies Installation
To use these tests you should download this repo and install some dependencies

* To install dependencies
```
python -m pip install --upgrade pip
pip install pipenv
pipenv install --system
playwright install
```
## Test Launch
There are some commands to launch test

To launch tests on default browser (Chromium)
```
pytest
```
To launch tests on different browsers
```
pytest --browser_name <chromium/webkit/firefox>
```
To launch tests in parallel
```
pytest -n <number of workers>
```
To launch tests in headed mode
```
pytest --headed
```
## Open allure report
Every time you launch tests reports generate automatically. To see reports in html run
```
allure serve reports
```
## Viewing Previous Runs
* Workflow is set up so that the tests run every time someone pushes the repo
* The result of tests deploys on my [Github Pages](https://vladyslavbrchk.github.io/playwrightPytestTest/)
* The result of tests also sends as Slack Notification on [My Slack Channel](https://vbrchkluxequality.slack.com/archives/C06CJ0SCA8M)