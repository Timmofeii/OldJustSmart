
class FileWorker():
    def file_writer(self,file, text):  # rewrite all text
        with open( file,"w") as writer:
            writer.write(text)


    def file_adder(self,file, text):
        with open(file,'a') as adder:
            adder.write(text)


    def file_reader(self,file):
        with open(file,"r") as reader:
            content = reader.read()
            return content


