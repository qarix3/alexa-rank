
import csv
import os
import queue
import urllib.request
import zipfile


def main():
    """
    Paths for the data file this module needs.
    """
    
    REMOTE_FILE = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
    LOCAL_ZIP_FILE = 'top-1m.csv.zip'
    LOCAL_FILE = 'top-1m.csv'
    OUTFILE = 'top-1m-url.csv'

    download_alexa(REMOTE_FILE, LOCAL_ZIP_FILE, LOCAL_FILE)
    strip_rank(LOCAL_FILE, OUTFILE)
    rankings_dict(LOCAL_FILE)


def download_alexa(REMOTE_FILE, LOCAL_ZIP_FILE, LOCAL_FILE):
    """
    Function to download the first million ranks.
    Downloads a zipped csv file.
    """

    # Verify that the top million list exists. If not, download it.
    if not os.path.exists(LOCAL_FILE):
        print("\nDownloading latest Alexa rankings. Please wait..")
        urllib.request.urlretrieve(REMOTE_FILE, LOCAL_ZIP_FILE)
        with zipfile.ZipFile(LOCAL_ZIP_FILE) as f:
            for file in f.namelist():
                f.extract(file, os.path.dirname(LOCAL_FILE))
    else:
        print("\nFile already exist")


def rankings_dict(LOCAL_FILE):
    """
    Imports the csv file into an empty dictionary.
    Key: Ranks
    Value: Domain Names
    """

    ranking = {}
    csv_reader = csv.reader(open(LOCAL_FILE, 'r'))
    for row in csv_reader:
        key, value = row
        ranking[key] = value

    print(ranking)


def strip_rank(LOCAL_FILE, OUTFILE):
    """
    Function remove rank in csv file.
    """

    urls = []
    with open(LOCAL_FILE, newline='\n') as fs_in:
        readfile = csv.reader(fs_in, delimiter=',')
        for row in readfile:
            urls.append(row[1].strip())

    with open(OUTFILE, mode='w', newline='') as fs_out:
        writer = csv.writer(fs_out)
        writer.writerow([url for url in urls])


if __name__ == '__main__':
    main()
