import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
import time
async def scraper(urls):

    run_conf = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        stream=True  ,# Enable streaming mode
        page_timeout=10*1000,
    )

    async with AsyncWebCrawler() as crawler:
        # Stream results as they complete
        async for result in await crawler.arun_many(urls, config=run_conf):
            if result.success:
                print(f"[OK] {result.url}, length: {len(result.markdown.raw_markdown)}")
            else:
                print(f"[ERROR] {result.url} => {result.error_message}")

        # Or get all results at once (default behavior)
        run_conf = run_conf.clone(stream=False)
        results = await crawler.arun_many(urls, config=run_conf)
        output = []
        for res in results:
            if res.success:
                print(f"[OK] {res.url}, length: {len(res.markdown.raw_markdown)}")
                out = res.markdown.raw_markdown
                print(type(out))
                output.append(out)
            else:
                print(f"[ERROR] {res.url} => {res.error_message}")
        return output

if __name__ == "__main__":
    s = time.time()
    urls = ['https://www.yahoo.com/news/articles/us-india-relations-hit-low-051715778.html?fr=sycsrp_catchall', 'https://www.yahoo.com/news/articles/trump-wants-india-stop-buying-034221824.html?fr=sycsrp_catchall', 'https://www.yahoo.com/news/articles/why-india-buying-oil-russia-153026111.html?fr=sycsrp_catchall', 'https://www.yahoo.com/news/articles/india-accuses-us-eu-russia-120533744.html?fr=sycsrp_catchall', 'https://www.aljazeera.com/news/2025/8/6/russia-ukraine-war-list-of-key-events-day-1259', 'https://thehill.com/homenews/5437533-india-china-us-trade-tensions/', 'https://www.yahoo.com/news/articles/u-india-relations-strain-over-084446644.html?fr=sycsrp_catchall', 'https://gulfbusiness.com/india-unites-against-us-tariff-threat-over-russian-oil-trade/', 'https://www.yahoo.com/news/articles/flash-flood-washes-himalayan-town-112014445.html?fr=sycsrp_catchall', 'https://www.yahoo.com/news/articles/least-4-dead-100-still-175650064.html?fr=sycsrp_catchall', 'https://www.cnbctv18.com/india/india-pakistan-war-live-updates-india-attacks-pakistan-islamabad-lahore-karachi-peshawar-sialkot-punjab-amritsar-blackout-missile-attack-liveblog-19601834.htm', 'https://www.bbc.com/news/live/cwyneele13qt', 'https://www.ndtv.com/india-news/india-pakistan-war-news-india-activates-14-infantry-battalions-territorial-army-operation-sindoor-india-shoots-down-pak-missiles-drones-8371114', 'https://www.cnn.com/world/live-news/india-pakistan-attack-kashmir-tourists-intl-hnk', 'https://www.aljazeera.com/news/2025/5/14/what-did-india-and-pakistan-gain-and-lose-in-their-military-standoff', 'https://apnews.com/live/india-pakistan-attack-pahalgam-kashmir', 'https://www.msn.com/en-in/news/world/trade-war-trump-was-asked-about-india-s-claim-on-us-importing-russian-uranium-fertilisers-here-s-his-response/ar-AA1JZ0v4', 'https://www.aol.com/news/india-accuses-eu-us-double-111410092.html', 'https://www.msn.com/en-us/news/world/us-india-relations-hit-new-low-despite-trump-modi-bromance-what-s-next/ar-AA1JZwJS', 'https://www.msn.com/en-us/news/world/trump-wants-india-to-stop-buying-russian-oil-why-is-modi-saying-no/ar-AA1JZ7Eg', 'https://www.msn.com/en-us/money/markets/trump-threatens-higher-india-tariffs-accuses-it-of-funding-war-in-ukraine/ar-AA1JT00v', 'https://www.msn.com/en-us/news/world/us-india-relations-hit-new-low-despite-trump-modi-bromance-what-s-next/ar-AA1JZwJS', 'https://indianexpress.com/article/india/operation-sindoor-live-updates-india-pakistan-border-airstrike-bahawalpur-9989832/']
    print(asyncio.run(scraper(urls)))
    print(f"Time taken: {time.time() - s}")
