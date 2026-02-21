import logging
from typing import Dict, Any
from ai_module learner import Learner

class Router:
    def __init__(self):
        self.routes = {}
        self.learner = Learner()
        
    def bind_communicator(self, communicator) -> None:
        """Binds the communicator for message sending."""
        self.communicator = communicator
        logging.info("Communicator bound to router successfully.")

    def determine_route(self, message: Dict[str, Any]) -> str:
        """Determines the optimal route based on current state."""
        try:
            # Use learner's model to predict best route
            best_route = self.learner.predict_best_route(message)
            logging.info(f"Route {best_route} selected for message.")
            return best_route
        except Exception as e:
            logging.error(f"Failed to determine route: {str(e)}")
            raise RouteNotFoundException("No active routes available")

    def handle_failure(self, error: Exception) -> None:
        """Handles routing failures by deactivating routes."""
        try:
            # Deactivate the failing route
            failed_route = self._get_route_from_error(error)
            if failed_route:
                self.deactivate_route(failed_route)
                logging.warning(f"Route {failed_route} deactivated due to failure.")
        except Exception as e:
            logging.error(f"Failed to handle routing failure: {str(e)}")

    def _get_route_from_error(self, error: Exception) -> str:
        """