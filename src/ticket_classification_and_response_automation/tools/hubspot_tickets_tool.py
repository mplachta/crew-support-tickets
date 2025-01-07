from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from hubspot3 import Hubspot3
import os

class HubspotTicketsToolInput(BaseModel):
    """Input schema for HubspotTicketsTool."""
    search_query: str = Field(..., description="The search query for Hubspot tickets. Ideally using 1-2 words.")

    model_config = {
        "json_schema_extra": {
            "examples": [{"search_query": "billing issues"}]
        }
    }

class HubspotTicketsTool(BaseTool):
    name: str = "Hubspot Tickets Search Tool"
    description: str = (
        "Finds Hubspot tickets and all email replies based on a search query. "
        "Returns closed tickets that match the search query along with their email threads."
        "The search query should be a very basic string, ideally using 1-2 words."
    )
    args_schema: Type[BaseModel] = HubspotTicketsToolInput

    def _run(self, search_query: str) -> str:
        api_client = Hubspot3(api_key=os.getenv("HUBSPOT_ACCESS_TOKEN"))

        result = ""

        try:
            tickets = api_client.crm.tickets.search_api.do_search(
                {
                    "query": search_query,
                    "properties": ["subject", "content", "hs_ticket_id", "hs_pipeline_stage"],
                    "limit": 20,
                    "filterGroups": [{
                        "filters": [{
                            "propertyName": "hs_pipeline_stage",
                            "operator": "EQ",
                            "value": "4"  # 4 is the ID for "Closed" stage in HubSpot's default pipeline
                        }]
                    }]
                }
            )
            
            for ticket in tickets.results:
                ticket_content = f"Subject: {ticket.properties['subject']}\nContent:\n {ticket.properties['content']}\n\nReplies:\n"

                email_replies = api_client.crm.objects.emails.search_api.do_search(
                    {
                        "properties": ["hs_object_id", "hs_email_text"],
                        "limit": 100,
                        "filterGroups": [{
                            "filters": [{
                                "propertyName": "associations.ticket",
                                "operator": "EQ",
                                "value": ticket.properties['hs_ticket_id']
                            }]
                        }]
                    }
                )

                for reply in email_replies.results:
                    ticket_content += f"Reply:\n {reply.properties['hs_email_text']}\n\n"
                
                result += ticket_content + "\n---\n\n"

            return result if result else "No matching tickets found."
            
        except Exception as e:
            return f"Error searching Hubspot tickets: {str(e)}"
