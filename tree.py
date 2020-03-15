import requests
import json
from flask import Flask,render_template
app = Flask(__name__)

# precomputation

url = "https://api.zenefits.com/core/people"
headers = {'Authorization': 'Bearer elZxQlHDSUallvL3OnnH'}
r = requests.get(url,headers=headers)
json_data = json.loads(r.text)
input1=json_data['data']['data']
tree={}
root=''
for people in input1:
	if people['status']!='active':
		continue
	id1=people['id']
	dict2={}
	dict2['name']=people['preferred_name']
	dict2['url']=people['url']
	dict2['child']=[]
	tree[id1]=dict2

for people in input1:
	if people['status']!='active':
		continue
	id1=people['id']
	manager=people['manager']['url']
	if (manager):
		manager_id=manager.split('/')[5]
		tree[manager_id]['child'].append(id1)
	else:
		root=id1

# simple web app
st='<head><body>'

def generate_tree(node):
	global st
	st=st+"<a href='"+tree[node]['url']+"'>"+tree[node]['name']+"</a>"
	childs=tree[node]['child']
	if (childs==[]):
		return
	else:
		for i in childs:
			#global st
			st=st+"<ul type='o'><li>"
			generate_tree(i)
			st=st+"</li></ul>"

@app.route('/tree')
def get_tree():
	global st
	st='<head><body>'
	generate_tree(root)
	st=st+"</body></head>"
	#print (st)
	return st

if __name__ == '__main__':
   app.run()
