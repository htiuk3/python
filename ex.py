import argparse
 
ap = argparse.ArgumentParser()
 
ap.add_argument("name")
 
ap.add_argument("-age")
 
args = vars(ap.parse_args())
 
print (args["name"])
 
print (args["age"])