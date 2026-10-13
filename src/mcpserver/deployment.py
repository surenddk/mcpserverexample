from mcp.server.mcpserver import MCPServer
mcp = MCPServer("Demo")

#Add a additional tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

#add a tool to get weather in given city
def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    # For demonstration purposes, we'll return a dummy weather string.
    # In a real implementation, you would call a weather API here.
    return f"The weather in {city} is sunny with a temperature of 25°C."
