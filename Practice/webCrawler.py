import json

def extract(a,b,c):
	dic = {}
	dic['one'] = a
	dic['two'] = b
	dic['three'] = c
	dic = json.dumps(dic)

	return dic