#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  26 09:12:35 2020

@author: sachinmcreddy
"""

import requests
import json

def repo_info(user_name='SachinMCReddy'):
    output = []
    user_url = 'https://api.github.com/users/{}/repos'.format(user_name)
    res = requests.get(user_url)
    repos = json.loads(res.text)
    output.append('User: {}'.format(user_name))

    try:
        repos[0]['name']
    except (TypeError, KeyError, IndexError):
        return 'not able to fetch repos from user'

    try:
        for repo in repos:
            repo_name = repo['SSW-567']
            repo_url = 'https://api.github.com/repos/{}/{}/commits'.format(user_name, repo_name)
            repo_info = requests.get(repo_url)
            repo_info_json = json.loads(repo_info.text)
            output.append('Repo: {} Number of commits: {}'.format(repo_name, len(repo_info_json)))
    except (TypeError, KeyError, IndexError):
        return 'not able to fetch commits from repo'
    return output

if __name__ == '__main__':
    for entry in repo_info():
        print(entry)