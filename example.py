from tkinter import *
from tkinter.ttk import Separator, Style,Treeview
import requests
import json
import urllib
 
# #Required header for XBMC JSON-RPC calls, otherwise you'll get a 
# #415 HTTP response code - Unsupported media type
# headers = {'content-type': 'application/json'}
 
# #Host name where XBMC is running, leave as localhost if on this PC
# #Make sure "Allow control of XBMC via HTTP" is set to ON in Settings -> 
# #Services -> Webserver
# xbmc_host = '153.106.89.75'
 
# #Configured in Settings -> Services -> Webserver -> Port
# xbmc_port = 8080
 
# #Base URL of the json RPC calls. For GET calls we append a "request" URI 
# #parameter. For POSTs, we add the payload as JSON the the HTTP request body
# xbmc_json_rpc_url = "http://" + xbmc_host + ":" + str(xbmc_port) + "/jsonrpc"
 
# #Payload for the method to get the currently playing / paused video or audio
# payload = {"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}

# url_param = urllib.parse.urlencode({'request': json.dumps(payload)})
 
# response = requests.get(xbmc_json_rpc_url + '?' + url_param, 
#                         headers=headers)
 
# #response.text will look like this if something is playing
# #{"id":1,"jsonrpc":"2.0","result":[{"playerid":1,"type":"video"}]}
# #and if nothing is playing:
# #{"id":1,"jsonrpc":"2.0","result":[]}
     
# data = json.loads(response.text)
# #result is an empty list if nothing is playing or paused. 
# if data['result']:
#     #We need the specific "playerid" of the currently playing file in order 
#     #to pause it
#     player_id = data['result'][0]["playerid"]
 
#     payload = {"jsonrpc": "2.0", "method": "Player.PlayPause", 
#                "params": { "playerid": player_id }, "id": 1}
#     response = requests.post(xbmc_json_rpc_url, data=json.dumps(payload), headers=headers)
     


#     #response.text will look like this if we're successful:
#     #{"id":1,"jsonrpc":"2.0","result":{"speed":0}}




root = Tk()
root.geometry("850x350") 
root.title('Kodi Remote')
#root.resizable(width=False, height=False)

frame = Frame(root, width=350, height=500)
frame.pack(side=LEFT, fill=X, expand=1, anchor=N)

volumeUP = Button(frame, text="VOLUME UP", width=10, height = 7)
volumeUP.grid(row=1, column=2)

previousVid = Button(frame, text="PREVIOUS VIDEO", width=10, height = 7)
previousVid.grid(row=2, column=1)

volumeDwn = Button(frame, text="VOLUME DOWN", width=10, height = 7)
volumeDwn.grid(row=3, column=2)

nextVideo = Button(frame, text="NEXT VIDEO", width=10, height = 7)
nextVideo.grid(row=2, column=3)

playPause = Button(frame, text="PLAY/PAUSE", width=10, height = 7)
playPause.grid(row=2, column=2)



bottomframe = Frame(root)
bottomframe.config(height = 350, width =500)
bottomframe.pack( side = RIGHT )

text = Text(bottomframe)
text.insert(END,'Enter URL to Add:')
text.grid(row=0, column=0)
text.config(state=DISABLED)

e = Entry(bottomframe)
e.grid(row=1, column=0)

tv = Treeview(bottomframe)
tv['columns']=['Name','url']
tv.heading('#0', text='Name')
tv.column('#0', anchor='center', width=100)

tv.heading('#1', text='URL')
tv.column('#1', anchor='center', width=420)
tv.grid(row=4, columnspan=4, sticky='nsew')
tv.grid(sticky = (N,S))


root.mainloop()


