from havenondemand.hodclient import *
client = HODClient("66578e7c-030d-4105-9a07-adb7a05bb0f6", version="v1")

text_string="I need a Facebook Ad for advertising LipMe discount on MAC Matte lipstick"



params = {'text': text_string}
response_async = client.post_request(params, HODApps.ENTITY_EXTRACTION, async=True)
print response_async


image_url="http://www.html5canvastutorials.com/demos/assets/darth-vader.jpg"
