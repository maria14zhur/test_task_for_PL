import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('tests')
parser.add_argument('values')
args = parser.parse_args()


try:
	with open(args.tests) as f:
		tests = json.load(f)
        
except Exception:
    print('Cant open tests.json')
    exit(1)
	
	
try:
	with open(args.values) as f:
		values = json.load(f)		
except Exception:
    print('Cant open values.json')
    exit(1)

def insert_value(d, required_key, new_value):
	for k,v in d.items():
		if k == 'id' and v == required_key:
			d['value'] = new_value
		if isinstance(v,list):
			for i in v:
				insert_value(i, required_key, new_value)
		
							
for v in values["values"]:
	id = v['id']
	value = v['value']
	insert_value(tests, id, value)	
	
	
try:
	with open('report.json', 'w') as f:
		json.dump(tests, f)
except Exception:
    print('Cant create report.json')		






