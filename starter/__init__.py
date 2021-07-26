import azure.functions as func
import azure.durable_functions as df


async def main(req: func.TimerRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)
    instance_id = await client.start_new('el_orchestrator', None, None)