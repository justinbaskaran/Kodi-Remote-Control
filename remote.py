#! /usr/bin/python3
from tkinter import *
from tkinter.ttk import Separator, Style,Treeview
import requests
import json
import urllib
 
playlist=[];

def main():
    setupGUI()
    

def play():
    headers = {'content-type': 'application/json'}
    

    xbmc_host = 'xxx.xxx.xx.xx'

    xbmc_port = 8080
    

    xbmc_json_rpc_url = "http://" + xbmc_host + ":" + str(xbmc_port) + "/jsonrpc"
    
    payload = {"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}

    url_param = urllib.parse.urlencode({'request': json.dumps(payload)})
    
    response = requests.get(xbmc_json_rpc_url + '?' + url_param, headers=headers)
    
    data = json.loads(response.text)
https://github.com/justinbaskaran/Kodi-Remote-Control.git
    if data['result']:

        player_id = data['result'][0]["playerid"]
    
        payload = {"jsonrpc": "2.0", "method": "Player.PlayPause", 
                "params": { "playerid": player_id }, "id": 1}
        response = requests.post(xbmc_json_rpc_url, data=json.dumps(payload), headers=headers)

def vUp():
    headers = {'content-type': 'application/json'}
    
    xbmc_host = 'xxx.xxx.xx.xx'
    
    xbmc_port = 8080

    xbmc_json_rpc_url = "http://" + xbmc_host + ":" + str(xbmc_port) + "/jsonrpc"

    payload = {"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}

    url_param = urllib.parse.urlencode({'request': json.dumps(payload)})

    response = requests.get(xbmc_json_rpc_url + '?' + url_param, headers=headers)

    data = json.loads(response.text)

    if data['result']:

        player_id = data['result'][0]["playerid"]

        payload = {"jsonrpc": "2.0", "method": "Application.SetVolume", "params": { "volume": "increment" }, "id": 1}
        response = requests.post(xbmc_json_rpc_url, data=json.dumps(payload), headers=headers)
 
def vDown():
    headers = {'content-type': 'application/json'}
    

    xbmc_host = 'xxx.xxx.xx.xx'

    xbmc_port = 8080


    xbmc_json_rpc_url = "http://" + xbmc_host + ":" + str(xbmc_port) + "/jsonrpc"

    payload = {"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}

    url_param = urllib.parse.urlencode({'request': json.dumps(payload)})

    response = requests.get(xbmc_json_rpc_url + '?' + url_param, headers=headers)

    data = json.loads(response.text)

    if data['result']:

        player_id = data['result'][0]["playerid"]

        payload = {"jsonrpc": "2.0", "method": "Application.SetVolume", "params": { "volume": "decrement" }, "id": 1}

        response = requests.post(xbmc_json_rpc_url, data=json.dumps(payload), headers=headers)
 
def lChannel():
    headers = {'content-type': 'application/json'}
    

    xbmc_host = 'xxx.xxx.xx.xx'

    xbmc_port = 8080


    xbmc_json_rpc_url = "http://" + xbmc_host + ":" + str(xbmc_port) + "/jsonrpc"

    payload = {"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}

    url_param = urllib.parse.urlencode({'request': json.dumps(payload)})

    response = requests.get(xbmc_json_rpc_url + '?' + url_param, headers=headers)

    data = json.loads(response.text)

    if data['result']:

        player_id = data['result'][0]["playerid"]

        payload = {"jsonrpc":"2.0","method":"Player.GoTo","params":{"playerid":1,"to":"previous"},"id":1} 
        response = requests.post(xbmc_json_rpc_url, data=json.dumps(payload), headers=headers)
 
def nChannel():
    headers = {'content-type': 'application/json'}
    

    xbmc_host = 'xxx.xxx.xx.xx'

    xbmc_port = 8080


    xbmc_json_rpc_url = "http://" + xbmc_host + ":" + str(xbmc_port) + "/jsonrpc"

    payload = {"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}

    url_param = urllib.parse.urlencode({'request': json.dumps(payload)})

    response = requests.get(xbmc_json_rpc_url + '?' + url_param, headers=headers)

    data = json.loads(response.text)

    if data['result']:

        player_id = data['result'][0]["playerid"]

        payload = {"jsonrpc":"2.0","method":"Player.GoTo","params":{"playerid":1,"to":"next"},"id":1} 
        response = requests.post(xbmc_json_rpc_url, data=json.dumps(payload), headers=headers)

def getPlaylist():
    headers = {'content-type': 'application/json'}
    

    xbmc_host = 'xxx.xxx.xx.xx'

    xbmc_port = 8080


    xbmc_json_rpc_url = "http://" + xbmc_host + ":" + str(xbmc_port) + "/jsonrpc"

    payload = {"jsonrpc":"2.0","id":"1","method":"Playlist.GetItems","params":{"playlistid":1}}

    url_param = urllib.parse.urlencode({'request': json.dumps(payload)})

    response = requests.get(xbmc_json_rpc_url + '?' + url_param, headers=headers)

    data1 = json.loads(response.text)

    #print(data1)

    print(data1['result']['items'])

    names = []


    for item in data1['result']['items']:
       # print (item.get('label'))
        names.append(item.get('label'))

    return names    


    

   
        

def setupGUI():
    root = Tk()
    root.geometry("1000x350") 
    root.title('Kodi Remote')
    #root.resizable(width=False, height=False)

    frame = Frame(root, width=350, height=500)
    frame.pack(side=LEFT, fill=X, expand=1, anchor=N)


    volumeUP = Button(frame, text="VOLUME UP", width=10, height = 7 , command=vUp)
    volumeUP.grid(row=1, column=2)

    previousVid = Button(frame, text="PREVIOUS VIDEO", width=10, height = 7 , command=lChannel)
    previousVid.grid(row=2, column=1)

    volumeDwn = Button(frame, text="VOLUME DOWN", width=10, height = 7, command=vDown)
    volumeDwn.grid(row=3, column=2)

    nextVideo = Button(frame, text="NEXT VIDEO", width=10, height = 7, command=nChannel)
    nextVideo.grid(row=2, column=3)

    playPause = Button(frame, text="PLAY/PAUSE", width=10, height = 7, command=play)
    playPause.grid(row=2, column=2)



    bottomframe = Frame(root)
    bottomframe.config(height = 350, width =500)
    bottomframe.pack( side = RIGHT )

    playlist = getPlaylist()

    addURLBox = Entry(bottomframe , width=60)
    addURLBox.grid(row=1, column=0)

    tree =Treeview(bottomframe, column=("col1"), show="headings")
    tree.heading('#1', text='Name')
    for x in playlist:
        print(x)
        tree.insert("",0,values=(x))
    tree.grid(row=2, column=0)


    addURLBtn = Button(bottomframe, text="ADD TO PLAYLIST" , command =lambda:add(addURLBox.get(),bottomframe,tree,playlist))
    addURLBtn.grid(row=1, column=1)

    
    



    root.mainloop()

def reload(bottomFrame,tree,playlist):
    tree.delete(*tree.get_children())
    for x in playlist:
        print(x)
        tree.insert("",0,values=(x))
    


def add(test,bottomFrame,tree,playlist):
    headers = {'content-type': 'application/json'}
    

    xbmc_host = 'xxx.xxx.xx.xx'

    xbmc_port = 8080


    xbmc_json_rpc_url = "http://" + xbmc_host + ":" + str(xbmc_port) + "/jsonrpc"

    payload = {"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id": 1}

    url_param = urllib.parse.urlencode({'request': json.dumps(payload)})

    response = requests.get(xbmc_json_rpc_url + '?' + url_param, headers=headers)

    data = json.loads(response.text)

    if data['result']:

        player_id = data['result'][0]["playerid"]

        payload = {"jsonrpc":"2.0","id":1,"method":"Playlist.Add","params":{"playlistid":1,"item":{"file":test}}} 
        if (test !=""):
            response = requests.post(xbmc_json_rpc_url, data=json.dumps(payload), headers=headers)
            playlist = getPlaylist()
            reload(bottomFrame,tree,playlist);
        

if __name__== "__main__":
      main()