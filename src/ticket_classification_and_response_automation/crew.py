import glob
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crewai.knowledge.source.csv_knowledge_source import CSVKnowledgeSource
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from ticket_classification_and_response_automation.tools.hubspot_tickets_tool import HubspotTicketsTool

# Prepare the knowledge base for the Enterprise Platform Knowledge Base
knowledge_enterprise_kb = CSVKnowledgeSource(
    file_paths=["enterprise_kb.csv"],
    metadata={
        "category": "Enterprise Platform",
    },
)

# Prepare the knowledge base for the OSS Framework
files = glob.glob("knowledge/oss-docs/**/*.mdx", recursive=True)
files = [file.replace("knowledge/", "", 1) for file in files]

oss_framework_kb = TextFileKnowledgeSource(
    file_paths=files,
    metadata={
        "category": "CrewAI Open Source Framework",
    },
)

llm = LLM(
    model="gpt-4o",
    temperature=0.7
)

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
            llm=llm,
            knowledge_sources=[knowledge_enterprise_kb, oss_framework_kb],
            tools=[
                HubspotTicketsTool(),
                SerperDevTool(),
                ScrapeWebsiteTool(),
            ]
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
            tools=[],
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
