from urllib.parse import urlparse
import argparse
import os

def getDomains(inp_file):
    #Read the domains file
    file_to_read = open(inp_file, 'r') 
    Lines = file_to_read.readlines() 
    sites = [] # holds the list of urls to be queried
    for line in Lines: 
        sites.append(line.strip("\n"))

    print("Urls to query " + str(len(sites)))

    outF = open("OutFile.txt", "a")

    for site in sites:
        parsed_uri = urlparse(site)
        result = '{uri.netloc}'.format(uri=parsed_uri)
        outF.writelines(result + "\n")

    outF.close()

def main():
    parser = argparse.ArgumentParser(description="Script to extract domain names from a list of urls")
    parser.add_argument("-rawurls", type=str, help="File Path containing raw urls")

    args = parser.parse_args()

    #print(args.rawurls)
    inp_file = str(args.rawurls)

    if(os.path.exists(inp_file) and inp_file.endswith("txt")):
        getDomains(inp_file)
        print("Finish!")
    else:
        print("The Input arguments or the input file is invalid")

if __name__ == "__main__":
    main()
