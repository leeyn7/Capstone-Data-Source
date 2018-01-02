import re
import time

def activation(data,AssetTypeList,session,directory):
    images = data["features"]
    print "no of images:",len(images)
    asset = re.split("[. :]", AssetTypeList[0])[1]
    for i in range(0,5):
        image_origin_x = images[i]["properties"]["origin_x"]
        image_origin_y = images[i]["properties"]["origin_y"]
        assets_url = images[i]["_links"]["assets"]
        result = session.get(assets_url)
        assets = result.json()
        #print (assets)
        if len(assets)==0:
            print ("cannot be downloaded")
        elif "location" in assets[asset]: # asset is active
            location_url = assets[asset]["location"]
            print (location_url)
            download(image_origin_x,image_origin_y,location_url,directory,session)
        else:#request activation
            activation_url = assets[asset]["_links"]["activate"]
            session.get(activation_url)
            result = session.get(assets_url)
            assets = result.json()
            while True:
                time.sleep(10)
                if assets[asset]["status"] == "active" :
                    location_url = assets[asset]["location"]
                    print (location_url)                                       
                    download(image_origin_x,image_origin_y,location_url,directory,session)
                    break
        

def download(x,y,url,directory,session):
    res = session.get(url)
    filename = "/x-"+ str(x) + "&y-" + str(y)
    with open(str(directory) + filename + ".png", "wb") as f:
        for chunk in res.iter_content(chunk_size=1024):
            if chunk: 
                f.write(chunk)
                f.flush()
    return filename       