import pandas as pd
import tiktoken
import streamlit as st
from graphrag.query.indexer_adapters import read_indexer_entities, read_indexer_reports
from graphrag.query.llm.oai.chat_openai import ChatOpenAI
from graphrag.query.llm.oai.typing import OpenaiApiType
from graphrag.query.structured_search.global_search.community_context import (
    GlobalCommunityContext,
)
from graphrag.query.structured_search.global_search.search import GlobalSearch


class RGlobalSearch:

    def __init__(
        self,
        input_dir="msftgrag/output/20240915-221852/artifacts",
        community_level=2,
        api_key=st.secrets["OPENAI_API_KEY"],
        llm_model="gpt-4o-mini",
    ):
        # Initialize LLM and token encoder
        self.llm = ChatOpenAI(
            api_key=api_key,
            model=llm_model,
            api_type=OpenaiApiType.OpenAI,
            max_retries=20,
        )
        self.token_encoder = tiktoken.get_encoding("cl100k_base")

        # Load data from parquet files
        self.entity_df = pd.read_parquet(f"{input_dir}/create_final_nodes.parquet")
        self.report_df = pd.read_parquet(
            f"{input_dir}/create_final_community_reports.parquet"
        )
        self.entity_embedding_df = pd.read_parquet(
            f"{input_dir}/create_final_entities.parquet"
        )

        # Read reports and entities with the specified community level
        self.reports = read_indexer_reports(
            self.report_df, self.entity_df, community_level
        )
        self.entities = read_indexer_entities(
            self.entity_df, self.entity_embedding_df, community_level
        )

        # Set up context builder
        self.context_builder = GlobalCommunityContext(
            community_reports=self.reports,
            entities=self.entities,
            token_encoder=self.token_encoder,
        )

        # Define context builder parameters
        self.context_builder_params = {
            "use_community_summary": False,
            "shuffle_data": True,
            "include_community_rank": True,
            "min_community_rank": 0,
            "community_rank_name": "rank",
            "include_community_weight": True,
            "community_weight_name": "occurrence weight",
            "normalize_community_weight": True,
            "max_tokens": 5000,
            "context_name": "Reports",
        }

        # Define LLM parameters for map and reduce steps
        self.map_llm_params = {
            "max_tokens": 1000,
            "temperature": 0.0,
            "response_format": {"type": "json_object"},
        }
        self.reduce_llm_params = {
            "max_tokens": 2000,
            "temperature": 0.0,
        }

        # Initialize the search engine
        self.search_engine = GlobalSearch(
            llm=self.llm,
            context_builder=self.context_builder,
            token_encoder=self.token_encoder,
            max_data_tokens=12_000,
            map_llm_params=self.map_llm_params,
            reduce_llm_params=self.reduce_llm_params,
            allow_general_knowledge=False,
            json_mode=True,
            context_builder_params=self.context_builder_params,
            concurrent_coroutines=32,
            response_type="Multiple paragraphs",
        )

    async def get_response(self, query):
        # Perform the search using the query
        result = await self.search_engine.asearch(query)
        return result.response
