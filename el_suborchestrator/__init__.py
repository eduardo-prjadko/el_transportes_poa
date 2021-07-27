import math

import azure.durable_functions as df

from instances import get_env_var


def orchestrator_function(context: df.DurableOrchestrationContext):
    
    env = get_env_var()
    offset = context.get_input()

    # extract call
    host = env.HOST
    limit = env.LIMIT
    endpoint = env.ENDPOINT.substitute(offset=str(offset), limit=str(limit))
    data = yield context.call_activity('activity_extract', f'{host}{endpoint}')

    # upload to storage
    params = {
        'container': env.CONTAINER, 
        'data': data,
        'index': offset
    }
    yield context.call_activity('activity_upload', input_=params)

    return 'succeeded'

main = df.Orchestrator.create(orchestrator_function)