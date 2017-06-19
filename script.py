import csvModule

csvModule.simple_function("hello")
frame = csvModule.create_dataframe_from_dir('./somebodys_data/', 6)
print(len(frame))
