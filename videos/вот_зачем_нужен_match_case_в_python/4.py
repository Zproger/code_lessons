
def download_files(values: list):
    match values:
        case "download", file_url:
            print(f"Download file: {file_url}")
        case "download", file, *file_urls:
            print(f"Download files: {file, file_urls}")
        case _:
            print("default")

download_files(["download", "file1", "file2", "file3"])
download_files(["download", "file5"])
download_files(["hello world"])