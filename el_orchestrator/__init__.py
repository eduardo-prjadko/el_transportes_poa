import azure.durable_functions as df

from instances import get_env_var


def orchestrator_function(context: df.DurableOrchestrationContext):

    env = get_env_var()

    # first extract and load
    host = env.HOST
    limit = env.LIMIT
    endpoint = env.ENDPOINT.substitute(offset=str(0), limit=str(limit))
    data = yield context.call_activity('activity_extract', f'{host}{endpoint}')
    params = {
        'container': env.CONTAINER, 
        'data': data,
        'index': 0
    }
    yield context.call_activity('activity_upload', input_=params)

    # suborchestrator call
    offset_list = list(range(int(limit), data['result']['total'], int(limit)))
    tasks = []
    for offset in offset_list:
        tasks.append(context.call_sub_orchestrator('el_suborchestrator', offset ))
    
    yield context.task_all(tasks)

    return 'succeeded'

main = df.Orchestrator.create(orchestrator_function)