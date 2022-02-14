# python_blockchain
This is my project based on the following Udemy course.
https://www.udemy.com/course/python-js-react-blockchain/

# Instructions (following the Udemy course)
**Activate the virtual environment**
```
source blockchain-env/bin/activate
```

**Install all packages**
```
cd /path/to/project/
pip install -e .
```

**Run the tests**

Make sure to activate the virtual environment.

```
python -m pytest backend/tests
```

**Run the application and API**

Make sure to activate the virtual environment.

```
python -m backend.app
```

**Run a peer instance**

Make sure to activate the virtual environment.

```
export PEER=True && python -m backend.app
```
