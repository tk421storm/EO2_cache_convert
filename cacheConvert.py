import os, shutil, sys
from traceback import format_exc

currentRoot=os.getcwd()

outputDirectory=os.path.join(currentRoot, "output")

if not os.path.exists(outputDirectory):
        os.makedirs(outputDirectory)
else:
        print("warning - output directory already exists. will overwrite any pre-existing files - is that ok?")
        yes=input("Y to continue:")
        if yes.lower()!="y":
                print("user abort")
                sys.exit()

for filepath in os.listdir(currentRoot):
        if os.path.splitext(filepath)[1]==".0":
                print("operating on cache file "+filepath)

                with open(os.path.join(currentRoot, filepath), "r") as myFile:
                        cacheInfo=myFile.readlines()

                        try:
                                artworkURL=cacheInfo[0].strip()

                                originalUID=artworkURL.split("artworks")[1].split("/")[6]
                                artworkExtension=artworkURL.split("?")[0].split(".")[-1]

                                print("i think this was for artwork "+str(originalUID))

                                cachePath=os.path.join(currentRoot, os.path.splitext(filepath)[0]+".1")
                                artworkPath=os.path.join(outputDirectory, originalUID+"."+artworkExtension)

                                shutil.copy(cachePath, artworkPath)

                                print("stored at "+artworkPath)
                                print("--------------")

                        except:
                                print("error operating on cache file "+str(filepath))

                                print(format_exc())

                                sys.exit()
