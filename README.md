# Aigeon AI Google Play API

## Overview

The `aigeon-ai.google-play-api` is a Python-based server application designed to interface with the Google Play Store using the SerpApi service. This application allows users to perform detailed searches on the Google Play Store, retrieving information about apps based on various parameters such as search queries, categories, device types, and more.

## Features

- **Search Functionality**: Perform comprehensive searches on the Google Play Store using a variety of parameters.
- **Flexible Query Options**: Supports queries by search term, app category, device type, and more.
- **Pagination Support**: Easily navigate through paginated results using tokens.
- **Output Formats**: Choose between JSON and HTML output formats for search results.
- **Asynchronous Execution**: Optionally execute searches asynchronously for improved performance.
- **Cache Control**: Control caching behavior to ensure fresh data retrieval.

## Main Features and Functionality

The core functionality of this application revolves around the `search_google_play` function, which is a tool provided by the FastMCP framework. This function interfaces with the SerpApi to perform searches on the Google Play Store. It constructs a request payload based on the provided parameters and sends a GET request to the SerpApi endpoint.

### Key Features:

- **Search Query (`q`)**: Allows users to search for apps using specific keywords.
- **Geolocation (`gl`)**: Specify the country code to tailor search results to a particular region.
- **Language (`hl`)**: Define the language code to receive results in a specific language.
- **App Category (`apps_category`)**: Filter results by app category.
- **Device Type (`store_device`)**: Specify the type of device (e.g., phone, tablet) to filter results accordingly.
- **Age Range (`age`)**: Filter results by age range, applicable when searching within the FAMILY category.
- **Pagination Tokens**: Utilize `next_page_token` and `section_page_token` for navigating through paginated results.
- **Chart Type (`chart`)**: Specify chart types like 'topselling_free' to filter results.
- **Caching and Async Options**: Control caching with `no_cache` and enable asynchronous execution with `aasync`.
- **ZeroTrace Mode**: An enterprise feature that enhances privacy during searches.
- **Output Format (`output`)**: Choose between 'json' or 'html' for the format of the search results.

## Main Function Description

### `search_google_play`

This function performs a search on the Google Play Store using the SerpApi service. It accepts a variety of parameters to customize the search and returns the results in the specified format.

#### Parameters:

- **`q`**: *(Optional)* A string representing the search query. Cannot be used with `apps_category` or `store_device`.
- **`gl`**: *(Optional)* A two-letter country code (e.g., 'us', 'uk'). Defaults to 'us'.
- **`hl`**: *(Optional)* A two-letter language code (e.g., 'en', 'es'). Defaults to 'en'.
- **`apps_category`**: *(Optional)* A string specifying the app store category. Cannot be used with `q` or `store_device`.
- **`store_device`**: *(Optional)* A string specifying the device type (e.g., 'phone', 'tablet'). Cannot be used with `q` or `apps_category`.
- **`age`**: *(Optional)* A string specifying the age range, applicable only with `apps_category=FAMILY`.
- **`next_page_token`**: *(Optional)* A string token for pagination to retrieve the next page of results.
- **`section_page_token`**: *(Optional)* A string token for pagination to retrieve a specific section of results.
- **`chart`**: *(Optional)* A string specifying the chart type (e.g., 'topselling_free').
- **`see_more_token`**: *(Optional)* A string token for pagination to see more results.
- **`no_cache`**: *(Optional)* A boolean to disallow cached results.
- **`aasync`**: *(Optional)* A boolean to enable asynchronous mode.
- **`zero_trace`**: *(Optional)* A boolean for enterprise use to enable ZeroTrace mode.
- **`output`**: *(Optional)* A string specifying the output format: 'json' or 'html'.

This function constructs a request payload, filters out any parameters with `None` values, and sends a GET request to the SerpApi endpoint. The response is returned in the specified output format.