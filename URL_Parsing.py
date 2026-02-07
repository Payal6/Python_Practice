url = 'https://www.kaggle.com/dataset'
protocol = url[ : url.find(':')]
dot1 = url.find('.')
dot2 = url.find('.',dot1+1)
domain = url[dot1+1:dot2]
# dataset = url[ url.rfind('/') : ]
dataset = url[ url.find('/',dot2):]
print('Protocol : ',protocol)
print('Domain : ',domain)
print('Dataset : ',dataset)