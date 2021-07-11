'''Data retrieved from open trivia database'''

import requests


def get_questions(category, difficulty):
    response = requests.get('https://opentdb.com/api.php', params={'amount':10, 'type':'boolean', 'category': category, 'difficulty': difficulty})
    response.raise_for_status()
    return response.json()['results']