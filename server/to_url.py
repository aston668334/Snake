import pyimgur

def to_url(PATH):
    """
    plt.figure(figsize=(240,240))
    plt.plot(ug)
    plt.savefig('send.png')
    """
    CLIENT_ID = "8fede842ec9cc9a"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur")

    return (uploaded_image.link)
