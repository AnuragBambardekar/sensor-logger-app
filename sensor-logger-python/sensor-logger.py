import websocket
import json
import matplotlib.pyplot as plt
import pandas as pd

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)

def on_message(ws, message):
	values = json.loads(message)['values']
	timestamp = json.loads(message)['timestamp']
	x = values[0]
	t1 = timestamp
	y = values[1]
	#t2 = timestamp[1]
	z = values[2]
	#t3 = timestamp[2]

	df = pd.read_json(message)
	print(df.head())
	#df.plot(x='values')
	print('x =',x,'y = ',y,'z = ',z)
	print(t1)
	#plotting(df)

	
	line1, = ax.plot(x, t1, 'r-') # Returns a tuple of line objects, thus the comma
	line2, = ax.plot(y, t1, 'b') # Returns a tuple of line objects, thus the comma
	line3, = ax.plot(z, t1, 'c') # Returns a tuple of line objects, thus the comma

	line1.set_ydata(x)
	line2.set_ydata(y)
	line3.set_ydata(z)

	fig.canvas.draw()
	fig.canvas.flush_events()

""" 	for phase in np.linspace(0, 10*np.pi, 500):
		line1.set_ydata(np.sin(x + phase))
		line2.set_ydata(np.sin(x1 + phase*0.4))
		line3.set_ydata(np.sin(x1 + phase*2)) """
	

""" def plotting(df):
	print(df)
	#plot individual lines
	plt.plot(df['values'])

	#display plot
	plt.show() """

def on_error(ws, error):
    print("error occurred")
    print(error)

def on_close(ws, close_code, reason):
    print("connection close")
    print("close code : ", close_code)
    print("reason : ", reason  )

def on_open(ws):
    print("connection open")
    

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://192.168.1.181:8081/sensor/connect?type=android.sensor.accelerometer",
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
	

    ws.run_forever()
 
 # To analyse multiple sensor data simultaneously, you can add as many websocket connections for different sensors as you want. 
