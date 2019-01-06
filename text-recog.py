import io

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient.from_service_account_json(r'''C:\Users\Saurabh Gupta\Desktop\My First Project-80353a5f126d.json''')

    # [START vision_python_migration_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))



detect_text(r'''C:\Users\Saurabh Gupta\Desktop\seven_300x300_2fcd56e7-0dd8-4061-a341-120c666e2907.png''')
