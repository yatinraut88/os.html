details={'INDIA':'NEW DELHI','AMERICA':'WASHINGTON DC','JAPAN':'TOKYO'}
print('country-capital list..')
print(details)
import operator

sort1=dict(sorted(details.items(),key=operator.itemgetter(1)))
print('country-capital in ascending order of capital...')
print (sort1)

sort2=dict(sorted(details.items(),key=operator.itemgetter(1),reverse= True ))
print('country-capital in ascending order of capital...')
print (sort2)
