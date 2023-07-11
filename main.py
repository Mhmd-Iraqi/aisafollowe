from flask import Flask, render_template, session, redirect, request
from database import *
import os,json
if 0==0:
 import requests,json,random,base64
 from urllib.parse import quote
 from base64 import b64encode, b64decode
 from datetime import datetime
 from time import sleep
def coll(tokens,userid,uh,un2,ah2,ak2):
	import requests
	headers = {
    'Host': 'asiafollower.com',
    'content-type': 'application/json; charset=UTF-8',
    "token": tokens,
    # 'content-length': '714',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}
	data1={"version_code":1,"market_type":"bazzar","language":"en","u_n":un2,"u_h":uh,"a_h":ah2,"a_k":ak2,"order_type":"follow"}
	req=requests.post("https://asiafollower.com/api/AsiaVersion/v1/getOrder",headers=headers,json=data1).json()
	try:
		for orderss in req:
			pk=orderss["pk"]
			idd=orderss["id"]
			orderid=orderss["order_id"]
			username=orderss["username"]
			hash=requests.get(f"https://hashtokenfrreefjxcccc--mhmd-ltyyltyy.repl.co/?uid={userid}&id={idd}&order={orderid}&pk={pk}&username={username}").json()["hash"]
			data2={"version_code":1,"market_type":"bazzar","language":"en","u_n":un2,"u_h":uh,"a_h":ah2,"a_k":ak2,"order_id":orderid,"get_coin":"true","u_hash":hash,"error":""}
			upd=requests.post("https://asiafollower.com/api/AsiaVersion/v1/updateOrder",headers=headers,json=data2).json()
		data3={"version_code":1,"market_type":"bazzar","language":"en","u_n":un2,"u_h":uh,"a_h":ah2,"a_k":ak2}
		info=requests.post("https://asiafollower.com/api/AsiaVersion/v1/getUserInfo",headers=headers,json=data3).json()
		coin=info["user"]["follow_coin"]
	except:coin=req["message"]
	return {"coin": coin}

def login(X,user):
	
		if 0==0:
			message2 = user
			message_bytes2 = message2.encode('ascii')
			base64_bytes2 = base64.b64encode(message_bytes2)
			base64_message2= base64_bytes2.decode('ascii')
			
			re = requests.get(f"https://dark-strom.000webhostapp.com/cio.php?usname={user}&usid={X}&submit=submit").text
			
			
			#print(re)
#print(re)
			uns = re.split('un:')[1]
			un = uns.split(':un')[0]
			#print(un)
#print(un)
			uhlogin = re.split('uhlogin:')[1]
			uhlog = uhlogin.split(':uhlogin')[0]
			#print(uhlog)


			keys = re.split('key:')[1]
			key = keys.split(':key')[0]
			#print(key)

#print(key)


			uhs = re.split('uh:')[1]
			uh = uhs.split(':uh')[0]

#print(uh)

			ahs= re.split('ah:')[1]
			ah = ahs.split(':ah')[0]

#print(ah)

			aks= re.split('ak:')[1]
			ak = aks.split(':ak')[0]

#print(ak)

			uis= re.split('ui:')[1]
			ui = uis.split(':ui')[0]
			#print(ui)

#print(ak)
#________--_____________-________________
			un1= re.split('un1:')[1]
			un1 = un1.split(':un1')[0]

#print(un1)

			uh1= re.split('uh1:')[1]
			uh1 = uh1.split(':uh1')[0]
#print(uh1)

			ak1= re.split('ak1:')[1]
			ak1 = ak1.split(':ak1')[0]
#print(ak1)

			ah1= re.split('ah1:')[1]
			ah1 = ah1.split(':ah1')[0]
#print(ah1)
			un2= re.split('un2:')[1]
			un2 = un2.split(':un')[0]
	#print(un2)
			ah2= re.split('ah2:')[1]
			ah2 = ah2.split(':ah2')[0]
	#print(ah2)
			ak2= re.split('ak2:')[1]
			ak2 = ak2.split(':ak2')[0]
	#print(ak2)

	




#		headers = {
#    'Host': 'asiafollower.com',
#    'content-type': 'application/json; charset=UTF-8',
#    # 'content-length': '714',
#    # 'accept-encoding': 'gzip',
#    'user-agent': 'okhttp/3.14.9',
#}

#		data = {"hashmail":"VjFjd2VGVXdOVmRqUld4cVVqTkNVMVZxU205a01WSllZWHBHYWxJd2NIaFZiRkpYVlVaYVIxSnFRbFZXVmtwaFdrVlZlRkpXV2xWTlJEQTk=",
#"version_code":1,
#"market_type":"bazzar",
#"language":"ar",
#"u_n":base64_message2,
#"u_h":uhlog,
#"a_h":ah,
#"a_k":ak,
#"u_i":ui,
#"hashc":"WVhWMGFHOXlhWHBoZEdsdmJqMUNaV0Z5WlhJZ1NVZFVPakk2WlhsS2EyTXhPVEZqTWxaNVdESnNhMGxxYjJsT1ZHZDNUVlJCZUU5VVNYbE9SRTFwVEVOS2VscFlUbnBoVnpsMVlWZFJhVTlwU1RGUFJFRjRUVVJGTlUxcVNUQk5lVlY2VVZaT1ZVMVVUVEJqUldSMVRrVk9VazR5U2s1S1ZFNUNUWGxWZWxGVlJscGFSbkJ1WWxaU1drMUhkRWxWUkZKU1dqRkNhMUo2WkRKWmJHeE9UVEJuZVdSRlJrMVdSVXBIVFd4V01WRXhUblpqYlVWNldubEtPU1pqYkdGcGJUMHdKbTFwWkQxYVJtSlRObEZCUWtGQlIwSkRkV1J2TFZsZk1HOVpORGRuZUZNd0puSjFjajBtVTJWemMybHZibDlKUkQwMk5tRm1ZbVF3T0MxaE4yRTBMVFEwTXpjdE9XRmtZaTFoT1dGaFlqWTRORGxqWXpjbVJHVjJhV05sWDBsRVgxVlZhV1E5TVdGbFlXSTVPVGN0TXpjMU15MDBZV1EyTFRrMFpURXRaR0V3T1RoaFkyWmtOek13SmxCb2IyNWxYMmxrUFdGdVpISnZhV1F0WVRNMk0yRmtOemhpWlRoaU1EbG1KbFZ6WlhKZlFXZGxiblE5U1c1emRHRm5jbUZ0SURFM09DNHhMakF1TXpjdU1USXpJRUZ1WkhKdmFXUWdLREkxTHpjdU1TNHhPeUEwTlRoa2NHazdJREUxTlRoNE5qSTJPeUJhVkVVN0lGTk5MVlE0TWpBN0lHZDBjemt5TUhabGJIUmxPeUJ4WTI5dE95QmxibDlIUWlrbQ=="
#}
#		
#		re = requests.post('https://asiafollower.com/api/AsiaVersion/v7/loginUser', headers=headers,json=data).text
#	
#		
#		
#			#print(re)
#		take = re.split('"token":"')[1]
#		tokens = take.split('"')[0]
		return {"ah": ah2,"uh": uh,"un": un2,"ak":ak2}
	
	
	


us='1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
app = Flask(__name__)
@app.route('/')
def index():
    	return render_template('index.html')

@app.route("/start")
def start():
   try:send+=0
   except:send=0
   userid=request.args.get("userid")
   token=request.args.get("token")
   pas=request.args.get("password")
   try:
   	data=conn.search(Query.code==pas)[0]
   	dat=data["date"]
   	print(dat)
   	dr1 = datetime.now()
   	d1=str(dr1)
   	year=d1.split("-")[0]
   	month=d1.split("-")[1].split("-")[0]
   	day=d1.split("-")[2].split(" ")[0]
   	if day=="02" or day=="01" or day=="03" or day=="04" or day=="05" or day=="06" or day=="07" or day=="08" or day=="09":
   		day=day.split("0")[1]
   	if month=="02" or month=="01" or month=="03" or month=="04" or month=="05" or month=="06" or month=="07" or month=="08" or month=="09":
   		month=month.split("0")[1]
   	if int(year)>=int(dat.split("/")[0]) and int(day)>=int(dat.split("/")[2]) and int(month)>=int(dat.split("/")[1]):
   		return render_template("res.html",res={"message": "password expire."})
   	
   except:return render_template("res.html",res={"message": "error password."})
   use="qazxcvbnmmlkjhgswrtuopp"
   user = str("".join(random.choice(use)for i in range(8)))
   ll=login(userid,user)	
   uh=ll["uh"]
   un2=ll["un"]
   ah2=ll["ah"]
   ak2=ll["ak"]
   coins=coll(token,userid,uh,un2,ah2,ak2)["coin"]
   return render_template("res.html",res={"coin": str(coins),"by": "@fo2d0j"})
   	
   

   
   
   return render_template("res.html",res=resp)
@app.route("/adminqazxQ12")
def admin():
	return render_template('index2.html')
@app.route("/admingdnbcgkvkktadd")
def addm():
	pas=request.args.get("password")
	date=request.args.get("date")
	try:
		conn.search(Query.code==pas)[0]
		conn.update({"date": date},Query.code==pas)
		return render_template("res.html",res={"message": "Success" , "password": pas , "date": date})
	except:
		conn.insert({"code": pas , "date": date})
		return render_template("res.html",res={"message": "Success" , "password": pas , "date": date})
		
app.run(host="0.0.0.0", port=5000)