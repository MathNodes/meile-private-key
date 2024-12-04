# meile-private-key

Retrieve the Meile 2.0 wallet private key in HEX to import into Keplr

# Install

Create a virtual environment to run this code:

```shell
python3 -m venv meileprivkey
```

Activate the virtual environment:

### Windows

```shell
.\meileprivkey\Scripts\activate
```

### Linux & OS X

```shell
source meileprivkey/bin/activate
```

Install the cryptfile module:

```shell
pip3 install keyrings.cryptfile
```

# Export the Private Key

Run the following once you have done the above

```shell
python3 meile_privkey.py
```

This will output the private key that can be imported to Keplr. 
