from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher

class ActionRecommandBook(Action):
    def name(self) -> Text:
        return "action_recommand_book"

    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
       
        dispatcher.utter_message("i recommendation book to you")
        return []
