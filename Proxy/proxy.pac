function FindProxyForURL(url, host)
{
    // If from facebook, use local proxy
    if (dnsDomainIs(host, ".facebook.com")) {
        return "PROXY 127.0.0.1:8080";
    } else {
        return "DIRECT";
    }
}
