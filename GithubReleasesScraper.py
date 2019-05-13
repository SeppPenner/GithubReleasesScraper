import requests
import json
import sys
import datetime

filePath = 'result.md'
projects = [['OutlookCaldavSynchronizer', 'https://api.github.com/repos/aluxnimm/outlookcaldavsynchronizer/releases/latest'],
            ['AspNetCore', 'https://api.github.com/repos/aspnet/AspNetCore/releases/latest']]

def getRelease(url: str):
    "Gets a release from the given urls"
    response = requests.get(url)
    jsonData = json.loads(response.content.decode())
    data = []
    tag = jsonData['name']
    tagUrl = jsonData['html_url']
    publishedAt = jsonData['published_at']
    publishedAtDate = datetime.datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
    print('Tag: ' + tag)
    print('Tag-Url: ' + tagUrl)
    print('Published at: ' + f"{publishedAtDate:%d.%m.%Y}")
    return(tag, tagUrl, f"{publishedAtDate:%d.%m.%Y}")

def getReleases(projects):
    "Gets the releases for all given urls and writes them to a markdown results file"
    with open(filePath, 'w') as f:
        f.write('# Projects\n\n')
        f.write('|Project name|Tag|Tag-Url|Published at|\n')
        f.write('|-|-|-|-|\n')
        for project in projects:
            tag, tagUrl, publishedAt = getRelease(project[1])
            f.write(project[0] + '|' + tag + '|[' + project[0] + '](' + tagUrl + ')|' + publishedAt + '|\n')

getReleases(projects)