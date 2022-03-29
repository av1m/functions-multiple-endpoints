# Functions_wrapper blueprint

Clone this repository:

```bash
git clone https://github.com/av1m/gcf-multiple-endpoints.git
```

Install the dependencies:

```bash
pip install -r requirements.txt
pip install .
```

Run the application:

```bash
# Move you to the examples folder you want to test
cd examples/blueprint # or cd examples/onefile

functions_framework --target app_wrap
```

You can also use Docker to run the application:

```bash
cd examples/blueprint
docker build -t flaskapp . && docker run --rm -p 8080:8080 -e PORT=8080 flaskapp
```
