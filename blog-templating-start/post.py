import requests

class Post:
    def all_post(self):
        self.response = requests.get('https://api.npoint.io/d6288bfdf3695e5d8f18')
        self.response.raise_for_status()
        self.data = self.response.json()
        return self.data


if __name__=='__main__':
    post = Post()
    data = post.all_post()
    for dt in data:
        if (dt['id']) == 1:
            print(f"Title: {dt['title']}\nSubtitle: {dt['subtitle']} \nBody: {dt['body']}\n")