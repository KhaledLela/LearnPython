import json

from dotenv import load_dotenv

from item.item_handler import item_prompt
from quote.quote_handler import quote_prompt

# Load environment variables from .env file
load_dotenv()


def lambda_handler(event, context):
    source = event['source'] or ''
    content = source['text'] if isinstance(source, dict) else source
    if check_token_limit(content):
        # Call Lambda function invokeSummarizeFunction
        summary_results = invokeSummarizeFunction(content)
        intermediate_steps: list = summary_results['intermediate_steps']
        content = '\n'.join(intermediate_steps)
        if check_token_limit(content):
            content = summary_results['output_text']

        if isinstance(source, dict):
            source['text'] = content
        else:
            source = content

    action_type = event.get('action_type')
    if action_type != 'quote':
        return item_prompt(event)
    else:
        return quote_prompt(event)


def check_token_limit(source):
    source_count = len(source.split())
    print(f"transcript_count:{source_count}")
    return source_count > 1024


def invokeSummarizeFunction(source):
    # Create a boto3 client for invoking Lambda functions
    client = boto3.client('lambda')
    # Invoke another Lambda function asynchronously
    response = client.invoke(
        FunctionName='nk3-transcription-summarize',
        Payload=json.dumps({'source': source})
    )
    return response.json()


event = {"action_type": "prompt", "prompt": "curriculum of ml", "source": ""}
lambda_handler(event, None)
