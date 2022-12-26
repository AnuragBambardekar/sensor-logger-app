import csv
import socket
from socket import *
import json
import pandas as pd

serverIP = "192.168.1.49"
serverPort = 8000
response =  b"HTTP/1.1 200 OK"
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverIP, serverPort))
serverSocket.listen(1) #listen to 1 client

# TCP Server
print("The server is listening on PORT 8000")

while True:
    connectionSocket, address = serverSocket.accept()
    print(f"Connected to {address}")
    
    data = connectionSocket.recv(2048).decode('utf-8')
    print(f"client Sent :\n {data}")
    print("")

    print("Parsed Data:")
    data = data[data.find('{'):]
    print(data)
    print('')
    print(type(data)) #<class 'str'>

    #converting str to JSON
    jsonObject = json.loads(data) 

    print (jsonObject)  
    print (type(jsonObject))  
    print("")

    
    import pandas as pd

    vals=[]
    for i in jsonObject.items():
        vals.append([i[0],i[1]])
    
    
    x = pd.DataFrame(vals,columns=['key','v'])

    #flatten the lists
    x = x.explode('v')

    #convert to json object
    n = x.to_json(orient="records")

    #load the json object
    j = json.loads(n)

    #normalize
    norm = pd.json_normalize(j)

    #drop the first 3 rows
    drop = norm.drop([0,1,2])
    
    #rename the columns
    finalD = drop.rename(columns={
        "key":"data",
        "v":"values", "v.name":"sensor", "v.accuracy":"accuracy",
        "v.values.x":"x", "v.values.y":"y", "v.values.z":"z", "v.time":"time"
    })
    print(finalD)

    #Run the program thrice to record 3 distinguishable activities (along three axes) by uncommenting each line at a time correspondingly
    #csv_data = finalD.to_csv (r'C:/Users/anura/Documents/VSCode_Workspace/ML4IoT/Assignment_3/TEST_folder/activity1X.csv', mode='a', index=False, header=False)
    #csv_data = finalD.to_csv (r'C:/Users/anura/Documents/VSCode_Workspace/ML4IoT/Assignment_3/TEST_folder/activity2Y.csv', mode='a', index=False, header=False)
    csv_data = finalD.to_csv (r'C:/Users/anura/Documents/VSCode_Workspace/ML4IoT/Assignment_3/TEST_folder/activity3Z.csv', mode='a', index=False, header=False)
    
    print("Data Collection Complete")
    connectionSocket.sendall(response)
    
    connectionSocket.close()

