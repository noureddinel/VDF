
def setup(lamb, t):
 
# lamb is security parameter, t is difficulty, proportional to time
	
	pp=(X,Y) #public parameter is specified by lamb and t
	X=some_function(Lamb,t)
	Y=some_function2(Lamb,t)

	return (ek,vk)
	#ek is evaluation key, vk is verification key

X=[] #X is an input space, sepcificed by public parameter
Y=[] #Y is an output space, specified by ppublic parameter and therefore by lamb and t

def eval(ek, x):
	return (y, pi)
	#takes in eval key and an input, outputs y output and a proof
def verify(vk,x,y,pi):
	result=True
	return result

def powermod(a, b, n):
    r = 1
    while b>0:
        if int(b)&1==1:
            r =r*a%n
        b/=2
        a=a*a%n
    return r
def candidate_perm_poly(x,s,a): #s=p^r
	enum=(x**s-a*x-a)*(x**s-a*x+a)^s+((x**s-a*x+a)^2+4*a^2*x)^((s+1)/2)
	denom=2*x^s
	return enum/denom
#p=3mod4
#lets test with 
#x must be a number smaller than p