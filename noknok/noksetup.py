__author__ = 'sinaastani'
import unirest
import json
import boto

conn = boto.connect_s3()

def trainalbum(id,urls):
    response = unirest.post("https://lambda-face-recognition.p.mashape.com/album_train",
    headers={
    "X-Mashape-Key": "mgPzfbOL6FmshydulGDL9nnAlnqmp1a5i3Ejsnc1g4EEWHYxKk",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
    },
params={
    "album": "FriendList",
    "albumkey": "b1ccb6caa8cefb7347d0cfb65146d5e3f84608f6ee55b1c90d37ed4ecca9b273",
    "entryid": id,
    "urls": urls,
    }
    )

def rebuild():
    response = unirest.get("https://lambda-face-recognition.p.mashape.com/album_rebuild?album=FriendList&albumkey=b1ccb6caa8cefb7347d0cfb65146d5e3f84608f6ee55b1c90d37ed4ecca9b273",
    headers={
    "X-Mashape-Key": "mgPzfbOL6FmshydulGDL9nnAlnqmp1a5i3Ejsnc1g4EEWHYxKk",
    "Accept": "application/json"
    }
    )



class facerecog():
    def __init__(self, filepath):
        self.file=filepath

    def search(self):
        response = unirest.post("https://lambda-face-recognition.p.mashape.com/recognize",
        headers={
        "X-Mashape-Key": "mgPzfbOL6FmshydulGDL9nnAlnqmp1a5i3Ejsnc1g4EEWHYxKk",
        },
        params={
        "album": "FriendsList",
        "albumkey": "b1ccb6caa8cefb7347d0cfb65146d5e3f84608f6ee55b1c90d37ed4ecca9b273",
        "files": open(self.file, mode="r")
        })
        successful = response.body["status"]
        # print(response.body)
        if successful == "success":
            print("Match found")
            photoresult=response.body["photos"]
            print(photoresult[0]["tags"][0]["uids"])
            #next=photoresult.index("tags")
            #print(next)

