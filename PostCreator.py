from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

filename = input("Enter the filename: ")
filename = filename.replace(" ", "-").lower()
title = input("Enter the title: ")
categories = input("Enter the categories (default is blog): ")
categories = categories if categories else "blog"
tags = input("Enter a tag: ")

filename = today + "-" + filename + ".md"

f = open(filename, "w")
f.write("---")
f.write("\ntitle: " + title)
f.write("\ndate: " + today + "T12:00:00-00:00")
f.write("\ncategories:")
f.write("\n  - " + categories)
f.write("\ntags:")
f.write("\n  - " + tags)
f.write("\n---")
f.close()


# ---
# title: "test"
# date: 2024-02-03T12:00:00-00:00
# categories:
#   - blog
# tags:
#   - Jekyll
#   - update
# ---