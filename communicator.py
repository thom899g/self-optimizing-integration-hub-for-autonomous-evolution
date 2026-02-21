import logging
from typing import Dict, Any
import websocket

class Communicator:
    def __init__(self):
        self.websocket = None
        
    def initialize(self) -> None:
        """Initializes the WebSocket connection."""
        try:
            self.websocket.connect("ws://example.com/ws")
            logging.info("Communicator initialized and connected.")
        except Exception as e:
            logging.error(f"Failed to initialize communicator: {str(e)}")
            raise

    def send_message(self, route: str, message: Dict[str, Any]) -> None:
        """Sends a message through the determined route."""
        try:
            if self.websocket:
                self.websocket.send(json.dumps(message))
                logging.info(f"Message sent via WebSocket to {route}")
            else:
                raise ConnectionError("Communicator not initialized")
        except Exception as e:
            logging.error(f"Failed to send message: {str(e)}")

    def receive_message(self) -> Dict[str, Any]:
        """Receives messages from the WebSocket."""
        try:
            message = self.websocket.recv()
            return json.loads(message)
        except Exception as e:
            logging.error(f"Failed to receive message: {str(e)}")