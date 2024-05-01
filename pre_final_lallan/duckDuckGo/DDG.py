from langchain_community.tools import DuckDuckGoSearchRun
import asyncio
from asyncio import WindowsSelectorEventLoopPolicy

asyncio.set_event_loop_policy(WindowsSelectorEventLoopPolicy())
def search_query(query):
    """
    Search the given query using DuckDuckGo via the langchain community tools.

    :param query: String containing the search query.
    :return: Results from the DuckDuckGo search.
    """
    search = DuckDuckGoSearchRun()
    result = search.run(query)
    return result


"""
Example:
print(search_query("Where I can find best chat in Lucknow?"))
Result: 
•Shukla Chat House in Hazratganj, one of the best Chat waala in Lucknow 
•Kalevum Sweets D-Block •Royal Cafe, Hazratganj, if you wanna try their famous and authentic Basket Chat 
•Balaji Chat in front of Spencer's Sec-8 
• Near Arvindo Park , i don't remember the name, in front of Yoga school/Wassle 
Laundry Lucknow is the capital city of the Indian state of Uttar Pradesh. Lucknow, 
popularly known as The City of Nawabs, has always been a multicultural city that 
flourished as a cultural and artistic capital of North India in the 18th and 19th centuries. 
It is also known as the Golden City of the East, Shiraz-i-Hind and The Constantinople of India. 
Lucknow is the capital city of the Indian state of Uttar Pradesh. 
Lucknow, popularly known as The City of Nawabs, has always been a multicultural city that 
flourished as a cultural and artistic capital of North India in the 18th and 19th centuries. ... 
Lucknow Social Thread [20231109]: Chit-Chat, Advice, Rants, Q&A, Meetups, Classifieds, etc ... 
King Of Chat in Lucknow, browse the original menu, discover prices, read customer reviews. 
The restaurant King Of Chat has received 1419 user ratings with a score of 76. ... 
Find the best restaurant in Lucknow. Unclamed activity. Compare the best restaurants near King Of Chat. 
TA. King of Chat: 76: 3.7: 4: L-14 All Day Dining: 90: 4.4: 5: Sepia ... 
It is a take on golgappa, filled with boiled and mashed white peas and spicy mint flavoured water. 
Dahi-chutney ke batashe is a Lucknow speciality where golgappas are stuffed with matar and topped ...
"""