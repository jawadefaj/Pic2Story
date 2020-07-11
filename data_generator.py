import glob, os



def GetStory(foldername, outputname,  _nline):
    name = str(foldername)
    output_file_name = str(outputname)
    number_of_lines = int(_nline)
    print(name + "  " + output_file_name + "  " + str(_nline))
    os.chdir(name)
    output = []
    for file in glob.glob("*.txt"):
        f_temp = open(file, "r")
        content = f_temp.read()
        f_temp.close()
        content = content.split(".")
        if len(content) <= number_of_lines:
            output.append(content)
        else:
            output.append(content[0:number_of_lines]) 
    output_string = str(output) 
    print(output_string)       
    output_string = output_string.replace("\\n", " ")
    output_string = output_string.replace("\\n", " ")
    output_string = output_string.replace("[", " " )
    output_string = output_string.replace("]", " " )
    output_string = output_string.replace("' ,  '", " " )
    output_string = output_string.replace("', '", " " )
    f_out = open(output_file_name, "a+")
    f_out.write(output_string)
    print("saving file")
    f_out.close()


#part to get all the lines of  each story
# os.chdir(r"C:\Users\abjaw\Documents\GitHub\Pic2Story\clean\fairytale")
# output = []
# for file in glob.glob("*.txt"):
#     f_temp = open(file, "r")
#     content = f_temp.read()
#     f_temp.close()
#     content = content
#     output.append(content)
# output_string = str(output)

# #output_string = output_string.replace("\\n", " ")
# output_string = output_string.replace("\\n", " ")
# output_string = output_string.replace("[", " " )
# output_string = output_string.replace("]", " " )
# output_string = output_string.replace("' ,  '", " " )
# output_string = output_string.replace("', '", " " )
# print(output_string)

# os.chdir(r"C:\Users\abjaw\Documents\GitHub\Pic2Story\clean")
# f_out = open("GPT_alltext_fairytale.txt", "a+")
# f_out.write(output_string)
# f_out.close()





# #part to get first 30 lines of  each story
# os.chdir(r"C:\Users\abjaw\Documents\GitHub\Pic2Story\clean\fairytale")
# output = []
# for file in glob.glob("*.txt"):
#     f_temp = open(file, "r")
#     content = f_temp.read()
#     f_temp.close()
#     content = content.split(".")
#     if len(content) <= 30:
#         output.append(content)
#     else:
#         output.append(content[0:30]) 
# output_string = str(output)

# output_string = output_string.replace("\\n", " ")
# output_string = output_string.replace("  ", " ")
# output_string = output_string.replace("[", " " )
# output_string = output_string.replace("]", " " )
# output_string = output_string.replace("' ,  '", " " )
# output_string = output_string.replace("', '", " " )
# print(output_string)

# os.chdir(r"C:\Users\abjaw\Documents\GitHub\Pic2Story\clean")
# f_out = open("GPT_FirstThirtyLine.txt", "a+")
# f_out.write(output_string)
# f_out.close()


def main():
    GetStory(r"C:\Users\abjaw\Documents\GitHub\Pic2Story\clean\fairytale", r"temp_GPT_FirstThirtyLine.txt", 30)
    print("Just saying")


if __name__== "__main__":
    main()


