import json

with open("README.md", "r") as f:
    readme = f.read()

with open("images.json", "r") as f:
    images_data = json.load(f)

with open("README.md", "w") as f:
    copying = True

    for line in readme.splitlines():
        if line == "<!-- generate start -->":
            f.write(line + "\n")

            # generate markdown table of images
            f.write("| Name | Description |\n| --- | --- |\n")
            for image in images_data:
                f.write(
                    f"| `ghcr.io/jake-walker/{image['name']}` | {image['description']} |\n"
                )

            copying = False
        elif line == "<!-- generate end -->":
            f.write(line + "\n")
            copying = True
        elif copying:
            f.write(line + "\n")
