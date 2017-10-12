import datetime
from base64 import urlsafe_b64encode
from hashlib import md5


class CDN77:
    """
    Basic CDN77 secure link generation
    """
    def __init__(self, hostname, token):
        self.token = token
        self.hostname = hostname

    def get_download_link(self, path, expires_in_sec= 24*60*60):
        """
        returns full url of the resource, with secure token for option Secure Token "Parameter"
        :param path: full path for the resource, without /wwww/; i.e. for /www/myfile.png it is /myfile.png
        :param expires_in_sec: link will expire after this amt of seconds
        :return:
        """
        if path[0] != '/':
            path = '/' + path
        expires = int(datetime.datetime.utcnow().timestamp()) + expires_in_sec

        secret = md5(("%s%s%s" % (
            expires, path, self.token)).encode())

        secret = urlsafe_b64encode(secret.digest()).decode().rstrip('=')

        return self.hostname + path + "?secure=%s,%s" % (
            secret, expires)


if __name__ == '__main__':
    c = CDN77("https://xxxxxxxx.rsc.cdn77.org", "your_token_from_dashboard")
    print(c.get_download_link("2d.png"))
