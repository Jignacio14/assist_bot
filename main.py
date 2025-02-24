import time
from obswebsocket import obsws, requests, exceptions, events



def main():
    host = "localhost"
    port = "8080"
    
    client = obsws(host, port)
    client.connect()

    respone = None


    response = client.call(requests.GetSceneList())
    if response.status:
        scenes = response.getScenes()
        print("📋 Lista de escenas:")
        print(scenes)    
    else:
        print(f"❌ Error al obtener la lista de escenas: {response.getError()}")

    try:
        respone = client.call(requests.StartRecord())
        print(respone)
        print("📌 Iniciando grabación")
        time.sleep(5)
        respone = client.call(requests.StopRecord())
        print(respone)
        print("📌 Deteniendo grabacion")
    except exceptions.InvalidRequest as e:
        print(f"❌ Error al iniciar grabación: {e}")
        client.disconnect()
        return

    client.disconnect()

if __name__ == "__main__":
    main()