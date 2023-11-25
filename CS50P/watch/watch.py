import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if yurl := re.search(r"(^<iframe(.)* src=\"(http(s)*:\/\/(www\.)*youtube\.com\/embed\/((\w)+))\".*</iframe>)",s):
        return "https://youtu.be/" + yurl.groups()[5]
        #return  yurl.groups()[5]


if __name__ == "__main__":
    main()