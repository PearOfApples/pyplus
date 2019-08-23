from netmiko import ConnectHandler
from datetime import datetime
from pprint import pprint
import yaml
import json

yaml_data = yaml.load(open('../../../.netmiko.yml', 'r'))

conn = ConnectHandler(**yaml_data['cisco3'])
print(conn.find_prompt())
conn.disconnect()

