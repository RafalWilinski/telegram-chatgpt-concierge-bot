import { DynamicTool } from "langchain/tools";
import google from "googlethis";

export const googleTool = new DynamicTool({
  name: "Google Search Tool",
  description:
    "This is Google. Use this tool to search the internet. Input should be a string",
  func: async (searchPhrase: string) => {
    try {
      const response = await google.search(searchPhrase, {
        page: 0,
        safe: false, // Safe Search
        parse_ads: false, // If set to true sponsored results will be parsed
        additional_params: {
          // add additional parameters here, see https://moz.com/blog/the-ultimate-guide-to-the-google-search-parameters and https://www.seoquake.com/blog/google-search-param/
        },
      });

      console.log({ googleResponse: response });

      return JSON.stringify({
        results: response.results,
        featured: response.featured_snippet,
      });
    } catch (error) {
      console.log(error);
      return "Failed to get results from Google. Do not try using Google again.";
    }
  },
});
