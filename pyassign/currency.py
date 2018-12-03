#!/usr/bin/env python3

"""currency.py: 汇率的计算
__author__ = "Zhangyinuo"
__pkuid__  = "1800011770"
__email__  = "1800011770@pku.edu.cn"
"""


def exchange(currency_from, currency_to, amount_from):
'''调用网上的数据，从而得到相应转化得到的值'''	
	from urllib.request import urlopen
	amount_from=str(amount_from)
	doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from)
	docstr = doc.read()
	doc.close()
	jstr = docstr.decode('ascii') 
	a1=jstr.replace("true","True")
	dict1=dict(eval(a1))                             
	return dict1['to']

list1=['17.13025 Chinese Yuan','278.4975 Japanese Yen','2.1589225 Euros']
'''在网站上用2.5美元兑换人民币，日元，欧元得到的结果，用于测试函数'''
def test1():
'''对于结果的测试'''
	assert  exchange('USD','CNY',2.5) == list1[0]
	assert  exchange('USD','JPY',2.5) == list1[1]
	assert  exchange('USD','EUR',2.5) == list1[2]

def test2():
'''对于输入内容的测试'''
	from urllib.request import urlopen
	doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+a+'&to='+b+'&amt='+c)
	docstr = doc.read()
	doc.close()
	jstr = docstr.decode('ascii') 
	if "false" in jstr:
		print("输入错误")
		assert False
	else:
		assert True 

a=input("输入货币源：")
b=input("输入要转变的货币：")
c=str(input("输入货币源的金额："))
def main():
'''先进行结果测试保证函数准确性，而后输入，在根据输入结果确定是否进一步执行exchange函数，最后执行exchange函数'''
	test1()
	test2()
	print(exchange(a,b,c))
    
if __name__ == '__main__':
	main()
