import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write an email to my boss for resignation?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)
'''
{
  "warning": "This model version is deprecated. Migrate before January 4, 2024 to avoid disruption of service. Learn more https://platform.openai.com/docs/deprecations",
  "id": "cmpl-8R5nc7cPTfjp5e9vA1Ge8CmL4MrVf",
  "object": "text_completion",
  "created": 1701467840,
  "model": "text-davinci-003",
  "choices": [
    {
      "text": "\n\nSubject: Resignation\n\nDear [Boss Name],\n\nI am writing to inform you of my intention to resign from my current position at [Company Name]. After careful consideration, I have decided that it is time for me to move on and pursue new challenges.\n\nI am extremely grateful for the opportunity I was given here and I have enjoyed every moment of my employment. I have learned a great deal while here and I am confident that I am leaving with increased knowledge and skills.\n\nMy last day of work will be [date]. I am eager to assist with the transition process and make sure that all of my current responsibilities are properly handled before I depart.\n\nThank you again for the opportunity to work here.\n\nSincerely,\n\n[Your Name]",
      "index": 0,
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 162,
    "total_tokens": 171
  }
}
'''