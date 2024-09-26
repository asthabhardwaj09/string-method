##     \\string is immutable
##  means we cannot change string we can creat a copy and thier we can change

##  \\\Although strings are not classified as primitive data types in Python

##### In Python, strings are considered as a built-in data type, 
# along with other types like integers, floats, lists, tuples, dictionaries, etc. 
# Strings are quite versatile in Python and are extensively used for representing text data.

a='astha'
print(type(a))

### line 4 : include 1 but not 5 that means 5-1
print(a[1:5])


### this will tell total length of a statement
print(len(a))

### this will give the particular element
print(a[4])
print(a[:3])      ##  //by default it will start from 0
print(a[-3:-4])    ##  // the output will be empty

## quick quiz

n="harry"

###len of n-4 : len of n-2
## n=5
## 5-4 ,, 5-2 means from 1:3 // 3-1
print(n[-4:-2])

## the len of harry is 5 but when we will count then we count from 0 to 4
print(len(n))