import requests
from lxml import html
from lxml import etree 

import argparse

# Initialize argument parser
parser = argparse.ArgumentParser(description='Compare HTML fetched from a URL XPath against stored HTML.')
parser.add_argument('--url', required=True, help='The URL to fetch HTML from.')
parser.add_argument('--xpath', required=True, help='The XPath to find the HTML element.')
parser.add_argument('--file_path', required=True, help='File path to store and read the HTML for comparison.')

args = parser.parse_args()
URL = args.url
XPATH = args.xpath
FILE_PATH = args.file_path


def fetch_html_by_xpath(url, xpath):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch the URL")
    
    tree = html.fromstring(response.content)
    elements = tree.xpath(xpath)
    
    if len(elements) == 0:
        raise Exception("No element found for the provided XPath")
    
    return etree.tostring(elements[0], pretty_print=True, method="html").decode('utf-8')


def write_html_to_disk(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    # Fetch the new HTML content
    new_content = fetch_html_by_xpath(URL, XPATH)

    # Write the new HTML to disk
    write_html_to_disk(FILE_PATH, new_content)


    

