# try:
#     filename = input("enter the filename:")
#     raise NameError("there is no such file name in systen..")
#     f = open(filename, 'r')
#     print(f.read())
#     with open(filename, 'w')as file:
#         file.write('HII DHEENA')
#     f.close()
# except NameError as e:
#     print("NameError Happened", e)
# else:
#     print("all good")

try:
    filename = input("Enter the filename: ")

    # Try to open the file in read mode
    with open(filename, 'r') as f:
        content = f.read()
        print("📄 File content:\n", content)

    # Writing to the file (optional)
    with open(filename, 'w') as file:
        file.write("HII DHEENA")

except FileNotFoundError:
    print("❌ NameError: There is no such file name in the system.")
except Exception as e:
    print("❌ Some other error occurred:", e)
else:
    print("✅ All good — file processed successfully.")
