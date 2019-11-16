"""Entry point to demonstrate Proxy pattern."""
from designpatterns.structural.proxy.request_proxy.proxy_request import ProxySubject
from designpatterns.structural.proxy.request_proxy.real_request import RealSubject


if __name__ == '__main__':
    """Main entry point for the proxy."""
    print("Client: Client request access to use resource.")
    real_subject = RealSubject()
    proxy_subject = ProxySubject(real_subject)
    proxy_subject.request()
