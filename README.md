# TicketClassificationAndResponseAutomation Crew

This project automates the process of responding to customer support tickets using a combination of NLP and AI.

The project is implemented in Python and uses the CrewAI framework. The CrewAI framework is an open-source framework for building AI automation projects. It is designed to be flexible and extensible, allowing for the integration of third-party tools and services.

The project consists of two main components: a ticket classification AI and a response automation AI. The ticket classification AI is responsible for classifying a ticket based on its subject and content. The response automation AI is responsible for generating a draft response to the ticket based on the classification and the content of the ticket.

The project is setup to use the CrewAI framework to integrate the two components. The CrewAI framework provides a simple and intuitive API for creating and managing AI agents. The API is designed to be easy to use and allows for the creation of complex automation projects.

The project is designed to be highly customizable and can be easily extended to integrate with other tools and services. The project is also designed to be highly scalable and can handle large volumes of tickets.

The project is built using the following technologies:

* Python
* CrewAI
* NLP
* AI

## Agents and Tasks

### Support Team Composition

1. **Ticket Classification Specialist**
   - **Role**: Analyzes and categorizes incoming support tickets
   - **Task**: `classify_ticket_category`
     - Classifies tickets into predefined categories:
       - Access and Account Management
       - Technical Support
       - Information and Documentation
       - Training and Onboarding
       - Billing and Subscription
       - Feature Requests and Feedback
     - Uses ticket subject and content for accurate classification

2. **Priority Assignment Specialist**
   - **Role**: Evaluates ticket urgency and sentiment
   - **Task**: `assign_ticket_priority`
     - Assigns priority levels (High/Medium/Low) based on:
       - Customer urgency
       - Sentiment analysis
       - Ticket category
     - Special rules:
       - Information/Documentation tickets: Low priority
       - Feature Requests/Feedback: Low priority (unless urgent)
       - Billing/Subscription: Always High priority

3. **Response Generation Specialist**
   - **Role**: Creates draft responses using available knowledge bases
   - **Task**: `generate_draft_response`
     - Searches multiple sources for relevant information:
       - crewai.com
       - docs.crewai.com
       - help.crewai.com
     - Utilizes CSV and JSON RAG Search Tools
     - Crafts contextual responses for the CrewAI Enterprise Platform

4. **CrewAI Support Manager**
   - **Role**: Orchestrates the support workflow
   - **Task**: `prepare_response`
     - Coordinates all previous tasks
     - Prepares final response including:
       - Ticket identification
       - Classification
       - Priority level
       - Suggested response
     - Ensures consistent response format and quality

### Workflow

The support process follows a sequential workflow:
1. Ticket classification
2. Priority assignment
3. Response generation
4. Final response preparation

Each agent's output serves as context for subsequent tasks, ensuring a cohesive and efficient support process.
