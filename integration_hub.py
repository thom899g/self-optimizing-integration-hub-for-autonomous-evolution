import logging
from typing import Dict, Any
from ai_module communicator import Communicator
from ai_module router import Router
from ai_module learner import Learner
from monitoring.monitor import Monitor

class IntegrationHub:
    def __init__(self):
        self.communicator = Communicator()
        self.router = Router()
        self.learner = Learner()
        self.monitor = Monitor()
        
    def initialize_components(self) -> None:
        """Initializes all components and sets up necessary connections."""
        try:
            self communicatior.initialize()
            self.router.bind_communicator(self communicator)
            self.learner.connect_to_knowledge_base()
            self.monitor.start_monitoring()
            logging.info("All components initialized successfully.")
        except Exception as e:
            logging.error(f"Failed to initialize components: {str(e)}")
            raise

    def process_message(self, message: Dict[str, Any]) -> None:
        """Processes incoming messages and routes them appropriately."""
        try:
            # Use router to determine the best path
            route = self.router.determine_route(message)
            
            # Send message through communicator using determined route
            self.communicator.send_message(route, message)
            
            # Update learner with outcome for future optimizations
            self.learner.update_model(route, message, status="success")
        except RouteNotFoundException as e:
            logging.warning(f"No active route found: {str(e)}")
            self.router.handle_failure(e)
        except CommunicationError as e:
            logging.error(f"Communication failed: {str(e)}")
            self.failure_handler.attempt_recovery()
        finally:
            # Ensure monitoring captures all outcomes
            self.monitor.log_activity("message_processed", message)

    def handle_failure(self, error: Exception) -> None:
        """Handles failures gracefully by triggering recovery mechanisms."""
        try:
            # Implement circuit breaking if necessary
            if self.router.is_route_unreliable():
                self.router.deactivate_route()
                
            # Attempt to recover failed connections
            self.failure_handler.attempt_recovery(error)
            
            # Log the failure for analysis
            logging.error(f"Failure handled: {str(error)}")
        except Exception as e:
            logging.critical(f"Failed to handle failure: {str(e)}")

    def update_knowledge_base(self, new_data: Dict[str, Any]) -> None:
        """Updates the knowledge base with new insights."""
        try:
            self.learner.train_model(new_data)
            self.knowledge_base.update_insights(new_data)
            logging.info("Knowledge base updated successfully.")
        except Exception as e:
            logging.error(f"Failed to update knowledge base: {str(e)}")

    def provide_dashboard_update(self) -> Dict[str, Any]:
        """Provides real-time metrics for the dashboard."""
        try:
            metrics = self.monitor.get_current_metrics()
            integration_status = self.router.get_integration_health()
            return {
                "metrics": metrics,
                "status": integration_status
            }
        except Exception as e:
            logging.error(f"Failed to fetch dashboard data: {str(e)}")
            return {"error": str(e)}