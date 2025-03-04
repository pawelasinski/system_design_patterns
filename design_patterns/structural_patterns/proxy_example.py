"""Proxy

The `Proxy`_ pattern is a structural design pattern that provides a surrogate or placeholder
for another object, controlling access to it. A proxy acts as an intermediary,
managing tasks such as lazy initialization, access control, logging, or caching,
before delegating requests to the real object.

Why use it?
* Access control (restricts or grants access to the real object based on conditions).
* Lazy initialization (delays object creation until it's actually needed, improving performance).
* Logging and monitoring (captures requests for debugging, analytics, or security audits).
* Performance optimization (caches expensive operations to reduce redundant processing).

.. _Proxy:
    https://refactoring.guru/design-patterns/proxy

"""

from abc import ABC, abstractmethod


# Common interface
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


# Real object
class RealSubject(Subject):
    def request(self):
        print("Processing request by the real object.")


# Proxy object
class Proxy(Subject):
    def __init__(self, real_subject):
        self._real_subject = real_subject
        self._access_granted = False

    def grant_access(self):
        self._access_granted = True

    def request(self):
        if self._access_granted:
            print("Access check passed. Forwarding request to the real object.")
            self._real_subject.request()
        else:
            print("Access denied. Request rejected.")


if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)

    print("Attempting to call method through proxy without access: ")
    proxy.request()

    print("\nGranting access and retrying the call: ")
    proxy.grant_access()
    proxy.request()
