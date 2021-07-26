import math

import azure.durable_functions as df

from instances import get_env_var


def orchestrator_function(context: df.DurableOrchestrationContext):
    
    env = get_env_var()

    # first extract call
    f_data = yield context.call_activity('activity_extract', '')
    f_data['result']['offset'] = 0

    # subsequent extract calls
    pages = math.ceil(f_data['result']['total'] / 100)
    i = 1
    tasks = []
    offset = 100
    while i <= pages:
        endpoint = f'/api/3/action/datastore_search?offset={str(offset)}&resource_id=cb96a73e-e18b-4371-95c5-2cf20e359e6c'
        tasks.append(context.call_activity('activity_extract', endpoint))
        i += 1
        offset += 100
    data = yield context.task_all(tasks)
    data.append(f_data)

    # upload to storage
    tasks = []
    for item in data:
        params = {
            'container': env.CONTAINER, 
            'data': item,
            'index': item['result']['offset']
        }
        tasks.append(context.call_activity('activity_upload', input_=params))
    yield context.task_all(tasks)

main = df.Orchestrator.create(orchestrator_function)