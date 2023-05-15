def main():
    filename = input("File name: ").lower().strip()
    print(get_mediaType(filename))

def get_mediaType(filename):
    if filename.endswith('.gif'):
        return 'image/gif'
    elif filename.endswith('.jpg') or filename.endswith('.jpeg'):
        return 'image/jpeg'
    elif filename.endswith('.png'):
        return 'image/png'
    elif filename.endswith('.txt'):
        return 'text/plain'
    elif filename.endswith('.pdf'):
        return 'application/pdf'
    elif filename.endswith('.zip'):
        return 'application/zip'
    else:
        return 'application/octet-stream'

main()