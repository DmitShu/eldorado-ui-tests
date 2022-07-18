Introduction
------------

This repository contains several Web UI tests for eldorado.ru.
Uses PyTest + Selenium.

Files
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[pytest.ini](pytest.ini) contains driver select and path.

[pages/base.py](pages/base.py) contains PageObject pattern implementation for Python.

[pages/elements.py](pages/elements.py) contains helper class to define web elements on web pages.

[pages/variables.py](pages/variables.py) contains variables for tests

[tests/....py](tests/test_pf_auth_page.py) contains several Web UI tests for ...


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip3 install -r requirements.txt
    ```

2) Download and unpack Selenium WebDriver (choose version which is compatible with your browser). 

3) Open [conftest.py](conftest.py) and specify the driver type and path to the executable file.

4) Run tests:

    ```bash
    python -m pytest -v tests/
    ```

   ![alt text](example.png)
