import pornhub
import sys

def main():
    print("--- PornHub API Demo ---")
    client = pornhub.PornHub([])

    print("\n[1] Fetching Stars...")
    try:
        stars_gen = client.getStars(quantity=5, page=1)
        count = 0
        for star in stars_gen:
            count += 1
            print(f"  {count}. Name: {star.get('name')}, Type: {star.get('type')}, URL: {star.get('url')}")
            # print(f"     Details: {star}")
    except Exception as e:
        print(f"Error fetching stars: {e}")

    print("\n[2] Fetching Videos...")
    try:
        videos_gen = client.getVideos(quantity=5, page=1)
        count = 0
        for video in videos_gen:
            count += 1
            print(f"  {count}. Title: {video.get('title')}")
            print(f"     Duration: {video.get('duration')}, Views: {video.get('views')}")
            print(f"     URL: {video.get('url')}")
    except Exception as e:
        print(f"Error fetching videos: {e}")

if __name__ == "__main__":
    main()