rahulurls = ['https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-xtf1/v/t1.0-9/11112857_398459257000508_1094354056773866063_n.jpg?oh=8aed44b5ebe2c47090f54473abc22bf7&oe=55BDA1FD&__gda__=1436277926_81d29ef151936d502dc1fe88f914bc81', 'https://fbcdn-sphotos-d-a.akamaihd.net/hphotos-ak-xaf1/v/t1.0-9/11096405_398459263667174_8284918708032644790_n.jpg?oh=0dd4b2fc293cc68dbc328373dd5e3d46&oe=55A5217E&__gda__=1437696463_6d8e6c4545a2ff6cca78cb3871f958ef', 'https://scontent.xx.fbcdn.net/hphotos-xfa1/v/t1.0-9/11059975_398459267000507_1599103390278096758_n.jpg?oh=4e43d8d93d67d8f073f9b18d32a98363&oe=55B653F5', 'https://scontent.xx.fbcdn.net/hphotos-xaf1/v/t1.0-9/10570548_398459293667171_4635158739465444357_n.jpg?oh=47121475340e02b4cf37224db030df10&oe=55B6CC57', 'https://scontent.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/10930107_398459313667169_6284145128406133113_n.jpg?oh=e87f35eec4648cfdc45716e5e6b46d54&oe=55AD2E37', 'https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-xpa1/v/t1.0-9/13913_398459327000501_5704586560267313463_n.jpg?oh=03f5fb591d66bb888bd0e2bceea71308&oe=55BCDCD2&__gda__=1436748975_a26a1d538ada50027cb38e6d2b5a0bb4', 'https://scontent.xx.fbcdn.net/hphotos-xft1/v/t1.0-9/11127570_398459340333833_973252894920058705_n.jpg?oh=c626e581605b5df17286c317f110a6d9&oe=55A3AA2D', 'https://scontent.xx.fbcdn.net/hphotos-xpf1/v/l/t1.0-9/62630_398459363667164_2812041615552489586_n.jpg?oh=b65ae3efe365914dd7e79351e2d290fd&oe=55B46B14', 'https://scontent.xx.fbcdn.net/hphotos-xat1/v/t1.0-9/11070138_398459383667162_8554118001346733173_n.jpg?oh=e670c120ebf7ae434bd77b9b83a65742&oe=55A23FA6']
trainalbum("rahul", rahulurls)
sinaurls = ['https://scontent.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/17510_398458813667219_1996971102229569461_n.jpg?oh=379d4f947d9f23485439a5d642825c9c&oe=55B228D7', 'https://scontent.xx.fbcdn.net/hphotos-xpf1/v/t1.0-9/11025122_398458810333886_933925555480007116_n.jpg?oh=c6958b8675fb7fd42985a9ed04cef002&oe=559BFBAA', 'https://scontent.xx.fbcdn.net/hphotos-xpf1/v/t1.0-9/13121_398458803667220_7714471357974792217_n.jpg?oh=726ee8ba21cd2c3fec354e22685a6e83&oe=559F43E0', 'https://scontent.xx.fbcdn.net/hphotos-xtp1/v/t1.0-9/11138653_398458850333882_4859806782357244926_n.jpg?oh=2a7227ba02e96e3be088344efd6f9bd9&oe=559828A7', 'https://scontent.xx.fbcdn.net/hphotos-xpa1/v/t1.0-9/11110455_398458853667215_5020502114421751612_n.jpg?oh=0c5ddea22def07cc679b271dbbbe9468&oe=55BA192D', 'https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-xpa1/v/t1.0-9/11102664_398458857000548_7798421133594483900_n.jpg?oh=dfbbeb2b8a0cb850f4fb405c0e661fcd&oe=55B16B1F&__gda__=1438226855_e2342c545fba5516fda34fba991fb715', 'https://fbcdn-sphotos-c-a.akamaihd.net/hphotos-ak-xpf1/v/t1.0-9/10984087_398458903667210_4471422237995139988_n.jpg?oh=716fda8996643a3043802c15a446c1b0&oe=55A546C6&__gda__=1438427308_6f5d2bf637e6c31f8e28b39d7352c1ad', 'https://scontent.xx.fbcdn.net/hphotos-xtf1/v/t1.0-9/11053455_398458923667208_6196267633790099987_n.jpg?oh=723abc3e8344ebdfa85e28529b4d991d&oe=55BC60B6']
trainalbum("sina", sinaurls)
watsonurls = ['https://scontent.xx.fbcdn.net/hphotos-xtp1/v/t1.0-9/11069398_398459040333863_7591723110563808613_n.jpg?oh=e08a04de1392323c289a753165ebc1cf&oe=55A9482D', 'https://scontent.xx.fbcdn.net/hphotos-xtf1/v/t1.0-9/1780900_398459043667196_5251710080087327400_n.jpg?oh=fdbcfbc0ac8c7d98f330fe98f0aa26ba&oe=55A54311', 'https://scontent.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/10999562_398459047000529_1255661424602833448_n.jpg?oh=fa2ae173bdb72a12d7c8940123a00546&oe=55AC9D1F', 'https://scontent.xx.fbcdn.net/hphotos-xap1/v/t1.0-9/11133749_398459077000526_784683462441242300_n.jpg?oh=414b521a665ebaed0e4b3a6a0a0c605e&oe=559944D8', 'https://fbcdn-sphotos-e-a.akamaihd.net/hphotos-ak-xpa1/v/t1.0-9/10456255_398459120333855_9033372345631970460_n.jpg?oh=6f887e1a6b90dabfcab5d9072af03a1e&oe=55A51181&__gda__=1436319545_4d89731b740a507642dda29c9cb4b982', 'https://fbcdn-sphotos-b-a.akamaihd.net/hphotos-ak-xap1/v/t1.0-9/11136693_398459127000521_8694164304852164603_n.jpg?oh=f8131bb7159b06019feba0c6c71a4faa&oe=55A8586E&__gda__=1436234162_68b6b06e4ab9e89ba63068a5a42fea7c', 'https://scontent.xx.fbcdn.net/hphotos-xta1/v/t1.0-9/11091198_398459123667188_7266051520082000365_n.jpg?oh=08fe99f90af138ef46ac7c69cec6d82c&oe=55AE30E4', 'https://scontent.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/10614347_398459160333851_2081383394505314256_n.jpg?oh=f15feadced4a489665b4506c87fff4ca&oe=559CE435']
trainalbum("watson", watsonurls)
paturls = ['https://scontent.xx.fbcdn.net/hphotos-xpa1/v/t1.0-9/17510_398457620334005_7109916782887877366_n.jpg?oh=e87ba1e8cd8e932e975815414f10d88f&oe=55B3C1F6', 'https://fbcdn-sphotos-a-a.akamaihd.net/hphotos-ak-xfa1/v/t1.0-9/11096571_398457623667338_575477992654348355_n.jpg?oh=589f3ff3133581e2f993787373817d3d&oe=55B4C3A8&__gda__=1437344248_a93c6077f8e8835b5ee4a40288956efc','https://scontent.xx.fbcdn.net/hphotos-xfp1/v/t1.0-9/18920_398457627000671_3362207778522725261_n.jpg?oh=8ca16dbb2f298ebfdfe862e12f579a00&oe=55A7F2E7', 'https://scontent.xx.fbcdn.net/hphotos-xtf1/v/t1.0-9/11128760_398457657000668_344781895452950803_n.jpg?oh=5446722787f5ab8b0553960e74e8de7a&oe=55B64BB9', 'https://scontent.xx.fbcdn.net/hphotos-xft1/v/t1.0-9/11120538_398457653667335_2235374426805719285_n.jpg?oh=24e956b2ca6d3142c851538386af0db4&oe=55BD8A15', 'https://fbcdn-sphotos-f-a.akamaihd.net/hphotos-ak-xap1/v/t1.0-9/10380751_398457667000667_5959681496253802643_n.jpg?oh=4cacd2226e44a67a44ac8227b3076032&oe=559A11BB&__gda__=1437819751_a542218f37d270b6292b5803e7886eed', 'https://scontent.xx.fbcdn.net/hphotos-xpt1/v/t1.0-9/11074169_398457700333997_4254867216829779217_n.jpg?oh=ccf30270d5cbb44300e24f7da61dd55e&oe=55BC7F5A', 'https://scontent.xx.fbcdn.net/hphotos-xfp1/v/l/t1.0-9/10425415_398457703667330_212693729524705060_n.jpg?oh=82273575f418534c452174528b28b914&oe=55AA8D72']
trainalbum("pat", paturls)


#Make a new file for the actual implementation of the code? (Actually waiting for camera, exporting to AWS, pulling file from AWS, run search method

#testpic = unirest.get() #FIXME: add http GET to retrieve object from Amazon AWS

x = facerecog("/Users/Rahul/Desktop/rahul/rahul1.jpg")
x.search()