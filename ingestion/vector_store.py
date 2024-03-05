import datetime

from bytewax.outputs import DynamicOutput, StatelessSink

from qdrant_client.http.models import Distance, VectorParams
from qdrant_client.models import PointStruct
from qdrant_client.http.api_client import UnexpectedResponse

def build_payloads(doc):
    payloads = []
    for chunk in doc.chunks:
        payload = doc.metadata
        payload.update({"text":chunk})
        payloads.append(payload)
    return payloads


class _QdrantVectorSink(StatelessSink):
    
    def __init__(self, client, collection_name):
        self._client=client
        self._collection_name=collection_name

    def write(self, doc):
        _payloads = build_payloads(doc)
        self._client.upsert(
            collection_name=self._collection_name,
            points=[
                PointStruct(
                    id=idx,
                    vector=vector,
                    payload=_payload
                )
                for idx, (vector, _payload) in enumerate(zip(doc.embeddings, _payloads))
            ]
        )


class QdrantVectorOutput(DynamicOutput):
    """Qdrant.

    Workers are the unit of parallelism.

    Can support at-least-once processing. Messages from the resume
    epoch will be duplicated right after resume.

    """
    def __init__(self, collection_name, vector_size, host='localhost', port=6333, client=None):
        self.collection_name=collection_name
        self.vector_size=vector_size
        
        if client:
          self.client = client

        else:
          self.client=QdrantClient(host, port=port)
    
        try: 
            self.client.get_collection(collection_name="test_collection")
        except (UnexpectedResponse, ValueError):
            self.client.recreate_collection(
                collection_name="test_collection",
                vectors_config=VectorParams(size=self.vector_size, distance=Distance.COSINE),
                schema=self.schema
            )

    def build(self, worker_index, worker_count):
        
        return _QdrantVectorSink(self.client, self.collection_name)

flow.output("output", QdrantVectorOutput("test_collection", 384, client=client))