#this file will be load before running any test
#every time we run pytest this will load and search for selenium.

pytest_plugins=[
    "ecommerce.tests.selenium",
    "ecommerce.tests.fixtures",
    "ecommerce.tests.factories"
]