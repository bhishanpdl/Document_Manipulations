
def get_config():
    # config
    openai_api_key = "f4001c4b49a845309d386e9014b7ae6b"
    openai_api_base = "https://qa.gai.cencora.com/aoai"
    azure_endpoint = openai_api_base
    openai_api_version = "2023-03-15-preview"
    openai_api_type = "azure"

    openai_deployment_name = "gpt-35-turbo-16k"
    openai_model_name      = "gpt-35-turbo-16k"

    # os environments
    import os
    os.environ['OPENAI_API_TYPE'] = openai_api_type
    os.environ['OPENAI_API_VERSION'] = openai_api_version
    os.environ['OPENAI_API_BASE'] = openai_api_base
    os.environ['OPENAI_API_KEY'] = openai_api_key

    # openai environments
    import openai
    openai.api_key = openai_api_key
    openai.api_type = openai_api_type
    openai.api_base = openai_api_base
    openai.api_version = openai_api_version
    openai.api_key = openai_api_key

    config = {
    'openai_api_base': openai_api_base,
    'openai_api_version': openai_api_version,
    'deployment_name': openai_deployment_name,
    'model_name': openai_model_name,
    'openai_api_key': openai_api_key,
    'openai_api_type': openai_api_type
    }

    return config

config = get_config()
