import os
from langfuse import Langfuse

# Singleton client instance
_langfuse_instance = None

def get_langfuse_client() -> Langfuse:
    global _langfuse_instance
    if _langfuse_instance is None:
        _langfuse_instance = Langfuse(
            public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
            secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
            host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
        )
    return _langfuse_instance

def log_evaluation_score(trace_id: str, name: str, score: float, comment: str = None):
    """
    Submits an evaluation metric directly to a trace in Langfuse.
    """
    client = get_langfuse_client()
    client.score(
        trace_id=trace_id,
        name=name,
        value=score,  # Value between 0.0 and 1.0 (or custom range)
        comment=comment
    )
    client.flush()