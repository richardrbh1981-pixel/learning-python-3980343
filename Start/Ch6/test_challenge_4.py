#This retunrs the total size of all text files in the deps folder
def file_info():
    # Your code goes here.
    total_text_size = 0
    if path.exists("deps"):
        deps_path_src = path.realpath("deps")
        deps_files = os.listdir(deps_path_src)
        for file in deps_files:
            if ".txt" in file[-4:]:
                files_size = os.path.getsize(deps_path_src + "/" + file)
                total_text_size += files_size

        return total_text_size

print(file_info())