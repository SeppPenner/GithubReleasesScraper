GithubReleasesScraper
====================================

GithubReleasesScraper is a script to get the releases of a Github project in a markdown formatted file.
GithubReleasesScraper is written and tested in Python 3.7.3

[![Build status](https://ci.appveyor.com/api/projects/status/g3pp8gxx5ywjxxnt?svg=true)](https://ci.appveyor.com/project/SeppPenner/githubreleasesscraper)
[![GitHub issues](https://img.shields.io/github/issues/SeppPenner/GithubReleasesScraper.svg)](https://github.com/SeppPenner/GithubReleasesScraper/issues)
[![GitHub forks](https://img.shields.io/github/forks/SeppPenner/GithubReleasesScraper.svg)](https://github.com/SeppPenner/GithubReleasesScraper/network)
[![GitHub stars](https://img.shields.io/github/stars/SeppPenner/GithubReleasesScraper.svg)](https://github.com/SeppPenner/GithubReleasesScraper/stargazers)
[![GitHub license](https://img.shields.io/badge/license-AGPL-blue.svg)](https://raw.githubusercontent.com/SeppPenner/GithubReleasesScraper/master/License.txt)
[![Known Vulnerabilities](https://snyk.io/test/github/SeppPenner/GithubReleasesScraper/badge.svg)](https://snyk.io/test/github/SeppPenner/GithubReleasesScraper)

## Basic usage
1. Adjust the `projects` sections in the [GithubReleasesScraper.py](https://github.com/SeppPenner/GithubReleasesScraper/blob/master/GithubReleasesScraper.py) file.
2. Install the requirements using `pip3 install -r requirements.txt`, `install.sh` or `install.bat`.
3. Run the project using `python LoadGames.py`, `run.sh` or `run.bat`.

## The result
The result looks like this:

```markdown
# Projects

|Project name|Tag|Tag-Url|Published at|
|-|-|-|-|
OutlookCaldavSynchronizer|3.6.1|[OutlookCaldavSynchronizer](https://github.com/aluxnimm/outlookcaldavsynchronizer/releases/tag/v3.6.1)|23.04.2019|
AspNetCore|v2.2.4|[AspNetCore](https://github.com/aspnet/AspNetCore/releases/tag/v2.2.4)|09.04.2019|
```

Check the file [result.md](https://github.com/SeppPenner/GithubReleasesScraper/blob/master/result.md), too.

## Further links
* https://developer.github.com/v3/repos/releases/

Change history
--------------

* **Version 1.0.0.0 (2018-05-13)** : 1.0 release.