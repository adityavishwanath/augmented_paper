"""
Ensure all the items in requirements.txt are installed.
Replace the Google Cloud Authentication with your own.

Run the script on an image to get data, E.g.:

    ./textindex.py <path-to-image>
"""
import os
os.system("export GOOGLE_APPLICATION_CREDENTIALS=Augmented\ Paper-9554d1f70c3e.json")

import argparse
import base64
import httplib2

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'

def main(photo_file):

    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials,
                              discoveryServiceUrl=DISCOVERY_URL)

    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                },
                'features': [{
                    'type': 'TEXT_DETECTION',
                    'maxResults': 1
                }]
            }]
        })
        response = service_request.execute()
        print response
        return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('image_file', help='The image you\'d like to label.')
    args = parser.parse_args()
    main(args.image_file)