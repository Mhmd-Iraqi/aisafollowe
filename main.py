import requests
import random,time,base64,flask
from tinydb import *
Query=Query()
conn=TinyDB("./daat.json")
use ="qwertyuiopazsdfgjxnczkznha"
from flask import *
api=Flask(__name__)
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
		return {"coin": coin}
	except:
		return {"coin": "Error"}
def coll1(token,userid,uh,un2,ah2,ak2):
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
	pk=req[0]["pk"]
	idd=req[0]["id"]
	orderid=req[0]["order_id"]
	username=req[0]["username"]
	hash=requests.get(f"https://hashtokenfrreefjxcccc--mhmd-ltyyltyy.repl.co/?uid={userid}&id={idd}&order={orderid}&pk={pk}&username={username}").json()["hash"]
	data2={"version_code":1,"market_type":"bazzar","language":"en","u_n":un2,"u_h":uh,"a_h":ah2,"a_k":ak2,"order_id":orderid,"get_coin":"true","u_hash":hash,"error":""}
	upd=requests.post("https://asiafollower.com/api/AsiaVersion/v1/updateOrder",headers=headers,json=data2).json()
	data3={"version_code":1,"market_type":"bazzar","language":"en","u_n":un2,"u_h":uh,"a_h":ah2,"a_k":ak2}
	info=requests.post("https://asiafollower.com/api/AsiaVersion/v1/getUserInfo",headers=headers,json=data3).json()
	coin=info["user"]["follow_coin"]
	return {"coin": coin}

