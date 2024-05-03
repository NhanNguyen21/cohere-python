import os
import unittest

import cohere

co = cohere.BedrockClient(
    timeout=10000,
    aws_region="us-east-1",
    chat_model="cohere.command-r-plus-v1:0",
    embed_model="cohere.embed-multilingual-v3",
    generate_model="cohere.command-text-v14",
)

package_dir = os.path.dirname(os.path.abspath(__file__))
embed_job = os.path.join(package_dir, 'embed_job.jsonl')


class TestClient(unittest.TestCase):
    def test_generate(self) -> None:
        response = co.generate(
            prompt='Please explain to me how LLMs work',
        )
        print(response)

    def test_generate_stream(self) -> None:
        response = co.generate_stream(
            prompt='Please explain to me how LLMs work',
        )
        for event in response:
            if event.event_type == "text-generation":
                print(event.text, end='')