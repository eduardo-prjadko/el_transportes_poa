import math

import azure.durable_functions as df

from instances import get_env_var


def orchestrator_function(context: df.DurableOrchestrationContext):
    
    env = get_env_var()

    # first extract
    f_data = yield context.call_activity('activity_extract', '')
    f_data['result']['offset'] = 0

    # subsequent extract calls
    offset_list = list(range(100, f_data['result']['total'], 100))
    tasks = []
    for offset in offset_list:
        tasks.append(context.call_activity('el_suborchestrator', offset))

main = df.Orchestrator.create(orchestrator_function)