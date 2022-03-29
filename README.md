# Run multiple endpoints on Google Cloud Functions and Amazon Lambda

This example show how to run multiple endpoints on Google Cloud Functions and Amazon Lambda.

By default, [functions-framework-python](https://github.com/GoogleCloudPlatform/functions-framework-python) can't run multiple endpoints on the same function.

I present two examples here:

* By using only [one file](examples/onefile/simple.py)
* By using [flask blueprints](examples/blueprint/main.py)

## Get started

Install the dependencies:

```bash
pip install functions_wrapper
```

```python
# main.py 
from flask import Flask
from functions_wrapper import entrypoint

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/test")
def test():
    return "Hello Test!"

app_wrap = lambda request: entrypoint(app, request)
```

Run this file with functions-framework:

```bash
functions_framework --target app_wrap
```
