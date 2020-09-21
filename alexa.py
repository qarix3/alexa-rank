import os
import csv
import urllib.request
import zipfile
import queue 


# Paths for the data file this module needs.
REMOTE_FILE = 'http://s3.amazonaws.com/alexa-static/top-1m.csv.zip'
LOCAL_ZIP_FILE = 'top-1m.csv.zip'
LOCAL_FILE = 'top-1m.csv'

def download_alexa(REMOTE_FILE, LOCAL_ZIP_FILE, LOCAL_FILE):
   
    """
    Function to download the first million ranks.
    Downloads a zipped csv file.
    """
    
    # Verify that the top million list exists. If not, download it.
    if not os.path.exists(LOCAL_FILE):
          print ("\nDownloading latest Alexa rankings. Please wait..\n")
          urllib.request.urlretrieve(REMOTE_FILE, LOCAL_ZIP_FILE)
          with zipfile.ZipFile(LOCAL_ZIP_FILE) as f:
            for file in f.namelist():
                  f.extract(file, os.path.dirname(LOCAL_FILE))
    else:
          print("\nFile already exist\n")
    
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
          rankings[key] = value
      
      return ranking
    
def strip_rank(FILE, OUTFILE):
            #  tasks = queue.Queue() # create an empty task list 
      #  with open(FILE, newline='\n') as csvfile:
      #    readfile = csv.reader(csvfile, delimiter=',')
      #    for row in readfile:
      #         #  row.split(",")[1].strip()
      #          print(row)
      #       #  tasks.put()
      #   #      print(i)
       """
       Function remove rank in csv file.
       """
      #  with open(FILE) as f_in, open(OUTFILE, 'w', newline='') as f_out:
             # Write header unchanged
            #  header = f_in.readline()
            #  f_out.write(header)
            # Transform the rest of the lines
            # for line in f_in:
            #       f_out.write(line.split(",")[1].strip())
      #  with open(FILE, 'a', newline='\n') as csvfile:
      #       #  writer = csv.writer(csvfile, delimiter=",")
      #        csvfile.write('Babo')
            #  for row in list_results:
                  #  columns = [c.strip() for c in row.strip(', ').split(',')]
                  #  writer.writerow(columns)

def read_csv(filename):
      with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            header = next(readCSV)
            for row in readCSV:
                  print(row)
                  print(row[0])
                  print(row[0],row[1])
                  
if __name__ == '__main__':
      print(read_csv('test.csv'))
      # strip_rank('test.csv','outfile.csv')
      # rankings_dict('test.csv')
      
  # download_alexa(REMOTE_FILE, LOCAL_ZIP_FILE, LOCAL_FILE)