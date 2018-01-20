import os


def main():

    posts = []

    for file in os.listdir("."):

        if not file.endswith(".md"):
            continue

        with open(file, "r") as post:
            data = post.read()
            title = data.split("\n")

            if len(title) < 1:
                print("Post title could not be fetched")
                exit(1)

            post_title = title[0].replace("#", "").strip()
            desc = None
            date = None
            author = None
            image = None

            metadata = data.split("---")
            if len(metadata) != 2:
                print("Post format is invalid!")
                exit(1)

            for line in metadata[1].split("\n"):
                if "Posted-on:" in line:
                    date = line.replace("Posted-on:", "").strip()
                if "Short-description:" in line:
                    desc = line.replace("Short-description:", "").strip()
                if "Image:" in line:
                    image = line.replace("Image:", "").strip()

            if desc is None or date is None:
                print("Invalid post metadata")
                exit(1)

            if image is None:
                image = "null"

            p = {
                "title": post_title,
                "desc": desc,
                "date": date,
                "image": image,
                "file": file.replace(".md", "")
            }

            posts.append(p)

    print("[", end='')
    for i in range(0, len(posts)):
        print(str(posts[i]).replace("\'", "\""), end='')
        if i != len(posts) - 1:
            print(",", end='')
    print("]")

if __name__ == "__main__":
    main()