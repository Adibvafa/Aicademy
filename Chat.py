"""
Chat.py
-----------------
Answers users question in the chat
"""

import os
import openai

openai.api_key = "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"

from PIL import Image
import requests
from io import BytesIO


def Answer_Question(user_input, user_question):
    """
    Returns list of paragraphs, and list of images for index 0 and -3
    :param user_input: Input of user to create the course
    :param user_question: Question of user in the chat
    """
    prompt = f"""User has asked {user_input} and you created a course based on it.
    Now user has asked {user_question}. Provide accurate clear answer."""

    answer_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=250,
        top_p=0.95,
    )
    answer = answer_response["choices"][0]["message"]["content"]
    return answer.strip()
