
import datetime
import json
import hashlib
from urllib.request import urlopen

def sqrt_mod_p_squaring(x,p):
	y=pow(x,(int((p+1)/4)),p)	
	return y

def sqrt_mod_p_verify(y,x,p):
	if pow(y,2)%p==x%p:
		return True
	else:
		return False
def fastpow(base, exp, mod):
	if exp == 0:
		x = 1
	else:
		half = fastpow(base, exp // 2, mod)  # just / in Python 2
		x = half * half
		if exp % 2 == 1:
			x *= base
	return x % mod
def quad_res(x,p):
	return pow(x,int((p-1)/2),p)==1

def mod_sqrt_op(x,p):
	if not quad_res(x,p):
		x=(-x)%p
	y=sqrt_mod_p_squaring(x,p)
	return y
def mod_op(x):# hash operation on an int with 2^10 iternations
	p=1000000007
	x=x%p
	start=datetime.datetime.now()
	for i in range(2**22+100000):
		x=mod_sqrt_op(x,p)
	end=datetime.datetime.now()
	print(end-start)
	print("Ending value of first sequence is:",hex(x))
	return x
def mod_verif(hsh,x):
	a=int(hsh)
	p=1000000007
	start=datetime.datetime.now()
	for i in range(2**22+100000):
		a=pow(int(a),2,p)

	end=datetime.datetime.now()
	print('Finished verifying, time elapsed: ',end-start)
	if x%1000000007==a:
		return True
	else:
		return False




while True:
	try:
		block_data=json.load(urlopen("https://api.blockcypher.com/v1/eth/main"))
		cur_hash=block_data["hash"]
	except:
		print("No Connection")
	x=int(cur_hash,16)
	print("\n\nUsing Block",block_data["height"],"as seed, X is",cur_hash )
	x=x%1000000007
	print("\n\nX mod P is ",hex(x))
	y=mod_op(x)
	mod_verif(y,x)
	hash_object = hashlib.sha256(str(x).encode())
	hex_dig = hash_object.hexdigest()
	print(x,"will be the seed for randomness beacon. The SHA256 hash will be",hex_dig )
	print()
	print()
