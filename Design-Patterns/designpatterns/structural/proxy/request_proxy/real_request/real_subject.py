from designpatterns.structural.proxy.request_proxy.base_subject.subject import Subject


class RealSubject(Subject):
    """
    This is the class which implements
    abstract class Subject and contains main Business Logic.
    """
    def request(self) -> None:
        """
        Main request for access and use Business Resource.
        :return:
        """
        print("RealSubject: handling the request")
