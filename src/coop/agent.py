from dotenv import load_dotenv

from langchain.agents import create_agent

load_dotenv()

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="deepseek-chat",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
response = agent.stream(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
    stream_mode="updates",
)
for chunk in response:
    for step, data in chunk.items():
        print("-" * 80)
        print(f"step: {step}")
        print(f"content: {data['messages'][-1].content_blocks}")