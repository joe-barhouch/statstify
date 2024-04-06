"""Custom Tools for the Crew"""

from crewai_tools import BaseTool



class OnlineSearchTool(BaseTool):
    name: str = "Online Search Tool"
    description: str = "Search the web for information about certain stats"


    def _run(self, argument: str) -> str:
        pass