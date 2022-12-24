import openai
import random
import pyshorteners as sh


openai.api_key = "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"


def shorten(link):
    s = sh.Shortener()
    tinyurl = s.tinyurl.short(link)
    return(tinyurl)


def image(params):
    response = openai.Image.create(
        prompt=params,
        n=1,
        size="1024x1024"
    )
    image = response['data'][0]['url']
    return(shorten(image))

def name(descr, seed):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Product description:{descr}Seed words:{seed}\nProduct names:",
        temperature=0.8,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return(response["choices"][0]["text"])


def horror(topic):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Topic:{topic}\nTwo-Sentence Horror Story:",
        temperature=0.8,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
    )
    return(response["choices"][0]["text"])


def recipe(ingredients):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Ingredients:{ingredients}\nRecipe:",
        temperature=0.8,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return(response["choices"][0]["text"])


def mood_to_color(mood, seed):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Mood:{mood}Seed words:{seed}\nColors:",
        temperature=0.8,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return(response["choices"][0]["text"])


def friend(text):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"You:{text}\nFriend:",
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
    )
    return(response['choices'][0]['text'])


def convo():
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Human:{text}\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return(response['choices'][0]['text'])