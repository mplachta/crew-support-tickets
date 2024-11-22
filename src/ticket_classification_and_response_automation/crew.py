from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import CSVSearchTool, JSONSearchTool, ScrapeWebsiteTool

@CrewBase
class TicketClassificationAndResponseAutomationCrew():
    """TicketClassificationAndResponseAutomation crew"""

    @agent
    def ticket_classifier(self) -> Agent:
        return Agent(
            config=self.agents_config['ticket_classifier'],
            
        )

    @agent
    def priority_assigner(self) -> Agent:
        return Agent(
            config=self.agents_config['priority_assigner'],
            
        )

    @agent
    def response_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['response_generator'],
            
        )

    @agent
    def support_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['support_manager'],
            
        )

    @task
    def classify_ticket_category(self) -> Task:
        return Task(
            config=self.tasks_config['classify_ticket_category'],
            
        )

    @task
    def assign_ticket_priority(self) -> Task:
        return Task(
            config=self.tasks_config['assign_ticket_priority'],
            
        )

    @task
    def generate_draft_response(self) -> Task:
        return Task(
            config=self.tasks_config['generate_draft_response'],
            tools=[CSVSearchTool(csv='./crewai_kb.csv'), JSONSearchTool(json_path='./crewai_kb.json'), ScrapeWebsiteTool()],
        )

    @task
    def prepare_response(self) -> Task:
        return Task(
            config=self.tasks_config['prepare_response'],
            
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TicketClassificationAndResponseAutomation crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
