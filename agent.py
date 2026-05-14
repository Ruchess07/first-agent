from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='finding_cheap_destinations',
    description='Looks for cheap destinations for a user',
    instruction='You are a helpful assistant that looks for cheap destinations for a user.',
)
