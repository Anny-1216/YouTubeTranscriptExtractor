import re
import requests
from youtube_transcript_api import YouTubeTranscriptApi
from bs4 import BeautifulSoup

# Function to get video links from a playlist
def get_video_links_from_playlist(playlist_url):
    try:
        # Send a GET request to the playlist URL
        response = requests.get(playlist_url)

        # Check if the request was successful
        if response.status_code != 200:
            print("Error fetching playlist page")
            return []

        # Parse the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Regular expression pattern to extract video URLs from the page
        video_url_pattern = re.compile(r'"videoId":"([a-zA-Z0-9_-]{11})"')

        # Find all video IDs using the regex pattern
        video_ids = re.findall(video_url_pattern, soup.prettify())

        # Create the video URLs
        video_links = [f"https://www.youtube.com/watch?v={video_id}" for video_id in video_ids]

        return video_links

    except Exception as e:
        print(f"Error: {e}")
        return []

# Function to get video ID and title from URL
def get_video_id_and_title(url):
    try:
        # Clean URL and extract video ID
        video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
        if not video_id_match:
            raise ValueError("Invalid YouTube URL")
        video_id = video_id_match.group(1)

        # Fetch title using requests
        response = requests.get(f"https://www.youtube.com/watch?v={video_id}")
        title_match = re.search(r'<title>(.*?)</title>', response.text)
        title = title_match.group(1).replace(" - YouTube", "").strip() if title_match else "YouTube_Transcript"

        return video_id, title
    except Exception as e:
        print(f"Error fetching video ID or title: {e}")
        return None, None

# Function to get transcript for the video
def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

# Function to save transcript to a file
def save_transcript_to_file(transcript, title):
    filename = f"{title}.txt"
    # Sanitize filename
    filename = "".join(c if c.isalnum() or c in " _-" else "_" for c in filename)
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for line in transcript:
                f.write(f"{line['text']}\n")
        print(f"Transcript saved as '{filename}'")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Main function to run the process
def main():
    playlist_url = input("Enter YouTube playlist URL: ").strip()

    # Get the video links from the playlist
    video_links = get_video_links_from_playlist(playlist_url)

    if video_links:
        print("\nVideo links found in the playlist:")
        print(f"Total videos found: {len(video_links)}")

        # Get unique links
        video_links = list(set(video_links))
        print(f"Total unique videos: {len(video_links)}")

        # Process each video link
        for video_url in video_links:
            print(f"\nProcessing video: {video_url}")
            video_id, title = get_video_id_and_title(video_url)

            if video_id and title:
                transcript = get_transcript(video_id)
                if transcript:
                    save_transcript_to_file(transcript, title)
                else:
                    print(f"Transcript not available for video {title}")
            else:
                print(f"Could not retrieve video ID or title for {video_url}")

    else:
        print("No videos found in the playlist or failed to fetch the playlist.")

if __name__ == "__main__":
    main()
