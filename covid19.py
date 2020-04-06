import requests
def banner():
	print('''
   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ 
 ( C | o | v | i | d | 1 | 9 )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ news
			Coded by KTZ
''')
def main():
	print(''' \t1.Myanmar	2.World''')
	z=input("\n Choose:: ")
	print("","_"*40,"\n","_"*40)
	if z=='1':
		myanmar()
	elif z=='2':
		world()
	else:
		print("[÷]Some Error![÷]")
		
def myanmar():
	url="https://covid19.joymogok.com/mm.json"
	r=requests.get(url).json()
	print ("\n Total::",r['total'],"\n pui::",r['pui'],"\n suspected::",r['suspected'],"\n confirm::",r['confirm'],"\n lab_negative::",r['lab_negative'],"\n lab_pending::",r['lab_pending'],"\n discharge::",r['discharge'],"\n deaths::",r['deaths'],"\n recovered::",r['recovered'],"\n lastupdate::",r['dt'])

def world():
	url="https://covid19.joymogok.com/total.json"
	r=requests.get(url).json()
	print("\n confirmed::",r['confirmed'],"\n deaths::",r['deaths'],"\n recovered::",r['recovered'],"\n active::",r['active'],"\n closed::",r['closed'],"\n",r['time'])

banner()
main()
