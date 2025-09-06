from core.prefect.flows.polars import polars_pipeline

def orchestrate_pipelines(sources: dict):
    results = {}
    for name, info in sources.items():
        if info[1] == "csv":
            results[name] = polars_pipeline(info[0])
        else:
            results[name] = {"error": f"Unsupported type {info[1]}"}
    return results
