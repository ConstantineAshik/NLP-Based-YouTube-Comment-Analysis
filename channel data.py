import pandas as pd
from googleapiclient.discovery import build

# CONFIGURATION
API_KEY = "AIzaSyDPKISVGGZsbgqByvUhxuXUE1QYiJyFeWM"
# List of channel IDs to scrape (e.g., Tech channels, News, etc.)
CHANNEL_IDS = [
    "UCXuqSBlHAE6Xw-yeJA0Tunw", # Example: Google Developers
    "UCBJycsmduvYEL83R_U4JriQ"
    "UCJsUvAqDzczYv2UpFmu4PcA"# Example: MKBHD
]

def get_video_ids(youtube, channel_id, limit=50):
    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        maxResults=limit,
        order="date",
        type="video"
    )
    response = request.execute()
    return [item['id']['videoId'] for item in response['items']]

def get_comments(youtube, video_ids):
    comments_data = []
    
    for video_id in video_ids:
        try:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100, # Max allowed per page
                textFormat="plainText"
            )
            response = request.execute()

            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']
                comments_data.append({
                    "channel_id": item['snippet']['channelId'],
                    "video_id": item['snippet']['videoId'],
                    "author_id": comment['authorChannelId']['value'], # Crucial for network
                    "text": comment['textDisplay'],
                    "like_count": comment['likeCount']
                })
        except:
            print(f"Comments disabled or error for video {video_id}")
            continue
            
    return comments_data

def main():
    if API_KEY == "AIzaSyDPKISVGGZsbgqByvUhxuXUE1QYiJyFeWM":
        print("ERROR: You need to put your API Key in the script.")
        return

    youtube = build("youtube", "v3", developerKey=API_KEY)
    
    all_comments = []
    print("Fetching video IDs...")
    for channel in CHANNEL_IDS:
        vids = get_video_ids(youtube, channel)
        print(f"Found {len(vids)} videos for channel {channel}. Fetching comments...")
        data = get_comments(youtube, vids)
        all_comments.extend(data)
        
    df = pd.DataFrame(all_comments)
    output_path = "data/raw_comments.csv"
    df.to_csv(output_path, index=False)
    print(f"SUCCESS: Saved {len(df)} comments to {output_path}")

if __name__ == "__main__":
    main()