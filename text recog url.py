import io
from google.cloud import vision
from google.cloud.vision import types

client = vision.ImageAnnotatorClient.from_service_account_json(r'''C:\Users\Saurabh Gupta\Desktop\My First Project-80353a5f126d.json''')
image = vision.types.Image()
image.source.image_uri = 'https://www.homemade-gifts-made-easy.com/image-files/xnewspaper-generator-katie-nicholson-old-800x659.jpg.pagespeed.ic.RUacjZ59bD.jpg'
resp = client.text_detection(image=image)
print('\n'.join([d.description for d in resp.text_annotations]))
