import sys



def main():
    fileName = sys.argv[1]
    lineList = []

    for line in open(fileName):
        lineList.append(line.strip())



if __name__ == "__main__":
    main()