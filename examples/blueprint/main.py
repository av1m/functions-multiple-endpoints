from src import create_app
from functions_wrapper import entrypoint

app_wrap = lambda request: entrypoint(create_app(), request)

# Run with the following command:
# functions_framework --target app_wrap
