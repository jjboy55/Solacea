import os
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore

# db connections
neo_4j_url = os.getenv("NEO4J_URI")
neo_4j_username = os.getenv("NEO4J_USERNAME")
neo_4j_password = os.getenv("NEO4J_PASSWORD")
# Load model directly
# Create graph instance
graph_store = Neo4jPropertyGraphStore(
    username=neo_4j_username,
    password=neo_4j_password,
    url=neo_4j_url,
)
