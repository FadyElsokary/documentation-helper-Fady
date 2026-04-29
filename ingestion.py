async def main() :
    """Main async function to orchestrate the entire process."""
    log_header ("DOCUMENTATION INGESTION PIPELINE")
    
    log_info(
    "TavilyCrawl: Starting to Crawl documentation from https://python.langchain.com/", Colors.PURPLE,
    )
    
    # Crawl the documentation site
    
    res = tavily_crawl.invoke({
        "url": "https://python.langchain.com/",
        "max_depth": 1,
        "extract_depth": "advanced",})
    
    all_docs = [Document (page_content=result[' raw_content'], metadata={"source": result['url']}) for result in res['results']]
    log_success(
    f"TavilyCrawl: Successfully crawled {len(all_docs)} URLs from documentation site"
    )
    
    
if __name__ == "__main__": 
    asyncio.run(main())

