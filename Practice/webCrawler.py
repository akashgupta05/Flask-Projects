import json

def extract(args1,args2,args3):
	dic={}
	dic['one'] = args1
	dic['two'] = args2
	dic['third'] = args3
	dic = json.dumps(dic)
	return dic