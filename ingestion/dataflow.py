import os
import json
from loguru import logger

from bytewax.dataflow import Dataflow
from bytewax.inputs import DynamicInput, StatelessSource
from websocket import create_connection

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# receives data from the websocket
class AlpacaSource(StatelessSource):
    def __init__(self, worker_tickers):
        self.worker_tickers = worker_tickers

        # establish a websocket connection to alpaca
        self.ws = create_connection("")
        logger.info(self.ws.recv())

        # authenticate to the websocket
        self.ws.send(
            json.dumps(
                {"action":"auth",
                 "key":f"{API_KEY}",
                 "secret":f"{API_SECRET}"}
            )
        )
        logger.info(self.ws.recv())
        
        # subscribe to the tickers
        self.ws.send(
            json.dumps(
                {"action":"subscribe","news":self.worker_tickers}
            )
        )
        logger.info(self.ws.recv())

    def next(self):
        return self.ws.recv()

# DynamicInput is the entrypoint of our input
class AlpacaNewsInput(DynamicInput):
    """
    Input class to receive streaming news data from
    the Alpaca real-time news API.

    Args:
        tickers: list - should be a list of tickers
    """

    def __init__(self, tickers):
        self.TICKERS = tickers

    # splits tickers over the workers and parallelize the requests
    def build(self, worker_index, worker_count):
        prods_per_worker = int(len(self.TICKERS) / worker_count)
        worker_tickers = self.TICKERS[
            int(worker_index * prods_per_worker) : int(
                worker_index * prods_per_worker + prods_per_worker
            )
        ]
        return AlpacaSource(worker_tickers)


flow = Dataflow()
flow.input("input", AlpacaNewsInput(tickers=["*"]))
flow.inspect(print)

