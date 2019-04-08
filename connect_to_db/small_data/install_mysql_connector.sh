# To install mysql Connector follow this:

# Update APT
sudo apt update
sudo apt install python3-pip

# Check PIP's MySQL connector list
pip3 search mysql-connector | grep --color mysql-connector-python
-> This will display something like:
mysql-connector-python (8.0.15)                           - MySQL driver written in Python
mysql-connector-python-rf (2.2.2)                         - MySQL driver written in Python
mysql-connector-python-dd (2.0.2)                         - MySQL driver written in Python

# Now Install one of these connectors:
pip3 install mysql-connector-python
