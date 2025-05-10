#!/bin/bash

# File containing a list of URLs, one per line
URL_FILE="private/aliases_web_query.txt"
RATE_LIMIT="8"

echo "We have a free API key. Our rate limit is '$RATE_LIMIT'."
echo "This is going to take a while..."
echo ""

# Check if the URL file exists
if [ ! -f "$URL_FILE" ]; then
    echo "URL file '$URL_FILE' not found."
    exit 1
fi

# Loop through each URL in the file
while IFS= read -r url || [[ -n "$url" ]]; do
    echo "Opening URL: $url"

    # Open the URL (adjust the command based on your system and preferred browser)
    # For example, on macOS with open:
    open "$url" &

    # Wait for RATE_LIMIT seconds
    sleep "$RATE_LIMIT"
done < "$URL_FILE"

echo "Script completed."
