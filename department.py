import requests
import json
from flask import Flask,render_template
app = Flask(__name__)

# precomputation

url = "https://api.zenefits.com/core/companies"
headers = {'Authorization': 'Bearer elZxQlHDSUallvL3OnnH'}
r = requests.get(url,headers=headers)
json_data = json.loads(r.text)
input1=json_data['data']['data']
print (input1)
cd={}
for comp in input1:
	dict2={}
	dict2['name']=comp['name']
	dep_url=comp['departments']['url']
	r = requests.get(dep_url,headers=headers)
	json_data = json.loads(r.text)
	input2=json_data['data']['data']
	print(input2)
	dict2['department']=[]
	for dept in input2:
		dict2['department'].append(dept['name'])
	cd[comp['id']]=dict2

@app.route('/department')
def get_department():
	return render_template('department.html',data=cd)

if __name__ == '__main__':
   app.run()
# simple web app

