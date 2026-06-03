import os
from api_wrapper import AnthropicClient
from dotenv import load_dotenv

load_dotenv()

client = AnthropicClient(api_key=os.getenv("ANTHROPIC_API_KEY"))

discovery_notes = """Spoke to Sarah Chen, VP of Revenue Operations at Northgate SaaS. She flagged that their current attribution model is basically broken — they're running campaigns across six channels but have no idea which ones are actually driving pipeline. Her CRO, Marcus Webb, is the one who needs to sign off on any new tooling — he's very data driven and won't move without seeing a clear ROI case. Sarah mentioned they need at least 30% reduction in wasted ad spend to justify the investment, and any contract over $75k goes to a quarterly board review. Their current process is to run a 60 day pilot before full procurement. Sarah herself has been pushing for this internally for months and has already got buy-in from her data team. Main pain is that their RevOps team is spending about 15 hours a week manually pulling reports from HubSpot, Google Ads and LinkedIn and it's still not giving them accurate attribution. They'd need the tool to integrate with HubSpot as a hard requirement — non negotiable. Decision timeline is end of Q3."""

system_prompt = """You are a tool that organises messy discovery notes into a clean, organised plan that adheres to the MEDDIC sales qualification framework. Before outputting JSON, analyse each piece of information against all six MEDDIC categories and identify every category it could belong to. When you get the notes, separate the contents according to the extent to which they align with each category. If content aligns with two or more categories, flag this with ⚠️ and specify which categories with AND. If there is no relevant content for a category, output ❓ and flag that this is the case. Output should follow this JSON structure exactly, no explanation. :
json{
  "Metrics": {"content": "...", "flag": ""},
  "Economic Buyer": {"content": "...", "flag": ""},
  "Decision Criteria": {"content": "...", "flag": ""},
  "Decision Process": {"content": "...", "flag": ""},
  "Identify Pain": {"content": "...", "flag": ""},
  "Champion": {"content": "...", "flag": ""}
}
Issue all output in JSON only, no explanation."""

response = client.send_message(message=discovery_notes, system=system_prompt)

print(response)
