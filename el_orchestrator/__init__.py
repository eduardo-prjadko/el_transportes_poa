import logging

import azure.durable_functions as df

from instances import get_env_var


def orchestrator_function(context: df.DurableOrchestrationContext):
    
    env = get_env_var()

    # get data
    data = yield context.call_activity('activity_extract', '')

    # upload to storage
    params = {
        'container': env.CONTAINER, 
        'data': data
    }
    yield context.call_activity('activity_upload', input_=params)

main = df.Orchestrator.create(orchestrator_function)