def login(X,user):
	
		if 0==0:
			message2 = user
			message_bytes2 = message2.encode('ascii')
			base64_bytes2 = base64.b64encode(message_bytes2)
			base64_message2= base64_bytes2.decode('ascii')
			
			re = requests.get(f"http://dark-strom.000webhostapp.com/cio.php?usname={user}&usid={X}&submit=submit",verify=False).text
			
			
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

	




		headers = {
    'Host': 'asiafollower.com',
    'content-type': 'application/json; charset=UTF-8',
    # 'content-length': '714',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}

		data = {"hashmail":"VjFjd2VGVXdOVmRqUld4cVVqTkNVMVZxU205a01WSllZWHBHYWxJd2NIaFZiRkpYVlVaYVIxSnFRbFZXVmtwaFdrVlZlRkpXV2xWTlJEQTk=",
"version_code":1,
"market_type":"bazzar",
"language":"ar",
"u_n":base64_message2,
"u_h":uhlog,
"a_h":ah,
"a_k":ak,
"u_i":ui,
"hashc":"WVhWMGFHOXlhWHBoZEdsdmJqMUNaV0Z5WlhJZ1NVZFVPakk2WlhsS2EyTXhPVEZqTWxaNVdESnNhMGxxYjJsT1ZHZDNUVlJCZUU5VVNYbE9SRTFwVEVOS2VscFlUbnBoVnpsMVlWZFJhVTlwU1RGUFJFRjRUVVJGTlUxcVNUQk5lVlY2VVZaT1ZVMVVUVEJqUldSMVRrVk9VazR5U2s1S1ZFNUNUWGxWZWxGVlJscGFSbkJ1WWxaU1drMUhkRWxWUkZKU1dqRkNhMUo2WkRKWmJHeE9UVEJuZVdSRlJrMVdSVXBIVFd4V01WRXhUblpqYlVWNldubEtPU1pqYkdGcGJUMHdKbTFwWkQxYVJtSlRObEZCUWtGQlIwSkRkV1J2TFZsZk1HOVpORGRuZUZNd0puSjFjajBtVTJWemMybHZibDlKUkQwMk5tRm1ZbVF3T0MxaE4yRTBMVFEwTXpjdE9XRmtZaTFoT1dGaFlqWTRORGxqWXpjbVJHVjJhV05sWDBsRVgxVlZhV1E5TVdGbFlXSTVPVGN0TXpjMU15MDBZV1EyTFRrMFpURXRaR0V3T1RoaFkyWmtOek13SmxCb2IyNWxYMmxrUFdGdVpISnZhV1F0WVRNMk0yRmtOemhpWlRoaU1EbG1KbFZ6WlhKZlFXZGxiblE5U1c1emRHRm5jbUZ0SURFM09DNHhMakF1TXpjdU1USXpJRUZ1WkhKdmFXUWdLREkxTHpjdU1TNHhPeUEwTlRoa2NHazdJREUxTlRoNE5qSTJPeUJhVkVVN0lGTk5MVlE0TWpBN0lHZDBjemt5TUhabGJIUmxPeUJ4WTI5dE95QmxibDlIUWlrbQ=="
}
		
		re = requests.post('https://asiafollower.com/api/AsiaVersion/v7/loginUser', headers=headers,json=data).text
	
		
		
			#print(re)
		take = re.split('"token":"')[1]
		tokens = take.split('"')[0]
		return {"token": tokens,"ah": ah2,"uh": uh,"un": un2,"ak":ak2}

@api.route("/aisa/follow/100/<yourpk>")
def ashu(yourpk):
		try:
			data=conn.search(Query.pk==yourpk)[0]
			tokens=data["token"]
			X=data["X"]
			ah2=data["ah"]
			ak2=data["ak"]
			un2=data["un"]
			uh=data["uh"]
			user=data["user"]
			youruser=user
		except:
			X=str("".join(random.choice("0987654321")for i in range(11)))
			user = str("".join(random.choice(use)for i in range(8)))
			ll=login(X,user)
			tokens=ll["token"]
			uh=ll["uh"]
			un2=ll["un"]
			ah2=ll["ah"]
			ak2=ll["ak"]
			youruser=user
			conn.insert({"pk":yourpk,"user":user,"X":X,"token": tokens,"ah":ah2,"ak":ak2,'uh':uh,"un":un2})
		
	


		
		import re
			
		coin=coll(tokens,X,uh,un2,ah2,ak2)["coin"]
		if coin=="Error":
				X=str("".join(random.choice("0987654321")for i in range(11)))
	
	
				user = str("".join(random.choice(use)for i in range(8)))
				ll=login(X,user)
				tokens=ll["token"]
				uh=ll["uh"]
				un2=ll["un"]
				ah2=ll["ah"]
				conn.insert({"pk":yourpk,"user":user,"X":X,"token": tokens,"ah":ah2,"ak":ak2,'uh':uh,"un":un2})
		else:
				
				
				if int(coin)>=200:
					headers = {
    'Host': 'asiafollower.com',
    'content-type': 'application/json; charset=UTF-8',
    "token": tokens,
    # 'content-length': '714',
    # 'accept-encoding': 'gzip',
    'user-agent': 'okhttp/3.14.9',
}


			
					ors = int(int(coin)/2)
					data ={
"hashmail":"VjFjd2VGVXdOVmRqUld4cVVqTkNVMVZxU205a01WSllZWHBHYWxJd2NIaFZiRkpYVlVaYVIxSnFRbFZXVmtwaFdrVlZlRkpXV2xWTlJEQTk=",
"version_code":1,
"market_type":"bazzar",
"language":"ar",
"u_n":un2,
"u_h":uh,
"a_h":ah2,
"pk":str(yourpk),
"image_url":"https://instagram.fisu4-2.fna.fbcdn.net/v/t51.2885-19/329778409_1225203568100002_418416571540140401_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fisu4-2.fna.fbcdn.net&_nc_cat=110&_nc_ohc=csyVQk4RehAAX_vEHaf&edm=AEF8tYYBAAAA&ccb=7-5&oh=00_AfAyI5YfVGhFmnWdaATSWfmSf19C0d88uXQo7-yVLO284A&oe=645B06EA&_nc_sid=a9513d",
"username":youruser,
"order_value":"",
"order_link":youruser,
"order_type":"follow",
"order_count":str(ors),
"start_count":"0",
"is_special":"false"}
					res= requests.post('https://asiafollower.com/api/AsiaVersion/v7/setOrder', headers=headers,json=data).text
					if 'success' in res:
					
			
						ko+=ors
						X=str("".join(random.choice("0987654321")for i in range(11)))
	
	
						user = str("".join(random.choice(use)for i in range(8)))
						ll=login(X,user)
						tokens=ll["token"]
						uh=ll["uh"]
						un2=ll["un"]
						ah2=ll["ah"]
						conn.insert({"pk":yourpk,"user":user,"X":X,"token": tokens,"ah":ah2,"ak":ak2,'uh':uh,"un":un2})
						return {"coin": coin,"message": "Done Send 100 Followers"}
					else:
						return {"coin": coin,"message": res}
			
				else:
					return {"coin": coin,"message": "Error Coins"}

api.run(host="0.0.0.0",port=5000)	
