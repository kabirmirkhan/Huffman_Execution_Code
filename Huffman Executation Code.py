# To execute Huffman Algorithm the below steps needed

# 1) Get Frequency of data
# 2) Sort by frequency
# 3) Build Tree
# 4) Trace down tree string


text ='abca_abc_ab_a' # Initial value Or user input value
# print('Please enter your text')
# text = input()


get_lenght = len(text)*8

# Define Dictionery
data={}
done = {}
routes = {} # Created after making last part
encodedText = ''

#1) Get Frequency of data 
for i in text.upper():
    if i in data:
        data[i]['val'] = data[i]['val'] + 1 
    else:
        data[i]={'val': 1}

print('Frequncy of charachters')
print(data)

# 2) Sort by frequency
# Sorted from bigger to smallest frequncy
sorted_key = sorted(data, key=lambda x : data[x]['val'], reverse= True) # converted to list
print('sorted list from bigger to small')
print(sorted_key)


# 3) Build Tree

while len(sorted_key) > 1: # 0 Or 1

    
    ak = sorted_key.pop()
    print('remove',ak)
    bk = sorted_key.pop()
    print('remove',bk)
    print(sorted_key)
    akval = data[ak]['val'] # frequency of c
    bkval = data[bk]['val'] # frequency of space
    totalval = bkval + akval
    print(akval,bkval)
    print(totalval)


    done[ak], done[bk] = data[ak], data[bk]
    print(data[ak], data[bk])
    print(done[ak], done[bk])
    del data[ak], data[bk]
    
    data[str(ak + bk)]= {'val': totalval, 'left': ak, 'right': bk}  #A:1 B:1     AB2
    print(data)


    sorted_key = sorted(data, key=lambda x : data[x]['val'], reverse=True)
    done[list(data.keys())[0]] = list(data.values())[0]
    print('\n', sorted_key)
    print('done list')
    print(done) # Print More data


# 4) Trace down tree string
print('\ntrace started')
def trace(currentNode, char, route): # Recursion Function
    
    if 'left' in done[currentNode]:
        print(done)
        print('if left')
        if char in done[currentNode]['left']:
            newRoute = route + '0'
            print('new Route',newRoute)
            print(done[currentNode]['left'],'dwayy rash bkawa')
            trace(done[currentNode]['left'], char, newRoute)

            print(done[currentNode]['left'], char, newRoute,'if 1 after add 0')

    if 'right' in done[currentNode]:
        print('if right')
        if char in done[currentNode]['right']:
            newRoute = route + '1'
            trace(done[currentNode]['right'], char, newRoute)


    if 'left' not in done[currentNode]:
        print('left not in done')
        if 'right' not in done[currentNode]:
            print('right not in done')
            routes[char] = route

            
rootNode = list(data.keys())[0]
print('RootNood')
print(rootNode)

for i in rootNode:
    print(i, 'in rootNode')
    trace(rootNode, i, '')
    
for i in text.upper():
    encodedText += routes[i]
print('\n')
print('Routes:',routes)
print('\n')
print('Encoded Binary text by Huffman Algorithm')
print( encodedText)
print('\nOrigical text with numbers of bits are:',get_lenght)
print('Compression text with numbers of bits are:',len(encodedText))
print('\n')
                  
    
    
