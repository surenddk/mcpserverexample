from mcp.server.mcpserver import MCPServer
mcp = MCPServer("Demo")

#Add a additional tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

