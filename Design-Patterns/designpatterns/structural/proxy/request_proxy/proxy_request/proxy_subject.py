from designpatterns.structural.proxy.request_proxy.base_subject import Subject
from designpatterns.structural.proxy.request_proxy.real_request import RealSubject


class ProxySubject(Subject):
    """
    This is Proxy Subject which will act as proxy to real subject.
    """
    __real_subject = ''

    def __init__(self, real_subject: RealSubject) -> None:
        """
        Constructor for proxy Subject.
        :param real_subject: Real Subject Object.
        """
        self.__real_subject = real_subject

    def request(self) -> None:
        """
        Implementing request method for Proxy Subject.
        :return: None.
        """
        if self.__check_access():
            self.__real_subject.request()
            self.__log_access()
        pass

    def __check_access(self) -> bool:
        """
        Checking access prior to fire real request.
        :returns: True if as access
                False if no access
        """
        return True

    def __log_access(self) -> None:
        """
        Logging the time taken by the real resource to fulfill.
        :return: None.
        """
        print("Proxy: Logging the time of request.", end="")
