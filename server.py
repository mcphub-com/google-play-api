import os
import requests
from typing import Union, Literal, List, Annotated
from dotenv import load_dotenv
from pydantic import Field
from mcp.server import FastMCP  # 确保您已安装MCP框架

# 加载环境变量
load_dotenv()

# 初始化FastMCP实例
mcp = FastMCP('google-play-server')

# API配置
serp_url = "https://serpapi.com/search?engine=google_play"
serp_api_key = os.getenv("SERP_API_KEY")

@mcp.tool()
def search_google_play(
    q: Annotated[Union[str, None], Field(description="Search query. Cannot be used with apps_category or store_device.")] = None,
    apps_category: Annotated[Union[str, None], Field(description="App store category. Cannot be used with q or store_device.")] = None,
    store_device: Annotated[Union[Literal['phone', 'tablet', 'tv', 'chromebook', 'watch', 'car'], None], 
        Field(description="Device type. Cannot be used with q or apps_category.")] = None,
    age: Annotated[Union[Literal['AGE_RANGE1', 'AGE_RANGE2', 'AGE_RANGE3'], None], 
        Field(description="Age range. Only works with apps_category=FAMILY.")] = None,
    next_page_token: Annotated[Union[str, None], Field(description="Next page token for pagination.")] = None,
    section_page_token: Annotated[Union[str, None], Field(description="Section page token for pagination.")] = None,
    chart: Annotated[Union[str, None], Field(description="Chart type (e.g., 'topselling_free').")] = None,
    see_more_token: Annotated[Union[str, None], Field(description="'See more' token for pagination.")] = None,
    no_cache: Annotated[Union[bool, None], Field(description="Disallow cached results.")] = None,
    aasync: Annotated[Union[bool, None], Field(description="Use async mode.")] = None,
    zero_trace: Annotated[Union[bool, None], Field(description="Enterprise only: Enable ZeroTrace mode.")] = None,
    output: Annotated[Union[Literal['json', 'html'], None], Field(description="Output format: 'json' or 'html'.")] = None
):
    """Search Google Play Apps Store using SerpApi"""
    # 构建请求负载
    payload = {
        'engine': 'google_play',
        'api_key': serp_api_key,
        'q': q,
        'apps_category': apps_category,
        'store_device': store_device,
        'age': age,
        'next_page_token': next_page_token,
        'section_page_token': section_page_token,
        'chart': chart,
        'see_more_token': see_more_token,
        'no_cache': no_cache,
        'async': aasync,
        'zero_trace': zero_trace,
        'output': output
    }
    
    # 移除空值参数
    payload = {k: v for k, v in payload.items() if v is not None}
    
    # 发送请求
    response = requests.get(serp_url, params=payload)
    response.raise_for_status()
    
    return response.json()

if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")