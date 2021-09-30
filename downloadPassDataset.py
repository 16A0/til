from joblib import delayed, Parallel
import os
import requests
import urllib.request as request


def get_image(url, index):
    try:
        response = requests.get(url)
        folder = str(index % 20)
        file_name = url.split('/')[-1]
        file = open(f"{TARGETDIR}/{folder}/{file_name}", "wb")
        file.write(response.content)
        file.close()
    except:
        print(f'download failed: {url}')
    if index % 50 == 0:
        print(f"{index}/1.4M done")




if __name__ == "__main__":
    TARGETDIR = "./pass"
    os.makedirs(TARGETDIR, exist_ok=True)
    print(f'will run and save to {TARGETDIR}', flush=True)
    for k in range(20):
        os.makedirs(os.path.join(TARGETDIR, str(k)), exist_ok=True)

    urls = request.urlretrieve('https://www.robots.ox.ac.uk/~vgg/research/pass/pass_urls.txt','pass_urls.txt')
    urls = open('pass_urls.txt', 'r').readlines()
    urls = [h.strip() for h in urls] # keep only image-hash
    START = 0
    _ = Parallel(n_jobs=-1)(delayed(get_image)(h,j) for j, h in enumerate(urls[START:]))
