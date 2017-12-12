# Krypto
> The Crypto Wrapper we've been mining for. - No One Ever

[![Python](https://img.shields.io/badge/Python-3.0-green.svg)
[![Github All Releases](https://img.shields.io/github/downloads/atom/atom/total.svg)]()


A lightweight and simple wrapper for the [GDAX](https://www.gdax.com) crypto API, with some useful utilities to calculate the following:
    - Crypto Net Worth
        - According to GDAX
    - Total Invested Amount
    - Total Earnings +/-

###Future Requests
    - turn this into a full application with DB, Auth, Mail, etc...
    - Build a react front end 
    - REST API from app
    - Machine Learning Algorithims integrated in App

## Getting Started
Getting started is simple head on over to GDAX[]

```bash
    git clone this_repository && ch this repository

    export GDAX_API_KEY=your_long_key_goes_here
    export GDAX_API_SECRET=your_API_secret
    export GDAX_API_PASS=your_API_pass

    python example.py

```

## Net Worth
This is a class that provides a useful wrapper for calculating the total value of cryptos

```python

from krypto.auth import CoinbaseExchangeAuth
from krypto.wo

# Create auth instance
auth = CoinbaseExchangeAuth(API_KEY, API_SECRET, API_PASS)

# Create Worth Instance
worth = Worth()
# Returns the following:
# [{'key': u'The Key's Value'},{'key2': u'Key 2s value'}]  


```





