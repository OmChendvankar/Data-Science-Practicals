
# PRACTICAL 3 - Utilities and Auditing
# 3A. Fixer Utitlities
# Om V Chendvankar - 23-SEP-2022
# UNIVERSITY DEPARTMENT OF INFORMATION TECHNOLOGY

#imports
import string
import datetime as dt

# 1 Removing lagging spaces from a data entry
print('#1 Removing lagging spaces from a data entry');
baddata = "Data Science with too many spaces is bad!!!      "
print('>',baddata,'<')

cleandata=baddata.strip()
print('>',cleandata,'<')

# 2 Removing leading spaces from a data entry
print('#2 Removing leading spaces from a data entry');
baddata = "     Data Science with too many spaces is bad!!!"
print('>',baddata,'<')

cleandata=baddata.strip()
print('>',cleandata,'<')

# 3 Removing leading & lagging spaces from a data entry
print('#3 Removing leading & lagging spaces from a data entry');
baddata = "     Data Science with too many spaces is bad!!!    "
print('>',baddata,'<')

cleandata=baddata.strip()
print('>',cleandata,'<')

# Convert YYYY/MM/DD to DD Month YYYY
print('# 3 Reformatting data entry to match specific formatting criteria.')
baddate = dt.date(2019, 10, 31)
baddata=format(baddate,'%Y-%m-%d')
baddata

gooddate = dt.datetime.strptime(baddata,'%Y-%m-%d')
print(gooddate)

gooddata=format(gooddate,'%d %B %Y')
print(gooddata)

print('Bad Data : ',baddata)
print('Good Data : ',gooddata)

# %b: Returns the first three characters of the month name. In our example, it returned "Sep"
# %d: Returns day of the month, from 1 to 31. In our example, it returned "15".
# %Y: Returns the year in four-digit format. In our example, it returned "2018".
# %H: Returns the hour. In our example, it returned "00".
# %M: Returns the minute, from 00 to 59. In our example, it returned "00".
# %S: Returns the second, from 00 to 59. In our example, it returned "00".

print('#2 Removing nonprintable characters from a data entry') 
printable = set(string.printable) 
baddata = "Data\x00Science with\x02 funny characters is \x10bad!!!" 
print('Bad Data : ',baddata);

cleandata=''.join(filter(lambda x: x in string.printable,baddata))
print('Clean Data : ',cleandata)

# more on lambda functions here : https://www.w3schools.com/python/python_lambda.asp
