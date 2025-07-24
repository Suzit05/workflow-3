def file_to_test(filename):
    with open (filename, "r") as f:
        return len(f.readlines())
            
